#!/usr/bin/env python3
"""Validate frontmatter in tool post files."""

import re
import sys
from pathlib import Path

import yaml

POSTS_DIR = Path("_posts")
TEMPLATE_FILE = POSTS_DIR / "_template.md"

# Required fields that must be present
REQUIRED_FIELDS = [
    "title",
    "category",
    "author",
    "external_link",
]

# Valid categories
VALID_CATEGORIES = {
    "Quality Analysis",
    "Helper Tools",
    "Subjective Test Software",
    "Streaming",
    "Encoding",
    "Content Preparation",
}

# Fields that should be boolean
BOOLEAN_FIELDS = ["broken_link"]

# Fields that should be strings (not lists/dicts unless specified)
STRING_FIELDS = [
    "title",
    "excerpt",
    "author",
    "license",
    "category",
    "external_link",
    "direct_download_link",
]


def extract_frontmatter(content: str) -> tuple[dict | None, str | None]:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return None, "No valid frontmatter found (must start with ---)"

    try:
        data = yaml.safe_load(match.group(1))
        return data, None
    except yaml.YAMLError as e:
        return None, f"YAML parsing error: {e}"


def validate_url(value: str, field_name: str) -> list[str]:
    """Validate that a URL field contains a valid URL, not markdown."""
    errors = []

    if not isinstance(value, str):
        errors.append(f"  - {field_name}: expected string URL, got {type(value).__name__}")
        return errors

    # Check for markdown link syntax [text](url)
    if re.match(r"^\[.*\]\(.*\)$", value.strip()):
        errors.append(f"  - {field_name}: contains markdown link syntax. Use plain URL instead.")

    # Check for obviously invalid URLs
    if value and not value.startswith(("http://", "https://", "ftp://")):
        # Allow empty strings
        if value.strip():
            errors.append(f"  - {field_name}: URL should start with http://, https://, or ftp://")

    return errors


def validate_frontmatter(data: dict, filepath: Path) -> list[str]:
    """Validate frontmatter fields."""
    errors = []

    # Check required fields
    has_broken_link = data.get("broken_link", False)
    for field in REQUIRED_FIELDS:
        # external_link is optional for tools with broken links
        if field == "external_link" and has_broken_link:
            continue
        if field not in data:
            errors.append(f"  - Missing required field: {field}")
        elif data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            # Allow empty strings for some fields
            # - excerpt is always optional
            # - external_link can be empty for tools with broken links
            if field == "excerpt":
                continue
            if field == "external_link" and has_broken_link:
                continue
            errors.append(f"  - Required field '{field}' is empty")

    # Validate category
    if "category" in data:
        cat = data["category"]
        if not isinstance(cat, str):
            errors.append(f"  - category: expected string, got {type(cat).__name__}")
        elif cat not in VALID_CATEGORIES:
            errors.append(f"  - category: invalid category '{cat}'. Must be one of: {', '.join(sorted(VALID_CATEGORIES))}")

    # Validate boolean fields
    for field in BOOLEAN_FIELDS:
        if field in data and data[field] is not None:
            if not isinstance(data[field], bool):
                errors.append(f"  - {field}: expected boolean (true/false), got {type(data[field]).__name__}: {data[field]}")

    # Validate string fields aren't lists (common YAML mistake)
    for field in STRING_FIELDS:
        if field in data and data[field] is not None:
            if isinstance(data[field], list):
                errors.append(f"  - {field}: expected string, got list. Check YAML syntax.")
            elif isinstance(data[field], dict):
                errors.append(f"  - {field}: expected string, got dict. Check YAML syntax.")

    # Validate URL fields
    if "external_link" in data and data["external_link"]:
        errors.extend(validate_url(data["external_link"], "external_link"))

    if "direct_download_link" in data and data["direct_download_link"]:
        errors.extend(validate_url(data["direct_download_link"], "direct_download_link"))

    # Validate tags format (can be space-separated string or list)
    if "tags" in data and data["tags"] is not None:
        tags = data["tags"]
        if not isinstance(tags, (str, list)):
            errors.append(f"  - tags: expected string or list, got {type(tags).__name__}")

    return errors


def main():
    """Main entry point."""
    all_errors = {}
    files_checked = 0

    for filepath in sorted(POSTS_DIR.glob("*.md")):
        # Skip template
        if filepath.name == "_template.md":
            continue

        files_checked += 1
        content = filepath.read_text(encoding="utf-8")

        data, parse_error = extract_frontmatter(content)

        if parse_error:
            all_errors[filepath] = [f"  - {parse_error}"]
            continue

        if data is None:
            all_errors[filepath] = ["  - Empty frontmatter"]
            continue

        errors = validate_frontmatter(data, filepath)
        if errors:
            all_errors[filepath] = errors

    # Report results
    print(f"Checked {files_checked} files")

    if all_errors:
        print(f"\nFound errors in {len(all_errors)} files:\n")
        for filepath, errors in all_errors.items():
            print(f"{filepath}:")
            for error in errors:
                print(error)
            print()
        sys.exit(1)
    else:
        print("All frontmatter is valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()

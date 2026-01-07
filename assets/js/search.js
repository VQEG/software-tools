(function() {
  'use strict';

  var searchInput = document.getElementById('search-input');
  var searchResults = document.getElementById('search-results');
  var searchOverlay = document.getElementById('search-overlay');

  var documents = [];
  var idx = null;

  // Load search index - use current page origin to avoid cross-origin issues
  var searchDataUrl = window.location.origin + '/software-tools/search-data.json';

  fetch(searchDataUrl)
    .then(function(response) { return response.json(); })
    .then(function(data) {
      documents = data;
      idx = lunr(function() {
        this.ref('id');
        this.field('title', { boost: 10 });
        this.field('content');
        this.field('tags', { boost: 5 });
        this.field('categories', { boost: 5 });

        data.forEach(function(doc, i) {
          doc.id = i;
          this.add(doc);
        }, this);
      });
    })
    .catch(function(err) {
      console.warn('Could not load search index:', err);
    });

  // Open search overlay
  window.openSearch = function() {
    if (searchOverlay) {
      searchOverlay.hidden = false;
      if (searchInput) {
        searchInput.focus();
      }
    }
  };

  // Close search overlay
  window.closeSearch = function() {
    if (searchOverlay) {
      searchOverlay.hidden = true;
      if (searchInput) {
        searchInput.value = '';
      }
      if (searchResults) {
        searchResults.innerHTML = '';
      }
    }
  };

  // Close on Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && searchOverlay && !searchOverlay.hidden) {
      closeSearch();
    }
    // Open on Ctrl/Cmd + K
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
  });

  // Close when clicking outside
  if (searchOverlay) {
    searchOverlay.addEventListener('click', function(e) {
      if (e.target === searchOverlay) {
        closeSearch();
      }
    });
  }

  // Perform search
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      var query = this.value.trim();
      if (query.length < 2 || !idx) {
        searchResults.innerHTML = '';
        return;
      }

      try {
        var results = idx.search(query + '*');
        displayResults(results, query);
      } catch (e) {
        // Handle search syntax errors
        searchResults.innerHTML = '<p>Invalid search query</p>';
      }
    });
  }

  function displayResults(results, query) {
    if (results.length === 0) {
      searchResults.innerHTML = '<p>No results found for "' + escapeHtml(query) + '"</p>';
      return;
    }

    var html = '<p>' + results.length + ' result' + (results.length === 1 ? '' : 's') + ' found</p>';
    results.slice(0, 10).forEach(function(result) {
      var doc = documents[result.ref];
      html += '<div class="search-result">';
      html += '<h3><a href="' + escapeHtml(doc.url) + '" onclick="closeSearch()">' + escapeHtml(doc.title) + '</a></h3>';
      if (doc.excerpt) {
        html += '<p>' + escapeHtml(doc.excerpt) + '</p>';
      }
      html += '</div>';
    });

    searchResults.innerHTML = html;
  }

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
})();

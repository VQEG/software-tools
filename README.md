# VQEG STL Website

Author: Werner Robitza

Go to [https://vqeg.github.io/software-tools/](https://vqeg.github.io/software-tools/) to view the site.

## Development

Install Ruby (2.4 or higher), then in this directory:

```
gem install bundler
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

You may also use `liveserve` instead of `serve` to trigger rebuilds.

## Updating Dependencies

If there are any updates needed, you can update the Gems with:

```
bundle update
```

This will install, among others, security updates. After updating,  Then, commit and push the `Gemfile` and `Gemfile.lock`.

## Checking Links

Install [GNU Parallel](https://www.gnu.org/software/parallel/) and run:

```
grep -hriE '(external_link:|direct_download_link:)' _posts/*.md | cut -d ":" -f2- | parallel --trim l --timeout 5 "curl -L -o /dev/null --silent --head --write-out '%{url_effective} %{http_code}\n' {}" 2>/dev/null | grep -v 200
```

This will print all non-200 links, which includes broken links or other errors. FTP is currently not supported.

## License

Copyright 2018 Werner Robitza

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# comic-scraper

Scrape webcomics from different sources and aggregate them in a single web page.

Hosted on Google App Engine: <http://comicscraper.appspot.com/>.

## Setup/Configuration

~~~~
git clone https://github.com/moretti/comic-scraper.git
cd comic-scraper
virtualenv -p /usr/bin/python2.7 --no-site-packages --distribute .
source bin/activate
pip install -r requirements.txt
~~~~

## Previewing the Application

To preview the application using App Engine's development server,
use [dev_appserver.py](http://code.google.com/appengine/docs/python/tools/devserver.html):

~~~~
dev_appserver.py src/
~~~~

Assuming the latest App Engine SDK is installed, the test environment is
available at <http://localhost:8080>.


## License 

(The MIT License)

Copyright (c) 2013 Paolo Moretti

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

~~~~
:::::::::::::
::         ::
:: Made at ::
::         ::
:::::::::::::
     ::
Hacker School
:::::::::::::
~~~~

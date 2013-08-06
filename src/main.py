import webapp2
import settings
import feeds

def get_feeds():
    urls = (
        'http://xkcd.com/rss.xml',
        'http://feeds.feedburner.com/thedoghousediaries/feed?format=xml',
        'http://feeds.feedburner.com/Foxtrotcom?format=xml',
        'http://www.phdcomics.com/gradfeed.php'
    )
    entries = []

    for url in urls:
        _, e = feeds.fetch_feed(url)
        entries += e

    entries.sort(key=lambda x: x.published)

    return entries

class Index(webapp2.RequestHandler):

    def get(self):
        entries = get_feeds()
        template = settings.JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render({'entries' : entries}))

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)

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
    feedz = []
    entries = []

    for url in urls:
        f, e = feeds.fetch_feed(url)
        feedz.append(f)
        entries += e

    feedz.sort(key=lambda x: x.title)
    entries.sort(key=lambda x: x.published)

    return feedz, entries

class Index(webapp2.RequestHandler):

    def get(self):
        feedz, entries = get_feeds()
        template = settings.JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render({'entries' : entries, 'feeds': feedz }))

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)

import webapp2
import settings
import feedfetcher


def get_feeds():
    urls = (
        'http://xkcd.com/rss.xml',
        'http://feeds.feedburner.com/thedoghousediaries/feed?format=xml',
        'http://feeds.feedburner.com/Foxtrotcom?format=xml',
        'http://www.phdcomics.com/gradfeed.php'
    )
    feeds = []
    entries = []

    for url in urls:
        feed, entry = feedfetcher.fetch(url)
        feeds.append(feed)
        entries += entry

    feeds.sort(key=lambda x: x.title)
    entries.sort(key=lambda x: x.published)

    return feeds, entries


class Index(webapp2.RequestHandler):

    def get(self):
        feeds, entries = get_feeds()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'templates/index.html')
        self.response.write(
            template.render({'entries': entries, 'feeds': feeds}))

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)

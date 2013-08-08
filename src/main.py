import datetime as dt
import webapp2
import settings
import feedfetcher
from google.appengine.ext import ndb
from models import Entry, Feed


def get_feeds():
    feeds = Feed.query().order(Feed.title)
    entries = Entry.query().order(-Entry.published)

    return feeds, entries


class Index(webapp2.RequestHandler):

    def get(self):
        feeds, entries = get_feeds()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'templates/index.html')
        self.response.write(
            template.render({'entries': entries, 'feeds': feeds}))


class Update(webapp2.RequestHandler):

    def get(self):
        an_hour_ago = dt.datetime.now() - dt.timedelta(hours=1)
        feeds = Feed.query(Feed.checked < an_hour_ago)

        for feed in feeds:
            self.update(feed.link)

    # TODO: Rewrite this code using `ndb.put_multi`:
    # https://developers.google.com/appengine/docs/python/ndb/entities#multiple
    #@ndb.transactional(xg=True)
    def update(self, url):
        feed, entries = feedfetcher.fetch(url)

        feed.key = ndb.Key('Feed', url)
        feed.checked = dt.datetime.now()
        feed.put()

        for entry in entries:
            entry_key = ndb.Key('Entry', entry.link)
            if entry_key.get() is None:
                entry.key = entry_key
                entry.feed = feed.key
                entry.put()


class CreateDefault(webapp2.RequestHandler):

    def get(self):
        default_urls = set((
            'http://xkcd.com/rss.xml',
            'http://feeds.feedburner.com/thedoghousediaries/feed?format=xml',
            'http://feeds.feedburner.com/Foxtrotcom?format=xml',
            'http://www.phdcomics.com/gradfeed.php',
        ))

        feeds = [Feed(key=ndb.Key('Feed', url), link=url) for url in default_urls]
        ndb.put_multi(feeds)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/update', Update),
    ('/createdefault', CreateDefault),
], debug=True)

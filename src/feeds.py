import feedparser
import models
import time
import datetime as dt


def fetch_feed(url):
    f = feedparser.parse(url)

    feed = models.Feed()
    feed.link = f.feed.get('link')
    feed.title = f.feed.get('title')
    feed.author = f.feed.get('author')

    entries = []
    for e in f.entries:
        entry = models.Entry()
        entry.link = e.get('link')
        entry.title = e.get('title')

        published = get_first_or_default(
            e, ('updated_parsed', 'published_parsed'))
        if published:
            entry.published = dt.datetime.fromtimestamp(time.mktime(published))

        entry.content = e.description

        entries.append(entry)

    return (feed, entries)


def get_first_or_default(d, sequence, default=None):
    for element in sequence:
        if element in d:
            return d[element]
    return default

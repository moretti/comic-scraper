import feedparser
import models
import time
import datetime as dt


def fetch_feed(url):
    f = feedparser.parse(url)

    feed = models.Feed()
    feed.url = f.feed.link
    feed.title = f.feed.title

    updated = get_first_or_default(
        f.feed, ('updated_parsed', 'published_parsed'))
    if updated:
        feed.updated = dt.datetime.fromtimestamp(time.mktime(updated))

    stories = []
    for entry in f.entries:
        story = models.Story()
        story.url = entry.link
        story.title = entry.title

        updated = get_first_or_default(
            entry, ('updated_parsed', 'published_parsed'))
        if updated:
            story.updated = dt.datetime.fromtimestamp(time.mktime(updated))

        story.content = entry.description

        stories.append(story)

    return (feed, stories)


def get_first_or_default(d, sequence, default=None):
    for element in sequence:
        if element in d:
            return d[element]
    return default

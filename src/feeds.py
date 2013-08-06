import feedparser
import models
import time
import datetime as dt


def fetch_feed(url):
    f = feedparser.parse(url)

    feed = models.Feed()
    feed.url = url
    feed.title = f.feed.title

    for prop in ('updated_parsed', 'published_parsed'):
        if prop in f.feed:
            feed.updated = dt.datetime.fromtimestamp(time.mktime(f.feed[prop]))

    stories = []
    for entry in f.entries:
        story = models.Story()
        story.url = entry.link
        story.title = entry.title

        for prop in ('updated_parsed', 'published_parsed'):
            if prop in entry:
                story.updated = dt.datetime.fromtimestamp(
                    time.mktime(entry[prop]))

        story.content = entry.description

        stories.append(story)

    return (feed, stories)

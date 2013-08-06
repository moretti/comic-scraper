import feedparser
import models
import time
import datetime as dt
from bs4 import BeautifulSoup

VALID_IMAGE_ATTRIBUTES = ('alt', 'title', 'src')


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

        if 'content' in e and e.content and isinstance(e.content, list):
            first_content = e.content[0]
            content = first_content.get('value')
        else:
            content = e.get('description')
        entry.content = content

        if content:
            entry.image_content = get_comic_image(content)

        entries.append(entry)

    return (feed, entries)


def get_comic_image(html):
    soup = BeautifulSoup(html)
    img = soup.find('img')
    if img:
        img.attrs = {key: value for key, value in img.attrs.iteritems() if key in VALID_IMAGE_ATTRIBUTES}
        return unicode(img)
    else:
        return None


def get_first_or_default(d, sequence, default=None):
    for element in sequence:
        if element in d:
            return d[element]
    return default

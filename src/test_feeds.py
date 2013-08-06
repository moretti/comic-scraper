import feeds


def test_feeds():
    url = 'http://xkcd.com/rss.xml'
    feed, stories = feeds.fetch_feed(url)

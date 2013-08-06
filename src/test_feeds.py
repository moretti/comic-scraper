import feeds
import os
from nose.tools import *

FEEDS = {
    'xkcd' : 'test_fixtures/xkcd.xml'
}

def test_xkcd_feed():
    feed_path = FEEDS['xkcd']
    feed, entries = feeds.fetch_feed(feed_path)

    assert_is_not_none(feed)
    assert_equal(feed.title, 'xkcd.com')
    assert_equal(feed.link, 'http://xkcd.com/')

    assert_is_not_none(entries)
    assert_equal(len(entries), 4)
    entry = entries[0]
    assert_equal(entry.title, 'The Mother of All Suspicious Files')
    assert_equal(entry.link, 'http://xkcd.com/1247/')
    assert_equal(entry.content, """<img alt="Better change the URL to 'https' before downloading." src="http://imgs.xkcd.com/comics/the_mother_of_all_suspicious_files.png" title="Better change the URL to 'https' before downloading." />""")
    assert_is_not_none(entry.published)
    assert_equal(entry.published.timetuple(), (2013, 8, 5, 4, 0, 0, 0, 217, -1))

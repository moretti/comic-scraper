import feeds
import os
from nose.tools import *

FEEDS = {
    'xkcd' : 'test_fixtures/xkcd.xml'
}

def test_xkcd_feed():
    feed_path = FEEDS['xkcd']
    feed, stories = feeds.fetch_feed(feed_path)

    assert_is_not_none(feed)
    assert_equal(feed.title, 'xkcd.com')
    assert_equal(feed.url, 'http://xkcd.com/')

    assert_is_not_none(stories)
    assert_equal(len(stories), 4)
    story = stories[0]
    assert_equal(story.title, 'The Mother of All Suspicious Files')
    assert_equal(story.url, 'http://xkcd.com/1247/')
    assert_equal(story.content, """<img alt="Better change the URL to 'https' before downloading." src="http://imgs.xkcd.com/comics/the_mother_of_all_suspicious_files.png" title="Better change the URL to 'https' before downloading." />""")
    assert_is_not_none(story.updated)
    assert_equal(story.updated.timetuple(), (2013, 8, 5, 4, 0, 0, 0, 217, -1))

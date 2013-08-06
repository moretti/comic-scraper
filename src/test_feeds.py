import feeds
import os
from nose.tools import *

FEEDS = {
    'xkcd': 'test_fixtures/xkcd.xml',
    'doghouse': 'test_fixtures/doghouse.xml',
    'foxtrot': 'test_fixtures/foxtrot.xml',
    'phdcomics': 'test_fixtures/phdcomics.xml',
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
    assert_equal(
        entry.content, """<img alt="Better change the URL to 'https' before downloading." src="http://imgs.xkcd.com/comics/the_mother_of_all_suspicious_files.png" title="Better change the URL to 'https' before downloading." />""")
    assert_equal(entry.image_content,
                 u"""<img alt="Better change the URL to 'https' before downloading." src="http://imgs.xkcd.com/comics/the_mother_of_all_suspicious_files.png" title="Better change the URL to 'https' before downloading."/>""")
    assert_is_not_none(entry.published)
    assert_equal(entry.published.timetuple(),
                 (2013, 8, 5, 4, 0, 0, 0, 217, -1))


def test_doghouse_feed():
    feed_path = FEEDS['doghouse']
    feed, entries = feeds.fetch_feed(feed_path)

    assert_is_not_none(feed)
    assert_equal(feed.title, 'DOGHOUSE')
    assert_equal(feed.link, 'http://thedoghousediaries.com')

    assert_is_not_none(entries)
    assert_equal(len(entries), 10)
    entry = entries[0]
    assert_equal(entry.title, 'Amazing Scientific Breakthroughs')
    assert_equal(
        entry.link, 'http://feedproxy.google.com/~r/thedoghousediaries/feed/~3/rml4PlBNLcs/5275')
    assert_equal(
        entry.content, """<p><img alt="Amazing Scientific Breakthroughs " class="comic-item comic-item-5275" height="2095" src="http://thedoghousediaries.com/comics/uncategorized/2013-08-05-9680a48.png" title="You know what they say, it&#8217;s better to have a late mouseover than to have no mouseover at all." width="800" /></p><p>For those hopeless optimists out there, here&#8217;s some catchy headline reads:<br />\n<span style="color: #0000ff;"><a href="http://news.wustl.edu/news/Pages/25061.aspx" target="_blank"><span style="color: #0000ff;">Nanoparticles loaded with bee venom kill HIV</span></a></span><br />\n<span style="color: #0000ff;"><a href="http://hereandnow.wbur.org/2013/05/09/protein-heart-disease" target="_blank"><span style="color: #0000ff;">Scientists Discover Protein That Reverses Heart Disease In Older Mice</span></a></span><br />\n<span style="color: #0000ff;"><a href="http://www.newscientist.com/article/dn22613-soupedup-immune-cells-force-leukaemia-into-remission.html#.Uf-QWZLOvEc" target="_blank"><span style="color: #0000ff;">Souped-up immune cells force leukaemia into remission</span></a></span><br />\n<span style="color: #0000ff;"><a href="http://www.ns.umich.edu/new/releases/20947-biofuel-breakthrough-quick-cook-method-turns-algae-into-oil" target="_blank"><span style="color: #0000ff;">Biofuel breakthrough: Quick cook method turns algae into oil</span></a></span><br />\n<span style="color: #0000ff;"><a href="http://www.extremetech.com/extreme/134672-harvard-cracks-dna-storage-crams-700-terabytes-of-data-into-a-single-gram" target="_blank"><span style="color: #0000ff;">Harvard cracks DNA storage, crams 700 terabytes of data into a single gram</span></a></span></p>\n<div class="tw_button" id="tweetbutton5275" style="float: left; margin-right: 10px;"><a class="twitter-share-button" href="http://twitter.com/share?url=http%3A%2F%2Fthedoghousediaries.com%2F5275&amp;via=willrayraf&amp;text=Amazing%20Scientific%20Breakthroughs&amp;related=&amp;lang=en&amp;count=none&amp;counturl=http%3A%2F%2Fthedoghousediaries.com%2F5275">Tweet</a></div><img height="1" src="http://feeds.feedburner.com/~r/thedoghousediaries/feed/~4/rml4PlBNLcs" width="1" />""")
    assert_equal(entry.image_content,
                 u"""<img alt="Amazing Scientific Breakthroughs " src="http://thedoghousediaries.com/comics/uncategorized/2013-08-05-9680a48.png" title="You know what they say, it\u2019s better to have a late mouseover than to have no mouseover at all."/>""")
    assert_is_not_none(entry.published)
    assert_equal(entry.published.timetuple(),
                 (2013, 8, 5, 12, 46, 56, 0, 217, -1))


def test_all_feeds():
    for feed_path in FEEDS.itervalues():
        feed, entries = feeds.fetch_feed(feed_path)
        check_feed(feed, entries)


def check_feed(feed, entries):
    assert_is_not_none(feed)
    assert_is_not_none(feed.title)
    assert_is_not_none(feed.link)

    assert_is_not_none(entries)
    for entry in entries:
            assert_is_not_none(entry.title)
            assert_is_not_none(entry.link)
            assert_is_not_none(entry.content)
            assert_is_not_none(entry.image_content) and assert_is_true(
                '<img' in entry.image_content)
            assert_is_not_none(entry.published)

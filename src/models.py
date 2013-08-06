from google.appengine.ext import ndb


class Feed(ndb.Model):
    title = ndb.StringProperty()
    link = ndb.StringProperty()
    description = ndb.StringProperty()
    author = ndb.StringProperty()
    checked = ndb.DateTimeProperty()


class Entry(ndb.Model):
    feed = ndb.KeyProperty()
    title = ndb.StringProperty()
    link = ndb.StringProperty()
    content = ndb.TextProperty()
    image_content = ndb.TextProperty()
    published = ndb.DateTimeProperty()
    checked = ndb.DateTimeProperty()

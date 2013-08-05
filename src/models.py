from google.appengine.ext import ndb


class Feed(ndb.Model):
    url = ndb.StringProperty()
    title = ndb.StringProperty()
    updated = ndb.DateTimeProperty()
    checked = ndb.DateTimeProperty()


class Story(ndb.Model):
    parent = ndb.KeyProperty()
    url = ndb.StringProperty()
    title = ndb.StringProperty()
    updated = ndb.DateTimeProperty()
    checked = ndb.DateTimeProperty()
    content = ndb.TextProperty()

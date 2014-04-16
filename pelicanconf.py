#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'cnsworder'
SITENAME = u'Linux Developer'
#SITEURL = ''
#SITEURL = 'http://docs.cnsworder.com'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          (u'问答', 'http://cnsworder.com'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/cnsworder'),
          ('github', 'https://github.com/cnsworder'),
          ('google+', 'https://plus.google.com/u/0/106278662052013132197/posts/p/pub'),)

DEFAULT_PAGINATION = 20

STATIC_PATHS = ([u'highlight', u'img', u'publication/image'])

#EXTRA_PATH_METADATA = 

#FILES_TO_COPY = (('publication/image/*', 'img/'),);

DISQUS_SITENAME = u"cnsworder"
#DISQUS_NO_ID = True

GITHUB_URL = u'http://github.com/cnsworder/staticdocs'

#THEME = "pelican-bootstrap3"
THEME = "bootstrap2"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

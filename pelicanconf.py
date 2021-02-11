#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'montoyamoraga'
SITENAME = 'texts'
SITEURL = 'https://montoyamoraga.io/texts'
THEME = './theme'
TIMEZONE = 'US/Eastern'
GITHUB_URL = "https://github.com/montoyamoraga/texts"
PATH = 'content'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# example RSS
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# static paths
STATIC_PATHS = ['extra/404.md']
EXTRA_PATH_METADATA = {'extra/404.md': {'path': '404.md'},}

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
        #  ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

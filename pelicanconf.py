#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

THEME = 'pure'

# THEME VARIABLES
#
COVER_IMG_URL = '/images/sidebar-banner.jpg'
# ===============

SITENAME = 'Meet the Carsons'
SITEURL = ''

TAGLINE = ''

AUTHOR = 'Amanda Carson'
AUTHOR_URL = 'author/{slug}/index.html'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = ['pages']

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_SAVE_AS = 'blog/{slug}/index.html'
CATEGORY_URL = 'blog/{slug}/'

USE_FOLDER_AS_CATEGORY = False

ARCHIVES_SAVE_AS = 'blog/archives/index.html'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%A %B %d, %Y'
DEFAULT_PAGENATION = 5
DEFAULT_CATEGORY = 'Uncategorized'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/meetthecarsons'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

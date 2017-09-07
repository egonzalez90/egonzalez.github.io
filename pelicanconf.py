#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eduardo Gonzalez'
SITENAME = 'OpenStack Stuff'
#SITEURL = 'http://egonzalez90.github.io'
THEME = 'themes/blueidea'
PATH = 'content'

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#PLUGIN_PATHS = ["plugins"]
#PLUGINS = ["disqus_static"]
DISQUS_SITENAME = 'egonzalez-1'
DISQUS_SHORTNAME = 'egonzalez-1'

# Blogroll
#LINKS = (('GitHub', 'https://github.com/egonzalez90'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/egongu90'),
          ('Linkedin', 'https://www.linkedin.com/in/eduardogonzalezgutierrez'),
          ('Github', 'https://github.com/egonzalez90'),)

DEFAULT_PAGINATION = 3
FEED_MAX_ITEMS = 5

TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

MENU_INTERNAL_PAGES = (
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
MENUITEMS = (
    ('OpenStack', 'https://docs.openstack.org'),
    ('Linkedin', 'https://www.linkedin.com/in/eduardogonzalezgutierrez'),
    ('Github', 'https://github.com/egonzalez90'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

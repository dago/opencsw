NAME = terminator
VERSION = 0.95
CATEGORIES = python

DESCRIPTION = Multiple GNOME terminals in one window
define BLURB
  Multiple GNOME terminals in one window
endef

MASTER_SITES = http://launchpad.net/terminator/trunk/$(VERSION)/+download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Just a bunch of paths used as fallback
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/terminatorlib/util.py

# App well known as terminator
CHECKPKG_OVERRIDES += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES += catalogname-does-not-start-with-py_

ARCHALL = 1

TEST_SCRIPTS =

include gar/category.mk

# $Id$
NAME = python-dateutil
VERSION = 1.5
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Dateutil provides powerful extensions to the standard python datetime module
define BLURB
  Dateutil offers functionality such as computing relative time deltas,
  computing dates based on flexible recurrence rules, generic parsing of
  dates, handling of tzfile(5) format files and computing of Easter
  Sunday for various calendars.
endef

MASTER_SITES = http://labix.org/download/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
SPKG_SOURCEURL = http://labix.org/$(NAME)/
BUILD_DEP_PKGS = CSWpy-setuptools
PACKAGES = CSWpy-dateutil

UPSTREAM_MASTER_SITES = http://labix.org/python-dateutil/

TEST_SCRIPTS = dateutil

LICENSE = LICENSE
ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpy-dateutil += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/dateutil/tz.py

include gar/category.mk

test-dateutil:
	(cd $(WORKSRC); python test.py)
	@$(MAKECOOKIE)

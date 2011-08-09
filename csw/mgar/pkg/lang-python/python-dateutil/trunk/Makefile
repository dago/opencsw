# $Id$
NAME = python-dateutil
VERSION = 1.5
CATEGORIES = python

DESCRIPTION = Dateutil provides powerful extensions to the standard python datetime module
define BLURB
  Dateutil offers functionality such as computing relative time deltas,
  computing dates based on flexible recurrence rules, generic parsing of
  dates, handling of tzfile(5) format files and computing of Easter
  Sunday for various calendars.
endef

MASTER_SITES = http://labix.org/download/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
SPKG_SOURCEURL = http://labix.org/$(NAME)/
BUILD_DEP_PKGS = CSWpysetuptools
PACKAGES = CSWpy-dateutil
CATALOGNAME = py_dateutil

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

UPSTREAM_MASTER_SITES = http://labix.org/python-dateutil/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS = dateutil

LICENSE = LICENSE
ARCHALL = 1

include gar/category.mk

test-dateutil:
	(cd $(WORKSRC); python test.py)
	@$(MAKECOOKIE)

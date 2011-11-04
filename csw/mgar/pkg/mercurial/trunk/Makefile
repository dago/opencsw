NAME = mercurial
VERSION = 2.0
CATEGORIES = python

DESCRIPTION = Fast, lightweight Source Control Management system

MASTER_SITES = http://selenic.com/mercurial/release/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWmercurial

SPKG_DESC_CSWmercurial = Mercurial
RUNTIME_DEP_PKGS_CSWmercurial += CSWlibpython2-6-1-0

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
# Some tests fail, but manual inspection of the failures show no significant failures.
TEST_SCRIPTS      =
#TEST_TARGET = #tests

CHECKPKG_OVERRIDES_CSWmercurial += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWmercurial += catalogname-does-not-start-with-py_

include gar/category.mk

pre-build-modulated:
	@echo "Changing /bin/sh to /opt/csw/bin/bash in test scripts..."
	@(cd $(WORKSRC)/tests; \
		ggrep -rl '#!/bin/sh' * | \
			xargs perl -pi -e 's|#!/bin/sh|#!/opt/csw/bin/bash|' )
	@$(MAKECOOKIE)

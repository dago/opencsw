# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = twisted
MAJ_VERSION = 8.2
PATCHLEVEL = 0
GARVERSION = $(MAJ_VERSION).$(PATCHLEVEL)
CATEGORIES = lib

DESCRIPTION = An event-driven networking engine
define BLURB
  Twisted is a networking engine written in Python, supporting numerous
  protocols. It contains a web server, numerous chat clients, chat servers,
  mail servers, and more.
endef

DLOAD_NAME = Twisted

MASTER_SITES = http://tmrc.mit.edu/mirror/$(GARNAME)/$(DLOAD_NAME)/$(MAJ_VERSION)/
DISTFILES  = $(DLOAD_NAME)-$(GARVERSION).tar.bz2

WORKSRC = $(WORKDIR)/$(DLOAD_NAME)-$(GARVERSION)
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS = CSWcswclassutils CSWpython CSWpython-rt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = twisted
TEST_SCRIPTS =
INSTALL_SCRIPTS = twisted

PROTOTYPE_FILTER = awk ' \
  $$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } \
  { print }'

build-twisted:
	(cd $(WORKSRC); python setup.py build)
	@$(MAKECOOKIE)

install-twisted:
	(cd $(WORKSRC); python setup.py install --root=$(DESTDIR))
	@$(MAKECOOKIE)

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)

include gar/category.mk

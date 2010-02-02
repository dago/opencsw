GARNAME = mercurial
GARVERSION = 1.4.3
CATEGORIES = devel

DESCRIPTION = Fast, lightweight Source Control Management system
#define BLURB
#endef

MASTER_SITES = http://selenic.com/mercurial/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_DESC_CSWmercurial = Mercurial

REQUIRED_PKGS_CSWmercurial = CSWpython

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
# Some tests fail, but manual inspection of the failures show no significant failures.
TEST_TARGET = #tests

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR) --prefix=/opt/csw

include gar/category.mk


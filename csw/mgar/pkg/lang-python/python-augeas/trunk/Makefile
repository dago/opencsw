NAME = python-augeas
VERSION = 0.3.0
CATEGORIES = python

DESCRIPTION = Augeas Python Bindings
define BLURB
endef

MASTER_SITES = http://augeas.net/download/python/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://augeas.net

PACKAGES = CSWpyaugeas
CATALOGNAME = py_augeas

DEP_PKGS = CSWaugeas

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 
# TEST_TARGET = check

ARCHALL = 1

include gar/category.mk

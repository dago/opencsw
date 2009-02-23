GARNAME = pygobject
GARVERSION = 2.15.4
CATEGORIES = lang

DESCRIPTION = pygobject support for Python
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.15/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += fixme.sh

PACKAGES = CSWpygobject
REQUIRED_PKGS_CSWpygobject  = CSWpython CSWggettextrt CSWglib2


CATALOGNAME_CSWpygobject = py_gobject
SPKG_DESC_CSWpygobject = pygobject support for Python

## patch to change zero sized struct to zero-sized sub-object
PATCHFILES = pygobject.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

## Tests require gtk, but gtk requries gobject
#TEST_TARGET = check
TEST_SCRIPTS = 

include gar/category.mk

post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

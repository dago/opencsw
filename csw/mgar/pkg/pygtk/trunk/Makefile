GARNAME = pygtk
GARVERSION = 2.12.1
CATEGORIES = lang

DESCRIPTION = pygobject support for Python define BLURB
  This is a Python language binding for gobject.
  endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.12/
	DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
	DISTFILES += fixme.sh

PACKAGES = CSWpygtk
REQUIRED_PKGS_CSWpygtk  = CSWpython CSWggettextrt CSWglib2 CSWgtk2 CSWpango
REQUIRED_PKGS_CSWpygtk += CSWlibatk CSWlibcairo CSWlibglade2 CSWlibxml2


CATALOGNAME_CSWpygobject = py_gobject
SPKG_DESC_CSWpygtk = pygtk support for Python

# We define upstream file regex so we can be notifed 
# of new upstream software release

UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)

## Tests require gtk, but gtk requries gobject
#TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk

post-configure-modulated:
	echo "==> Fixing Libtool ==>"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)
							

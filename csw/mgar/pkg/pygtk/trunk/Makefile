GARNAME = pygtk
GARVERSION = 2.12.1
CATEGORIES = lang

DESCRIPTION = pygtk support for Python
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.15/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += fixme.sh

PACKAGES = CSWpygtk
REQUIRED_PKGS_CSWpygtk  = CSWpython 

EXTRA_CFLAGS = -I../../pygobject/work/install-isa-sparcv8/usr/local/include/pygtk-2.0
EXTRA_LINKER_FLAGS = -L../../pygobject/work/install-isa-sparcv8/usr/local/lib

CATALOGNAME_CSWpygtk = py_gtk
SPKG_DESC_CSWpygtk = pygtk support for Python

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

#TEST_TARGET = check
TEST_SCRIPTS = 

include gar/category.mk

post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

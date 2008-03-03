GARNAME = libglade
GARVERSION = 0.17
CATEGORIES = lib

DESCRIPTION = library to load Glade XML user interface files at runtime
define BLURB
Libglade is a library that performs a similar job to the C source output routines in the GLADE user interface builder. Whereas GLADE's output routines create C source code that must be compiled, libglade builds the interface from an XML file (GLADE's save format) at runtime. This can allow modifying the user interface without recompiling.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/libglade/0.17/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibglade,)

CONFIGURE_ARGS = $(DIRPATHS) --disable-nls

TEST_SCRIPTS =

include gar/category.mk

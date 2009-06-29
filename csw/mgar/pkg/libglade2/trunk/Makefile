GARNAME = libglade
GARVERSION = 2.6.4
CATEGORIES = lib
RELVER = $(shell echo $(GARVERSION) |gsed 's/\(^[0-9].*\.[0-9].*\)\.[0-9]*/\1/')

DESCRIPTION = library to load Glade XML user interface files at runtime
define BLURB
Libglade is a library that performs a similar job to the C source output routines in the GLADE user interface builder. Whereas GLADE's output routines create C source code that must be compiled, libglade builds the interface from an XML file (GLADE's save format) at runtime. This can allow modifying the user interface without recompiling.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/libglade/$(RELVER)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWlibglade2
CATALOGNAME = libglade2
SPKG_DESC = $(DESCRIPTION)
SPKG_SOURCEURL = http://www.gnome.org/

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

include gar/category.mk

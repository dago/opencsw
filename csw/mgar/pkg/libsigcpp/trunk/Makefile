GARNAME = libsigc++
GARVERSION = 2.2.6
CATEGORIES = lib

DESCRIPTION = Typesafe signal and callback system for C++
define BLURB
  Typesafe signal and callback system for C++
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES  = CSWlibsigc++rt
PACKAGES += CSWlibsigc++devel
SPKG_DESC_CSWlibsigc++rt = Typesafe signal and callback system for C++
SPKG_DESC_CSWlibsigc++devel = Header files and docs for libsigc++

PKGFILES_CSWlibsigc++devel = /opt/csw/share/.*
PKGFILES_CSWlibsigc++devel += /opt/csw/include/.*
PKGFILES_CSWlibsigc++devel += /opt/csw/lib/pkgconfig/.*
PKGFILES_CSWlibsigc++devel += /opt/csw/lib/sigc\+\+-2.0/include/.*

CATALOGNAME_CSWlibsigc++rt= libsigc++_rt
CATALOGNAME_CSWlibsigc++devel = libsigc++_devel 

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
BUILD64 = 1
NOISAEXEC = 1
TEST_TARGET = check

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)

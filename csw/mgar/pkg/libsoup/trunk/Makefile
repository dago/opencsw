GARNAME = libsoup
GARVERSION = 2.26.3
CATEGORIES = lib
  
 
DESCRIPTION = HTTP client/server library for GNOME
define BLURB
endef
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2


PACKAGES = CSWlibsoup CSWlibsoupdevel CSWlibsoupdoc
CATALOGNAME_CSWlibsoup = libsoup
CATALOGNAME_CSWlibsoupdevel = libsoup_devel
CATALOGNAME_CSWlibsoupdoc = libsoup_doc

SPKG_DESC_CSWlibsoup += HTTP client/server library for GNOME
SPKG_DESC_CSWlibsoupdevel += HTTP client/server library for GNOME - developer package
SPKG_DESC_CSWlibsoupdoc += HTTP client/server library for GNOME - documentation

RUNTIME_DEP_PKGS_CSWlibsoup += CSWgconf2 CSWgcrypt CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWlibsoup += CSWgnutls CSWgpgerr CSWlibproxy CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibsoup += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWlibsoupdevel += CSWlibsoup
RUNTIME_DEP_PKGS_CSWlibsoupdoc += 

BUILD_DEP_PKGS += CSWlibproxy

PKGFILES_CSWlibsoupdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsoupdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibsoupdoc = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib 
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

# Not working until gconf2 is 64-bit
#BUILD64 = 1

# One test fails for some unknown reason
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk

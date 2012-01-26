NAME = webkit
VERSION = 1.1.15.4
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Portable web rendering engine
define BLURB
endef

MASTER_SITES =  http://www.webkitgtk.org/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWwebkit CSWwebkitdevel CSWwebkitdoc
CATALOGNAME_CSWwebkit = webkit
CATALOGNAME_CSWwebkitdevel = webkit_devel
CATALOGNAME_CSWwebkitdoc = webkit_doc

SPKG_DESC_CSWwebkit += $(DESCRIPTION)
SPKG_DESC_CSWwebkitdevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWwebkitdoc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWwebkitdevel += CSWwebkit
RUNTIME_DEP_PKGS_CSWwebkitdoc += CSWwebkit

BUILD_DEP_PKGS += CSWenchantdevel CSWgperf CSWlibicudevel CSWlibsoupdevel
BUILD_DEP_PKGS += CSWgstreamer

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.webkitgtk.org/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
# libdbus not 64-bit yet
#BUILD64 = 1

PKGFILES_CSWwebkitdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWwebkitdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWwebkitdoc = 1

LIBS = -lsocket -lnsl
export LIBS

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

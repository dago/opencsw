NAME = evolution-mapi
VERSION = 0.28.2
CATEGORIES = gnome

DESCRIPTION = Evolution extension for MS Exchange 2007 servers
define BLURB
	A provider for Evolution that can connect to Exchange 2007 servers and
	also to Exchange 2003, 2000 and 5.5.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWevolutionmapi CSWevolutionmapidev CSWevolutionmapidoc
CATALOGNAME_CSWevolutionmapi = evolution_mapi
CATALOGNAME_CSWevolutionmapidev = evolution_mapi_devel
CATALOGNAME_CSWevolutionmapidoc = evolution_mapi_doc

SPKG_DESC_CSWevolutionmapi += Evolution extension for MS Exchange 2007 servers
SPKG_DESC_CSWevolutionmapidevel += Evolution extension for MS Exchange 2007 servers - developer package
SPKG_DESC_CSWevolutionmapidoc += Evolution extension for MS Exchange 2007 servers - documentation

RUNTIME_DEP_PKGS_CSWevolutionmapi += 
RUNTIME_DEP_PKGS_CSWevolutionmapi += 
RUNTIME_DEP_PKGS_CSWevolutionmapi += 
RUNTIME_DEP_PKGS_CSWevolutionmapidev += CSWevolutionmapi
RUNTIME_DEP_PKGS_CSWevolutionmapidoc += CSWevolutionmapi

PKGFILES_CSWevolutionmapidev = $(PKGFILES_DEVEL)
PKGFILES_CSWevolutionmapidoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWevolutionmapidoc = 1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://projects.gnome.org/evolution

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

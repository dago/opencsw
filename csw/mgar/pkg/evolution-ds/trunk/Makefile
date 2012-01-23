NAME = evolution-data-server
VERSION = 2.28.2
CATEGORIES = gnome

DESCRIPTION = Evolution database backend server
define BLURB
	The data server, called "Evolution Data Server" is responsible for
	managing calendar and addressbook information.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWevolution-ds CSWevolution-ds-devel CSWevolution-ds-doc
CATALOGNAME_CSWevolution-ds = evolution_ds
CATALOGNAME_CSWevolution-ds-devel = evolution_ds_devel
CATALOGNAME_CSWevolution-ds-doc = evolution_ds_doc

SPKG_DESC_CSWevolution-ds += Evolution database backend server
SPKG_DESC_CSWevolution-ds-devel += Evolution database backend server - developer package
SPKG_DESC_CSWevolution-ds-doc += Evolution database backend server - documentation

RUNTIME_DEP_PKGS_CSWevolution-ds += 
RUNTIME_DEP_PKGS_CSWevolution-ds += 
RUNTIME_DEP_PKGS_CSWevolution-ds += 
RUNTIME_DEP_PKGS_CSWevolution-dsdevel += CSWevolution
RUNTIME_DEP_PKGS_CSWevolution-dsdoc += CSWevolution

PKGFILES_CSWevolution-dsdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWevolution-dsdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWevolution-dsdoc = 1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL =http://projects.gnome.org/evolution

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

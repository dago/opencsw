NAME = evolution-exchange
VERSION = 2.28.2
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Evolution Web Calendar
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWevolutionexchange CSWevolutionexchange-devel CSWevolutionexchange-doc
CATALOGNAME_CSWevolutionexchange = evolution_webcal
CATALOGNAME_CSWevolutionexchange-devel = evolution_webcal_devel
CATALOGNAME_CSWevolutionexchange-doc = evolution_webcal_doc

SPKG_DESC_CSWevolutionexchange += Evolution Web Calendar
SPKG_DESC_CSWevolutionexchange-devel += Evolution Web Calendar - developer package
SPKG_DESC_CSWevolutionexchange-doc += Evolution Web Calendar - documentation

RUNTIME_DEP_PKGS_CSWevolutionexchange += 
RUNTIME_DEP_PKGS_CSWevolutionexchange += 
RUNTIME_DEP_PKGS_CSWevolutionexchange += 
RUNTIME_DEP_PKGS_CSWevolutionexchange-devel += CSWevolution
RUNTIME_DEP_PKGS_CSWevolutionexchange-doc += CSWevolution

PKGFILES_CSWevolutionexchange-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWevolutionexchange-doc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWevolutionexchange-doc = 1

INCOMPATIBLE_PKGS_CSWevolutionexchange = CSWximian-connector 

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL =http://projects.gnome.org/evolution-webcal

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

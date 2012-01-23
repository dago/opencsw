NAME = evolution-webcal
VERSION = 2.28.0
CATEGORIES = gnome

DESCRIPTION = Evolution Web Calendar
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWevolutionwebcal CSWevolutionwebcal-devel CSWevolutionwebcal-doc
CATALOGNAME_CSWevolutionwebcal = evolution_webcal
CATALOGNAME_CSWevolutionwebcal-devel = evolution_webcal_devel
CATALOGNAME_CSWevolutionwebcal-doc = evolution_webcal_doc

SPKG_DESC_CSWevolutionwebcal += Evolution Web Calendar
SPKG_DESC_CSWevolutionwebcal-devel += Evolution Web Calendar - developer package
SPKG_DESC_CSWevolutionwebcal-doc += Evolution Web Calendar - documentation

RUNTIME_DEP_PKGS_CSWevolutionwebcal += 
RUNTIME_DEP_PKGS_CSWevolutionwebcal += 
RUNTIME_DEP_PKGS_CSWevolutionwebcal += 
RUNTIME_DEP_PKGS_CSWevolutionwebcal-devel += CSWevolution
RUNTIME_DEP_PKGS_CSWevolutionwebcal-doc += CSWevolution

PKGFILES_CSWevolutionwebcal-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWevolutionwebcal-doc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWevolutionwebcal-doc = 1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL =http://projects.gnome.org/evolution-webcal

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

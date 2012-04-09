# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfconf
VERSION = 4.9.0
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfconf is a simple client-server configuration storage and query system
define BLURB
   Xfconf is a simple client-server configuration storage and query system
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Catalog description
PACKAGES = CSWxfconf CSWxfconf-dev CSWxfconf-doc

# Package description
SPKG_DESC_CSWxfconf      = $(DESCRIPTION)
SPKG_DESC_CSWxfconf-dev  = $(DESCRIPTION) development package
SPKG_DESC_CSWxfconf-doc  = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWxfconf-dev   = $(PKGFILES_DEVEL)
PKGFILES_CSWxfconf-dev  += /opt/csw/include/xfce4/xfconf/.*
PKGFILES_CSWxfconf-doc   = /opt/csw/share/gtk-doc/.*

# Required packages for compilation
BUILD_DEP_PKGS  = CSWpmglib CSWpmextutilsdepends CSWpmextutpkgconf

# Defines dependencies
ARCHALL_CSWxfconf-doc = 1
RUNTIME_DEP_PKGS_CSWxfconf-dev += CSWxfconf

RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibxfce4util
RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWxfconf      += CSWperl
RUNTIME_DEP_PKGS_CSWxfconf      += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWxfconf-dev  += CSWxfconf
RUNTIME_DEP_PKGS_CSWxfconf-doc   =

#PATCHFILES = xf-conf-locking-utils.h.diff xfconf-gvaluefuncs.h.diff Makefile.PL.in.diff

SITEPREFIX = /opt/csw/share
export SITEPREFIX

TEST_SCRIPTS =

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)


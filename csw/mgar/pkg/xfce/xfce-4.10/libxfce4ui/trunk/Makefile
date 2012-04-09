# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libxfce4ui
VERSION = 4.9.1
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Share commonly used Xfce widgets amoung the Xfce applications
define BLURB
  libxfce4ui is the replacement of the old libxfce4ui library. It is used to share commonly used Xfce widgets amoung the Xfce applications.
endef

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWlibxfce4ui CSWlibxfce4ui-dev CSWlibxfce4ui-doc

# Package description
SPKG_DESC_CSWlibxfce4ui       = $(DESCRIPTION)
SPKG_DESC_CSWlibxfce4ui-dev   = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfce4ui-doc   = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWlibxfce4ui-dev    = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfce4ui-dev   += /opt/csw/include/xfce4/libxfce4ui/.*
PKGFILES_CSWlibxfce4ui-doc    = /opt/csw/share/gtk-doc/.*

# Defines dependencies
RUNTIME_DEP_PKGS_CSWlibxfce4ui-dev   = 
RUNTIME_DEP_PKGS_CSWlibxfce4ui-doc   = 

ARCHALL_CSWlibxfce4ui-doc = 1
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWpango
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWxfconf
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui += CSWlibxfce4util
RUNTIME_DEP_PKGS_CSWlibxfce4ui-dev += CSWlibxfce4ui

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 

CONFIGURE_ARGS  = $(DIRPATHS)

CPPFLAGS += -I/opt/csw/include/gtk-2.0
CPPFLAGS += -I/opt/csw/lib/gtk-2.0/include/
CPPFLAGS += -I/opt/csw/include/cairo
CPPFLAGS += -I/opt/csw/include/pango-1.0
CPPFLAGS += -I/opt/csw/include/gdk-pixbuf-2.0
CPPFLAGS += -I/opt/csw/include/atk-1.0/

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)

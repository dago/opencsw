# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfce4-settings
VERSION = 4.9.4
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Configuration system for the Xfce desktop environment
define BLURB
  Configuration system for the Xfce desktop environment
endef

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Catalog description
PACKAGES = CSWxfce4settings CSWxfce4settings-doc

# Package description
SPKG_DESC_CSWxfce4settings       = $(DESCRIPTION)
SPKG_DESC_CSWxfce4settings-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWxfce4settings-doc   = 1

# Dynamic prototype
PKGFILES_CSWxfce4settings-doc  = /opt/csw/share/gtk-doc/.*

# Defines dependencies


CPPFLAGS += -I/opt/csw/include/gtk-2.0
CPPFLAGS += -I/opt/csw/lib/gtk-2.0/include/
CPPFLAGS += -I/opt/csw/include/cairo
CPPFLAGS += -I/opt/csw/include/pango-1.0
CPPFLAGS += -I/opt/csw/include/gdk-pixbuf-2.0
CPPFLAGS += -I/opt/csw/include/atk-1.0/
CPPFLAGS += -I/opt/csw/include/xfce4/libxfce4ui-1/
CPPFLAGS += -I/opt/csw/include/xfce4/
CPPFLAGS += -I/opt/csw/include/exo-1/
CPPFLAGS += -I/opt/csw/include/xfce4/libxfce4kbd-private-2

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)

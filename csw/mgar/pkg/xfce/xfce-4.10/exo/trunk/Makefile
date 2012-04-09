# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = exo
VERSION = 0.7.2
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce Extensions Library 
define BLURB
   Xfce Extensions Library 
endef


PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# Catalog description
PACKAGES = CSWexo CSWexo-dev CSWexo-doc

# Package description
SPKG_DESC_CSWexo       = $(DESCRIPTION)
SPKG_DESC_CSWexo-dev   = $(DESCRIPTION) development package
SPKG_DESC_CSWexo-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWexo-doc     = 1
ARCHALL_CSWexo-dev     = 1

# Dynamic prototype
PKGFILES_CSWexo-dev    = $(PKGFILES_DEVEL)
PKGFILES_CSWexo-doc    = /opt/csw/share/gtk-doc/.*

# Defines dependencies

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-python --enable-hal

CPPFLAGS += -I/opt/csw/include/gtk-2.0
CPPFLAGS += -I/opt/csw/lib/gtk-2.0/include/
CPPFLAGS += -I/opt/csw/include/cairo
CPPFLAGS += -I/opt/csw/include/pango-1.0
CPPFLAGS += -I/opt/csw/include/gdk-pixbuf-2.0
CPPFLAGS += -I/opt/csw/include/atk-1.0/
CPPFLAGS += -I/opt/csw/include/xfce4/libxfce4ui-1/

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)



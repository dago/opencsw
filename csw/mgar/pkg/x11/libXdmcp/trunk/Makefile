GARNAME = libXdmcp
GARVERSION = 1.0.2
CATEGORIES = x11

DESCRIPTION = X11 display manager control protocol library
define BLURB
  This package provides the main interface to the X11 display manager control
  protocol library, which allows for remote logins to display managers. 
endef

MASTER_SITES = http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxdmcp CSWlibxdmcpdevel
CATALOGNAME_CSWlibxdmcp = libxdmcp
CATALOGNAME_CSWlibxdmcpdevel = libxdmcp_devel

REQUIRED_PKGS_CSWlibxdmcpdevel = CSWlibxdmcp

SPKG_DESC_CSWlibxdmcp = X11 display manager control protocol library
SPKG_DESC_CSWlibxdmcpdevel = X11 display manager control protocol library development package

PKGFILES_CSWlibxdmcpdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/include/.*
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/lib/pkgconfig/.*

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk

post-merge:
	gln -s . $(PKGROOT)$(libdir)/32
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)


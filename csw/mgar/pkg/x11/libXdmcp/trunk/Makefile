GARNAME = libXdmcp
GARVERSION = 1.0.2
CATEGORIES = x11

DESCRIPTION = X11 display manager control protocol library
define BLURB
This package provides the main interface to the X11 display manager control protocol library, which allows for remote logins to display managers. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES    += $(call admfiles,CSWlibxdmcpdevel, )
DISTFILES    += $(call admfiles,CSWlibxdmcp, )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxdmcp = X11 display manager control protocol library
SPKG_DESC_CSWlibxdmcpdevel = X11 display manager control protocol library development package

PKGFILES_CSWlibxdmcpdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/include/.*
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/lib/pkgconfig/.*
PKGFILES_CSWlibxdmcpdevel += $(prefix)/share/doc/$(GARNAME)/License-devel.txt

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)

pre-install:
	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME) 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(DISTNAME)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)/License.txt 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(DISTNAME)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)/License-devel.txt 

include gar/category.mk



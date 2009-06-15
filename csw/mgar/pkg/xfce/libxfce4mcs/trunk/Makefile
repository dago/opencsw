GARNAME = libxfce4mcs
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager Library 
define BLURB
   Xfce Settings Manager Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWlibxfce4mcs.depend CSWlibxfce4mcs.gspec CSWlibxfce4mcs.prototype
# DISTFILES += CSWlibxfce4mcsdoc.depend CSWlibxfce4mcsdoc.gspec CSWlibxfce4mcsdoc.prototype
# DISTFILES += CSWlibxfce4mcsdev.depend CSWlibxfce4mcsdev.gspec CSWlibxfce4mcsdev.prototype
DISTFILES += $(call admfiles,CSWlibxfce4mcs, )
DISTFILES += $(call admfiles,CSWlibxfce4mcsdoc, )
DISTFILES += $(call admfiles,CSWlibxfce4mcsdev, )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Generate description fields
SPKG_DESC_CSWlibxfce4mcs      = $(DESCRIPTION)
SPKG_DESC_CSWlibxfce4mcsdoc   = $(DESCRIPTION) documentation
SPKG_DESC_CSWlibxfce4mcsdev   = $(DESCRIPTION) development package

# Dynamic prototype
PKGFILES_CSWlibxfce4mcsdev  = $(PKGFILES_DEVEL)

# Dependencies tracking

include gar/category.mk

# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfce4-power-manager
VERSION = 1.0.11
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = This software is a power manager for the Xfce desktop
define BLURB
  This software is a power manager for the Xfce desktop, Xfce power manager manages the power sources on the computer and the devices that can be controlled to reduce their power consumption (such as LCD brightness level, monitor sleep, CPU frequency scaling). In addition, xfce4-power-manager provides a set of freedesktop-compliant DBus interfaces to inform other applications about current power level so that they can adjust their power consumption, and it provides the inhibit interface which allows applications to prevent automatic sleep actions via the power manager; as an example, the operating system’s package manager should make use of this interface while it is performing update operations.
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# Catalog description
PACKAGES = CSWxfce4powermanager CSWxfce4powermanager-dev CSWxfce4powermanager-doc

# Package description
SPKG_DESC_CSWxfce4powermanager       = $(DESCRIPTION)
SPKG_DESC_CSWxfce4powermanager-dev   = $(DESCRIPTION) development package
SPKG_DESC_CSWxfce4powermanager-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWxfce4powermanager-doc   = 1
ARCHALL_CSWxfce4powermanager-dev   = 1

# Dynamic prototype
PKGFILES_CSWxfce4powermanager-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWxfce4powermanager-dev += /opt/csw/include/xfce4/xfce4powermanager/.*
PKGFILES_CSWxfce4powermanager-doc  = /opt/csw/share/gtk-doc/.*

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)



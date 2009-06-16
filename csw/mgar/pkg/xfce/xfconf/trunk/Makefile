GARNAME = xfconf
CATEGORIES = xfce

DESCRIPTION = Xfconf is a simple client-server configuration storage and query system
define BLURB
   Xfconf is a simple client-server configuration storage and query system
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# Don't forget to add this after checking dependencies with panel CSWxfconfdep.preinstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Catalog description
PACKAGES = CSWxfconf CSWxfconfdevel CSWxfconfdoc

CATALOGNAME_CSWxfconf      = xfconf
CATALOGNAME_CSWxfconfdevel = xfconf_devel
CATALOGNAME_CSWxfconfdoc   = xfconf_doc

# Package description
SPKG_DESC_CSWxfconf      = $(DESCRIPTION)
SPKG_DESC_CSWxfconfdevel = $(DESCRIPTION) development package
SPKG_DESC_CSWxfconfdoc   = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWxfconfdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWxfconfdevel += /opt/csw/include/xfce4/xfconf/.*
PKGFILES_CSWxfconfdoc    = /opt/csw/share/gtk-doc/.*

# Required packages for compilation
PREREQUISITE_PKGS        = CSWpmglib CSWpmextutilsdepends CSWpmextutpkgconf

# Defines dependencies
REQUIRED_PKGS_CSWxfconf      = CSWpmglib CSWpmextutilsdepends CSWpmextutpkgconf CSWdbusglib
REQUIRED_PKGS_CSWxfconf     += CSWggettextrt CSWglib2 CSWiconv CSWlibdbus CSWlibxfce4util
REQUIRED_PKGS_CSWxfconfdevel = 
REQUIRED_PKGS_CSWxfconfdoc   = 

PATCHFILES = xf-conf-locking-utils.h.diff xfconf-gvaluefuncs.h.diff Makefile.PL.in.diff

SITEPREFIX = /opt/csw/share
export SITEPREFIX

# BUILD64 = 1
# NOISALIST = 1

TEST_SCRIPTS = 

include gar/category.mk

post-install:
	( rm -fr $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))/opt/csw/lib/perl )


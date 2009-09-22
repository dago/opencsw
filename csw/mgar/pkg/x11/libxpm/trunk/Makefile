GARNAME = libxpm
GARVERSION = 3.5.7
CATEGORIES = x11

DESCRIPTION = X11 pixmap library
define BLURB
  LibXpm provides support and common operation for the XPM pixmap format,
  which is commonly used in legacy X applications. XPM is an extension of
  the monochrome XBM bitmap.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXpm-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# CSWxpm is the legacy library
PACKAGES = CSWlibxpm CSWlibxpmdevel CSWxpm

CATALOGNAME_CSWlibxpm = libxpm
CATALOGNAME_CSWlibxpmdevel = libxpm_devel

SPKG_DESC_CSWlibxpm = X11 pixmap library
SPKG_DESC_CSWlibxpmdevel = X11 pixmap library development files

REQUIRED_PKGS_CSWlibxpm = CSWlibice CSWlibsm CSWlibx11 CSWlibxext CSWlibxt
REQUIRED_PKGS_CSWlibxpmdevel = CSWlibxpm
REQUIRED_PKGS_CSWxpm = CSWlibxpm

PKGFILES_CSWlibxpmdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWxpm  = /opt/csw/bin/.*
PKGFILES_CSWxpm += /opt/csw/lib/.*

BUILD64 = 1
NO_ISAEXEC = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis
CONFIGURE_ARGS = $(DIRPATHS)

# We don't want optimized binaries, optimized libs are sufficient
        MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-sparcv8plus+vis = $(libdir)
          MERGE_DIRS_isa-amd64 = $(libdir)

include gar/category.mk

post-merge:
ifeq ($(GARCH),sparc)
	@ginstall -d $(PKGROOT)/opt/csw/lib/sparcv8plus+vis
	ln -s ../../X11/lib/sparcv8plus+vis/libXpm.so.4.11 $(PKGROOT)/opt/csw/lib/sparcv8plus+vis
	ln -s ../../X11/lib/sparcv8plus+vis/libXpm.so.4 $(PKGROOT)/opt/csw/lib/sparcv8plus+vis
	ln -s ../../X11/lib/sparcv8plus+vis/libXpm.so $(PKGROOT)/opt/csw/lib/sparcv8plus+vis
	@ginstall -d $(PKGROOT)/opt/csw/lib/sparcv9
	ln -s ../../X11/lib/sparcv9/libXpm.so.4.11 $(PKGROOT)/opt/csw/lib/sparcv9
	ln -s ../../X11/lib/sparcv9/libXpm.so.4 $(PKGROOT)/opt/csw/lib/sparcv9
	ln -s ../../X11/lib/sparcv9/libXpm.so $(PKGROOT)/opt/csw/lib/sparcv9
endif
	@ginstall -d $(PKGROOT)/opt/csw/lib
	ln -s ../X11/lib/libXpm.so.4.11 $(PKGROOT)/opt/csw/lib
	ln -s ../X11/lib/libXpm.so.4 $(PKGROOT)/opt/csw/lib
	ln -s ../X11/lib/libXpm.so $(PKGROOT)/opt/csw/lib
	@ginstall -d $(PKGROOT)/opt/csw/bin
	ln -s ../X11/bin/sxpm $(PKGROOT)/opt/csw/bin
	ln -s ../X11/bin/cxpm $(PKGROOT)/opt/csw/bin
	@$(MAKECOOKIE)

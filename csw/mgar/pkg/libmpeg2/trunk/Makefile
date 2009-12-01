GARNAME = libmpeg2
GARVERSION = 0.5.1
CATEGORIES = lib

DESCRIPTION = A free MPEG-2 video stream decoder
define BLURB
endef

MASTER_SITES = http://libmpeg2.sourceforge.net/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES  = 0001-Don-t-use-arm-specific-assembly-on-Sparc.patch
PATCHFILES += 0002-Fix-return-type-for-Sun-Studio.patch
PATCHFILES += 0003-Add-missing-m4-files.patch
PATCHFILES += 0004-Add-missing-libtool.patch
PATCHFILES += 0005-Add-missing-autostuff.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibmpeg2 CSWmpeg2dec

SPKG_DESC_CSWlibmpeg2 = A free MPEG-2 video stream library
SPKG_DESC_CSWmpeg2dec = A free MPEG-2 video stream decoder

REQUIRED_PKGS_CSWmpeg2dec = CSWlibmpeg2 CSWlibsdl

SPKG_SOURCEURL = http://libmpeg2.sourceforge.net

PACKAGING_PLATFORMS = solaris8-sparc solaris8-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# This stupid configure script adds '-fast' overwriting -xarch ande especially activating 64 bit.
BUILD_ARGS = MPEG2DEC_CFLAGS= OPT_CFLAGS=

BUILD64_platform-solaris8-sparc = 1
BUILD64_platform-solaris10-sparc = 1
BUILD64_platform-solaris10-i386 = 1
BUILD64 = $(BUILD64_platform-$(PLATFORM))

NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS_garosrel-5.8  = --x-includes=/usr/openwin/include
CONFIGURE_ARGS_garosrel-5.8 += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS_garosrel-5.10  = --x-includes=/usr/X11/include
CONFIGURE_ARGS_garosrel-5.10 += --x-libraries=/usr/X11/lib 

CONFIGURE_ARGS += $(CONFIGURE_ARGS_garosrel-$(GAROSREL))

MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWmpeg2dec = $(bindir)/.*
PKGFILES_CSWmpeg2dec += $(mandir)/man1/.*

include gar/category.mk

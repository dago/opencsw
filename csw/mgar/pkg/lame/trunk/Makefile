NAME = lame
VERSION = 3.99.1
CATEGORIES = apps

DESCRIPTION = LAME is an LGPL MP3 encoder
define BLURB
  LAME is a high quality MPEG Audio Layer III (MP3) encoder licensed under the LGPL.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://lame.sourceforge.net/

# For powf, fabsf, log10f only in libm on Solaris 10
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES += CSWlame
SPKG_DESC_CSWlame = LAME is an LGPL MP3 encoder
RUNTIME_DEP_PKGS_CSWlame += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlame += CSWlibiconv2

PACKAGES += CSWlame-mp3x
SPKG_DESC_CSWlame-mp3x = LAME Frame Analyzer for X11
PKGFILES_CSWlame-mp3x = .*/mp3x
RUNTIME_DEP_PKGS_CSWlame-mp3x += CSWglib
RUNTIME_DEP_PKGS_CSWlame-mp3x += CSWgtk
RUNTIME_DEP_PKGS_CSWlame-mp3x += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlame-mp3x += CSWlibiconv2

PACKAGES += CSWlibmp3lame-dev
SPKG_DESC_CSWlibmp3lame-dev = Development files for libmp3lame.so.0
PKGFILES_CSWlibmp3lame-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibmp3lame-dev = CSWlibmp3lame0
OBSOLETED_BY_CSWlibmp3lame-dev += CSWlame-devel

PACKAGES += CSWlibmp3lame0
SPKG_DESC_CSWlibmp3lame0 = Library for LAME, libmp3lame.so.0
PKGFILES_CSWlibmp3lame0 = $(call pkgfiles_lib,libmp3lame.so.0)

BUILD64 = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium_pro

# Disable intrinsics until this has been resolved:
#   https://sourceforge.net/tracker/?func=detail&aid=3150289&group_id=290&atid=100290
# CONFIGURE_ARGS_isa-i386 = --without-nasm
CONFIGURE_ARGS_isa-i386 = ac_cv_header_xmmintrin_h=no
CONFIGURE_ARGS_isa-pentium_pro = ac_cv_header_xmmintrin_h=no

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-mp3x
CONFIGURE_ARGS += --enable-mp3rtp
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

include gar/category.mk

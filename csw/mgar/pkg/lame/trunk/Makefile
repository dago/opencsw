NAME = lame
VERSION = 3.98.4
CATEGORIES = apps

DESCRIPTION = LAME is an LGPL MP3 encoder
define BLURB
  LAME is a high quality MPEG Audio Layer III (MP3) encoder licensed under the LGPL.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWlame CSWlame-mp3x CSWlame-devel CSWlibmp3lame0

CATALOGNAME_CSWlame = lame
CATALOGNAME_CSWlame-mp3x = lame_mp3x
CATALOGNAME_CSWlame-devel = lame_devel
CATALOGNAME_CSWlibmp3lame0 = libmp3lame0

SPKG_DESC_CSWlame = $(DESCRIPTION)
SPKG_DESC_CSWlame-mp3x = LAME Frame Analyzer for X11
SPKG_DESC_CSWlame-devel = Development files for LAME
SPKG_DESC_CSWlibmp3lame0 = Librare for LAME providing libmp3lame.so.0

RUNTIME_DEP_PKGS_CSWlame = CSWncurses
RUNTIME_DEP_PKGS_CSWlame-mp3x = CSWglib CSWgtk CSWncurses
RUNTIME_DEP_PKGS_CSWlame-devel = CSWlibmp3lame0


PKGFILES_CSWlame-mp3x = .*/mp3x
PKGFILES_CSWlame-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibmp3lame0 = $(call baseisadirs,$(libdir),libmp3lame\.so\.0(\.\d+)*)

VENDOR_URL = http://lame.sourceforge.net/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=628063
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

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

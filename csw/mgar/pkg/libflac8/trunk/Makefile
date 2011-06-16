NAME = libflac
VERSION = 1.2.1
CATEGORIES = lib

DESCRIPTION = Free lossless audio codec
define BLURB
  FLAC stands for Free Lossless Audio Codec, an audio format similar
  to MP3, but lossless, meaning that audio is compressed in FLAC without
  any loss in quality. This is similar to how Zip works, except with FLAC
  you will get much better compression because it is designed specifically
  for audio, and you can play back compressed FLAC files in your favorite
  player (or your car or home stereo, see supported devices) just like you
  would an MP3 file.
endef

SF_PROJ = flac
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

PATCHFILES += libtool-64bit.patch
PATCHFILES += strip-nasm-1.2.1.patch
PATCHFILES += no-stdint.patch
PATCHFILES += 0004-Preserve-norunpath-in-libtool.patch

BUILD_DEP_PKGS += CSWbash

PACKAGES += CSWlibflac8
CATALOGNAME_CSWlibflac8 = libflac8
SPKG_DESC_CSWlibflac8 = Free lossless audio codec library, libflac.so.8
PKGFILES_CSWlibflac8 = $(call pkgfiles_lib,libFLAC.so.8)
RUNTIME_DEP_PKGS_CSWlibflac8 += CSWlibogg0
OBSOLETED_BY_CSWlibflac8 = CSWlibflac

PACKAGES += CSWlibflac++6
CATALOGNAME_CSWlibflac++6 = libflac++6
SPKG_DESC_CSWlibflac++6 = Free lossless audio codec library, libFLAC++.so.6
PKGFILES_CSWlibflac++6 = $(call pkgfiles_lib,libFLAC++.so.6)
RUNTIME_DEP_PKGS_CSWlibflac++6 += CSWlibflac8
OBSOLETED_BY_CSWlibflac++6 = CSWlibflac

PACKAGES += CSWlibflac-dev
CATALOGNAME_CSWlibflac-dev = libflac_dev
SPKG_DESC_CSWlibflac-dev = Development files for libflac.so.8
PKGFILES_CSWlibflac-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibflac-dev += $(docdir)/flac/.*
RUNTIME_DEP_PKGS_CSWlibflac-dev = CSWlibflac8
RUNTIME_DEP_PKGS_CSWlibflac-dev += CSWlibflac++6

PACKAGES += CSWflac
CATALOGNAME_CSWflac = flac
SPKG_DESC_CSWflac = Utility programs for the Free Lossless Audio Codec (FLAC)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWflac += CSWlibogg0
RUNTIME_DEP_PKGS_CSWflac += CSWiconv
RUNTIME_DEP_PKGS_CSWflac += CSWlibflac8

PACKAGES += CSWxmms-flac
PKGFILES_CSWxmms-flac = $(libdir)/xmms/.*
SPKG_DESC_CSWxmms-flac = XMMS plugin for the FLAC audio file format
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWglib
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibogg0
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWgtk
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibflac8
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWxmms
OBSOLETED_BY_CSWxmms-flac = CSWxmmsflac
CATALOGNAME_CSWxmmsflac = xmms_flac_stub

VENDOR_URL = http://flac.sourceforge.net/

LICENSE = $(foreach lic,FDL GPL LGPL Xiph,COPYING.$(lic))

EXTRA_LINKER_FLAGS = -norunpath

# Must be defined and empty or -I$(includedir) is added too early
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS) -D__inline=

STRIP_LIBTOOL = 1

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CONFIGURE_ARGS_mm-64 = --disable-xmms-plugin
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# XXX: Assembler optimization just doesn't work. Disable for now.
CONFIGURE_ARGS += --disable-asm-optimizations

# Testsuite takes forever, disable once for new version
SKIPTEST ?= 1

EXTRA_PAX_ARGS = -s ',$(docdir)/flac-$(VERSION),$(docdir)/flac,'

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/share/doc,$(docdir),' \
		$(DESTDIR)$(mandir)/man1/flac.1

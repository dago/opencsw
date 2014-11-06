NAME = flac
VERSION = 1.3.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Free lossless audio codec
define BLURB
  FLAC stands for Free Lossless Audio Codec, an audio format similar
  to MP3, but lossless, meaning that audio is compressed in FLAC without
  any loss in quality. This is similar to how Zip works, except with FLAC
  you will get much better compression because it is designed specifically
  for audio, and you can play back compressed FLAC files in your favorite
  player (or your car or home stereo, see supported devices) just like you
  would an MASTER_SITES += http://downloads.xiph.org/releases/flac/
DISTFILES += $(DISTNAME).tar.xz

GARCOMPILER = GNU-in-libtool.patch

BUILD_DEP_PKGS += CSWbash

PACKAGES += CSWlibflac8
CATALOGNAME_CSWlibflac8 = libflac8
SPKG_DESC_CSWlibflac8 = Free lossless audio codec library, libflac.so.8
PKGFILES_CSWlibflac8 = $(call pkgfiles_lib,libFLAC.so.8)
RUNTIME_DEP_PKGS_CSWlibflaRUNTIME_DEP_PKGS_CSWlibflac8 += CSWlibgcc-s1lac8 = CSWlibflac

PACKAGES += CSWlibflac++6
CATALOGNAME_CSWlibflac++6 = libflac++6
SPKG_DESC_CSWlibflac++6 = Free lossless audio codec library, libFLAC++.so.6
PKGFILES_CSWlibflac++6 = $(call pkgfiles_lib,libFLAC++.so.6)
RUNTIME_DEP_PKGS_CSWlibflac++RUNTIME_DEP_PKGS_CSWlibflac++6 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibflac++6 += CSWlibstdc++6c++6 = CSWlibflac

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
RUNTIME_DEP_PKGS_iconv2Wflac += CSWiconv
RUNTIME_DEP_PKGS_CSWflaency|CSWlibflac7

PACKAGES += CSWxmms-flac
PKGFILES_CSWxmms-flac = $(libdir)/xmms/.*
SPKG_DESC_CSWxmms-flac = XMMS plugin for the FLAC audio file format
RUNTIME_DEP_PKGS_CSlibglib1-2-0
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibgtk1-2-0
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibgdk1-2-0ms-flac += CSWgtk
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibflac8
RUNTIME_DEP_PKGS_CSWxmms-flaRUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxmms-flac += CSWlibgcc-s1
OBSOLETED_BY_CSWxmms-flac = CSWxmmsflac
CATALOGNAME_CSWxmmsflac = xmms_flac_stub

# This is because XMMS is not available in 64 bit
CHECKPKG_OVERRIDES_CSWxmms-flac += 64-bit-binaries-missing

VENDOR_URL = http://flac.sourceforge.net/

LICENSE = $(foreach lic,FDL GPL LGPL Xiph,COPYING.$(lic))

#S = -norunpath

# Must be defined and empty or -I$(includedir) is#CPPFLAGS =
#early
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS) -D__inline=

STRIP_LIBTOOL = 1

BUILD6#EXTRA_CFLAGS += -xc99=all
#GARFLAVOR = DBG

CONFIGURE_ARGS = $(DIRPATHS)

# There is no XMMS in 64 bitGS = $(DIRPATHS)

EXTRA_CONFIGURE_ARGS_mm-64 = --disable-xmms-plugin
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# XXX: Assembler optimization just doesn't work. Disable for now.
CONFIGURE_ARGS += --disable-asn
SKIPTEST ?= 1

EXTRA_PAX_ARGS = -s ',$(docdir)/flac-$(VERSION),$(docdir)/flac,'

include gar/cextract:
	cd $(WORKSRC)/test && perl -e 's,#!/bin/sh,#!/bin/bash,' -npi *.sh
	@$(MAKECOOKIE)e gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/share/doc,$(docdir),' \
		$(DESTDIR)$(man
NAME = faad2
VERSION = 2.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Freeware Advanced Audio (AAC) Decoder including SBR decoding
define BLURB
  FAAD2 is an open source MPEG-4 and MPEG-2 AAC decoder, it is licensed
  under the GPLv2 licensECTe.
endef

SF_PROJ = faac
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES  = 0001-Remove-iquote-from-CFLAGS-unknown-to-SS.patch
PATCHFILES += 0002-Use-inline-suitable-for-SS.patch
PATCHFILES += 0003-Use-inttypes-instead-of-stdint.patch
PATCHFILES += 0004-Remove-Wall-from-xmms-plugin.patch

VENDOR_URL = http://www.audiocoding.com/faad2.html

BUILD_DEP_PKGS += CSWlibxmms-dev

PACKAGES += CSWfaad2
CATALOGNAME_CSWfaad2 = faad2
SPKG_DESC_CSWfaad2 = AAC utility program
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWfaad2 += CSWlibfaad2

PACKAGES += CSWlibfaad2
SPKG_DESC_CSWlibfaad2 = Freeware Advanced Audio (AAC) Decoder including SBR decoding, libfaad.so.2
PKGFILES_CSWlibfaad2 += $(call pkgfiles_lib,libfaad.so.2)

PACKAGES += CSWlibfaad-dev
SPKG_DESC_CSWlibfaad-dev = Development files for libfaad.so.2
PKGFILES_CSWlibfaad-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibfaad-dev += CSWlibfaad2

PACKAGES += CSWxmms-faad2
SPKG_DESC_CSWxmms-faad2 = XMMS plugin for the AAC audio file format
PKGFILES_CSWxmms-faad2 += $(libdir)/xmms/.*
RUNTIME_DEP_PKGS_CSWxmms-faad2 += CSWglib
RUNTIME_DEP_PKGS_CSWxmms-faad2 += CSWgtk
RUNTIME_DEP_PKGS_CSWxmms-faad2 += CSWlibxmms1
OBSOLETED_BY_CSWxmms-faad2 += CSWxmmsfaad2
CATALOGNAME_CSWxmmsfaad2 = xmms_faad2_stub

STRIP_LIBTOOL = 1

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-drm

CONFIGURE_ARGS-32 = --with-xmms
CONFIGURE_ARGS-64 = 
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# This is a hard package... add when ready.
# CONFIGURE_ARGS += --with-mpeg4ip

CHECKPKG_OVERRIDES_CSWxmms-faad2 += soname-not-found|libfaad.so.0|is|needed|by|opt/csw/lib/xmms/Input/libmp4.so

include
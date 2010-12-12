NAME = faad2
VERSION = 2.7
CATEGORIES = lib

DESCRIPTION = Freeware Advanced Audio (AAC) Decoder including SBR decoding
define BLURB
  FAAD2 is an open source MPEG-4 and MPEG-2 AAC decoder, it is licensed
  under the GPLv2 license.
endef

SF_PROJ = faac
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES  = 0001-Remove-iquote-from-CFLAGS-unknown-to-SS.patch
PATCHFILES += 0002-Use-inline-suitable-for-SS.patch
PATCHFILES += 0003-Use-inttypes-instead-of-stdint.patch
PATCHFILES += 0004-Remove-Wall-from-xmms-plugin.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SF_PROJ)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWfaad2 CSWxmmsfaad2
CATALOGNAME_CSWfaad2 = faad2
CATALOGNAME_CSWxmmsfaad2 = xmms_faad2

SPKG_DESC_CSWfaad2 = $(DESCRIPTION)
SPKG_DESC_CSWxmmsfaad2 = AAC plugin for XMMS

BUILD_DEP_PKGS = CSWxmms
RUNTIME_DEP_PKGS_CSWfaad2 = 
RUNTIME_DEP_PKGS_CSWxmmsfaad2 = CSWxmms CSWglib CSWgtk

VENDOR_URL = http://www.audiocoding.com/faad2.html

STRIP_LIBTOOL = 1

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS-32 = --with-xmms
CONFIGURE_ARGS-64 = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-drm
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# This is a hard package... add when ready.
# CONFIGURE_ARGS += --with-mpeg4ip

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWxmmsfaad2 = $(libdir)/xmms/.*

CHECKPKG_OVERRIDES_CSWxmmsfaad2 += soname-not-found|libfaad.so.0|is|needed|by|opt/csw/lib/xmms/Input/libmp4.so

include gar/category.mk

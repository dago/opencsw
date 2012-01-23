NAME = taglib
VERSION = 1.6.3
CATEGORIES = lib

DESCRIPTION = Library for reading and editing the meta-data of several popular audio formats
define BLURB
  TagLib is a library for reading and editing the meta-data of several popular audio formats.
  Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags
  and Vorbis comments in FLAC, MPC, Speex, WavPack and TrueAudio files.
endef

MASTER_SITES = http://developer.kde.org/~wheeler/files/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = 0001-Make-sure-m64-is-passed-to-the-linker.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYING.MPL

VENDOR_URL = http://developer.kde.org/~wheeler/taglib.html

PACKAGES += CSWtaglib
CATALOGNAME_CSWtaglib = taglib
SPKG_DESC_CSWtaglib = Library for reading and editing the meta-data of several popular audio formats
RUNTIME_DEP_PKGS_CSWtaglib = CSWlibtag1 CSWlibtag-c0
CHECKPKG_OVERRIDES_CSWtaglib += surplus-dependency|CSWlibtag-c0
CHECKPKG_OVERRIDES_CSWtaglib += surplus-dependency|CSWlibtag1
ARCHALL_CSWtaglib = 1
PKGFILES_CSWtaglib = NOFILES

PACKAGES += CSWtaglib-devel
CATALOGNAME_CSWtaglib-devel = taglib_devel
SPKG_DESC_CSWtaglib-devel = Developer files for taglib (composed of libtag1 and libtag_c0)
RUNTIME_DEP_PKGS_CSWtaglib-devel = CSWlibtag1 CSWlibtag-c0
PKGFILES_CSWtaglib-devel = $(PKGFILES_DEVEL)

PACKAGES += CSWlibtag1
CATALOGNAME_CSWlibtag1 = libtag1
SPKG_DESC_CSWlibtag1 += Library for reading and editing the meta-data of several popular audio formats, libtag.so.1
RUNTIME_DEP_PKGS_CSWlibtag1 += CSWzlib
PKGFILES_CSWlibtag1 += $(call baseisadirs,$(libdir),libtag\.so\.1(\.\d+)*)

PACKAGES += CSWlibtag-c0
CATALOGNAME_CSWlibtag-c0 = libtag_c0
SPKG_DESC_CSWlibtag-c0 += Library for reading and editing the meta-data of several popular audio formats, libtag_c.so.0
PKGFILES_CSWlibtag-c0 += $(call baseisadirs,$(libdir),libtag_c\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibtag-c0 += CSWlibtag1
RUNTIME_DEP_PKGS_CSWlibtag-c0 += CSWzlib

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

# There are collisions with the existing taglib_gcc at the moment. These will go away
# as soon as the updated taglib_gcc has been released.
CHECKPKG_OVERRIDES_CSWlibtag-c0 += file-collision
CHECKPKG_OVERRIDES_CSWlibtag1 += file-collision
CHECKPKG_OVERRIDES_CSWtaglib-devel += file-collision

include gar/category.mk

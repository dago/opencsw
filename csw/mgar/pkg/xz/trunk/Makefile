NAME = xz
VERSION = 5.0.1
CATEGORIES = utils

DESCRIPTION = XZ Utils is free data compression software with high compression ratio
define BLURB
  XZ Utils is free general-purpose data compression software with high compression
  ratio. XZ Utils were written for POSIX-like systems (GNU/Linux, *BSDs, etc.), but
  also work on some not-so-POSIX systems like Windows. XZ is based on the LZMA2
  algorithm. The implementation is much more heavywight than lzip.
endef

MASTER_SITES = http://tukaani.org/xz/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES = 0001-Do-not-force-inclusion-of-stdint.h.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWxz
CATALOGNAME_CSWxz = xz
SPKG_DESC_CSWxz = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWxz += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxz += CSWliblzma5

PACKAGES += CSWlzma
CATALOGNAME_CSWlzma = lzma
SPKG_DESC_CSWlzma = Stub to the successor xz
RUNTIME_DEP_PKGS_CSWlzma = CSWxz
CHECKPKG_OVERRIDES_CSWlzma += surplus-dependency|CSWxz
PKGFILES_CSWlzma = NOFILES
ARCHALL_CSWlzma = 1

PACKAGES += CSWliblzma5
CATALOGNAME_CSWliblzma5 = liblzma5
SPKG_DESC_CSWliblzma5 = LZMA Compression Library providing liblzma.so.5
PKGFILES_CSWliblzma5 = $(call baseisadirs,$(libdir),liblzma\.so\.5(\.\d+)*)
RUNTIME_DEP_PKGS_CSWliblzma5 += CSWgcc4corert

PACKAGES += CSWliblzma-dev
CATALOGNAME_CSWliblzma-dev = liblzma_dev
SPKG_DESC_CSWliblzma-dev = Development Files for liblzma
PKGFILES_CSWliblzma-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWliblzma-dev += CSWliblzma5

GARCOMPILER = GNU

BUILD64 = 1
NOISAEXEC = 1

# Assembler integration broken in amd64
CONFIGURE_ARGS_isa-amd64 = --disable-assembler

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

# Workaround for reported bug:
#   <http://sourceforge.net/projects/lzmautils/forums/forum/708858/topic/3500014>
CONFIGURE_ARGS += gl_cv_cc_visibility=no

MERGE_DIRS_isa-extra = $(libdir)

# not able to figure out which target runs the tests in "tests"
TEST_TARGET = check

include gar/category.mk

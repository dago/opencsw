GARNAME = bzip2
GARVERSION = 1.0.5
CATEGORIES = utils

# BUILD_DEP_PKGS =  CSWggettext CSWgit

# RUNTIME_DEP_PKGS = CSWiconv CSWggettextrt

# INCOMPATIBLE_PKGS =

DESCRIPTION = bzip2 Compressiion Utility
define BLURB
bzip2 is a freely available, patent free, high-quality data compressor. It typically
compresses files to within 10% to 15% of the best available techniques (the PPM family of
statistical compressors), whilst being around twice as fast at compression and six
times faster at decompression.
endef

MASTER_SITES = http://www.bzip.org/$(GARVERSION)/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES   = 0001-CFLAGS-LDFLAGS-for-SOS12-shared-lib.patch
PATCHFILES  += 0002-test-should-depend-on-bzip2.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES    = CSWbzip2
CATALOGNAME = bzip2

BUILD64     = 1
GARCOMPILER = SOS12

CFLAGS  += -KPIC -D_FILE_OFFSET_BITS=64 -fast $(SOS12_CC_FLAGS)
LDFLAGS += $(SOS12_LD_FLAGS) $(RUNPATH_LINKER_FLAGS)

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"

BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = custom
CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS   = custom

LD_LIBRARY_PATH=.
export LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

include gar/category.mk

build-custom:
	$(MAKE) -C $(WORKSRC) -f Makefile-libbz2_so $(BUILD_ARGS)
	@$(MAKECOOKIE)

test-custom:
	$(MAKE) -C $(WORKSRC) -f Makefile-libbz2_so test
	@$(MAKECOOKIE)

install-custom:
	@echo " => Installing $(CATALOGNAME)"
	@$(MAKECOOKIE)

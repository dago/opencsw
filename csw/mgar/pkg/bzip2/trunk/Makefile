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

MASTER_SITES = http://www.bzip.org/$(GARVERSION)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)
# TODO: Check if these might be needed
#  CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw
#  CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw

ifneq ($(GARVERSION), 8.4)
TEST_TARGET = check
else
TEST_SCRIPTS =
endif

include gar/category.mk


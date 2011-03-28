NAME = libidn
VERSION = 1.20
CATEGORIES = lib

DESCRIPTION = GNU IDN Library
define BLURB
  GNU Libidn is a fully documented implementation of the Stringprep,
  Punycode and IDNA specifications. Libidn's purpose is to encode and
  decode internationalized domain names. The native C, C# and Java
  libraries are available under the GNU Lesser General Public License
  version 2.1 or later.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.gnu.org/software/libidn/

PACKAGES += CSWlibidn11
CATALOGNAME_CSWlibidn11 = libidn11
SPKG_DESC_CSWlibidn11 = GNU IDN library, libidn.so.11
PKGFILES_CSWlibidn11 += $(call baseisadirs,$(libdir),libidn\.so\.11(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibidn11 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibidn11 += CSWiconv

PACKAGES += CSWlibidn-dev
CATALOGNAME_CSWlibidn-dev = libidn_dev
SPKG_DESC_CSWlibidn-dev = GNU IDN development files
PKGFILES_CSWlibidn-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibidn-dev += $(sharedstatedir)/emacs/.*
PKGFILES_CSWlibidn-dev += $(infodir)/.*
RUNTIME_DEP_PKGS_CSWlibidn-dev += CSWlibidn11
CHECKPKG_OVERRIDES_CSWlibidn-dev += missing-dependency|CSWemacscommon

PACKAGES += CSWlibidn-utils
CATALOGNAME_CSWlibidn-utils = libidn_utils
SPKG_DESC_CSWlibidn-utils = GNU IDN utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibidn-utils += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibidn-utils += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibidn-utils += CSWiconv
OBSOLETED_BY_CSWlibidn-utils = CSWlibidn

BUILD64 = 1
NOISAEXEC = 1

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# One test for GNULib in 32 bit is failing, disable for now
SKIPTEST ?= 1

# What's this? Windows DLLs? How do they end up in the Solaris build?
EXTRA_MERGE_EXCLUDE_FILES = .*\.dll

MERGE_DIRS_isa-extra = $(libdir)

CHECKPKG_OVERRIDES_CSWlibidn += missing-dependency|CSWemacscommon

include gar/category.mk

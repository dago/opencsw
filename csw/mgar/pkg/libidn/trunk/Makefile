NAME = libidn
VERSION = 1.24
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU IDN Library
define BLURB
  GNU Libidn is a fully documented implementation of the Stringprep,
  Punycode and IDNA specifications. Libidn's purpose is to encode and
  decode internationalized domain names. The native C, C# and Java
  libraries are available under the GNU Lesser General Public License
  version 2.1 or later.
endef

MASTER_SITES = $(GNU_MIRROR)
# MASTER_SITES += http://daily.josefsson.org/libidn/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.gnu.org/software/libidn/

PACKAGES += CSWlibidn11
SPKG_DESC_CSWlibidn11 = GNU IDN library, libidn.so.11
PKGFILES_CSWlibidn11 += $(call pkgfiles_lib,libidn.so.11)
PKGFILES_CSWlibidn11 += .*/libidn\.mo
RUNTIME_DEP_PKGS_CSWlibidn11 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibidn11 += CSWlibiconv2

PACKAGES += CSWlibidn-dev
SPKG_DESC_CSWlibidn-dev = GNU IDN development files for libidn.so.11
PKGFILES_CSWlibidn-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibidn-dev += $(sharedstatedir)/emacs/.*
PKGFILES_CSWlibidn-dev += $(infodir)/.*
RUNTIME_DEP_PKGS_CSWlibidn-dev += CSWlibidn11
# This is just a file for the emacs mode
CHECKPKG_OVERRIDES_CSWlibidn-dev += missing-dependency|CSWemacscommon

PACKAGES += CSWlibidn-utils
SPKG_DESC_CSWlibidn-utils = GNU IDN utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibidn-utils += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibidn-utils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibidn-utils += CSWlibiconv2
OBSOLETED_BY_CSWlibidn-utils = CSWlibidn

BUILD_OVERRIDE_VARS = SHELL
BUILD_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash

TEST_OVERRIDE_VARS = SHELL
TEST_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash

INSTALL_OVERRIDE_VARS = SHELL
INSTALL_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash

BUILD64_LIBS_ONLY = 1

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

# What's this? Windows DLLs? How do they end up in the Solaris build?
EXTRA_MERGE_EXCLUDE_FILES = .*\.dll

include gar/category.mk

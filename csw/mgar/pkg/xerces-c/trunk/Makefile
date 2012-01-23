NAME = xerces-c
VERSION = 3.1.1
CATEGORIES = lib

DESCRIPTION = Xerces XML parser for C++
define BLURB
  Xerces-C++ is a validating XML parser written in a portable subset
  of C++. Xerces-C++ makes it easy to give your application the ability
  to read and write XML data. A shared library is provided for parsing,
  generating, manipulating, and validating XML documents using the DOM,
  SAX, and SAX2 APIs. For an introduction to programming with Xerces-C++
 refer to the Programming Guide.
endef

MASTER_SITES = http://apache.abdaal.com/xerces/c/3/sources/
DISTFILES += $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Do-not-strip-norunpath.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibxerces-c3-1
CATALOGNAME_CSWlibxerces-c3-1 = libxerces_c3_1
SPKG_DESC_CSWlibxerces-c3-1 = Xerces XML parser for C++ providing libxerces-c-3.1.so
PKGFILES_CSWlibxerces-c3-1 = $(call baseisadirs,$(libdir),libxerces-c-3\.1\.so)
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWcurlrt
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibidn
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibcares
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWoldaprt
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibicu46

PACKAGES += CSWlibxerces-c-dev
CATALOGNAME_CSWlibxerces-c-dev = libxerces_c_dev
SPKG_DESC_CSWlibxerces-c-dev = Development files for Xerces
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWlibxerces-c3-1
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWcurlrt
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWlibidn
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWzlib
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWlibcares
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWoldaprt

PACKAGES += CSWxerces-c
CATALOGNAME_CSWxerces-c = xerces_c
SPKG_DESC_CSWxerces-c = Utility programs from the Xerces XML parser
PKGFILES_CSWxerces-c = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibxerces-c3-1
RUNTIME_DEP_PKGS_CSWxerces-c += CSWcurlrt
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibidn
RUNTIME_DEP_PKGS_CSWxerces-c += CSWzlib
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibcares
RUNTIME_DEP_PKGS_CSWxerces-c += CSWosslrt
RUNTIME_DEP_PKGS_CSWxerces-c += CSWoldaprt
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibicu46

VENDOR_URL = http://xerces.apache.org/xerces-c/
LICENSE = LICENSE

BUILD64 = 1

icu_config = $(bindir)/icu-config
EXTRA_CONFIGURE_EXPORTS = icu_config

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --with-icu=$(prefix)
# CONFIGURE_ARGS += --with-curl=$(prefix)

include gar/category.mk

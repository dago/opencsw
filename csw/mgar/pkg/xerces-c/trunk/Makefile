NAME = xerces-c
VERSION = 3.1.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Xerces XML parser for C++
define BLURB
  Xerces-C++ is a validating XML parser written in a portable subset
  of C++. Xerces-C++ makes it easy to give your application the ability
  to read and write XML data. A shared library is provided for parsing,
  generating, manipulating, and validating XML documents using the DOM,
  SAX, and SAX2 APIs. For an introduction to programming with Xerces-C++
 refer to the Programming Guide.
endef

MASTER_SITES = http://www.apache.org/dist/xerces/c/3/sources/
DISTFILES += $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Do-not-strip-norunpath.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://xerces.apache.org/xerces-c/

LICENSE = LICENSE

PACKAGES += CSWlibxerces-c3-1
SPKG_DESC_CSWlibxerces-c3-1 = Xerces XML parser for C++ providing libxerces-c-3.1.so
PKGFILES_CSWlibxerces-c3-1 = $(call pkgfiles_lib,libxerces-c-3.1.so)
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibxerces-c3-1 += CSWlibicui18n48

# The version number is in the base and not appended to .so as usual
CHECKPKG_OVERRIDES_CSWlibxerces-c3-1 += soname-equals-filename

PACKAGES += CSWlibxerces-c-dev
SPKG_DESC_CSWlibxerces-c-dev = Development files for libxerces-c-3.1.so
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibxerces-c-dev += CSWlibxerces-c3-1

PACKAGES += CSWxerces-c
CATALOGNAME_CSWxerces-c = xerces_c
SPKG_DESC_CSWxerces-c = Utility programs from the Xerces XML parser
PKGFILES_CSWxerces-c = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibxerces-c3-1
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibz1
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibidn11
RUNTIME_DEP_PKGS_CSWxerces-c += CSWlibicui18n48

BUILD64 = 1
ISAEXEC = 1

EXTRA_CONFIGURE_EXPORTS = icu_config
EXTRA_CONFIGURE_ENV_icu_config = $(bindir)/icu-config

include gar/category.mk

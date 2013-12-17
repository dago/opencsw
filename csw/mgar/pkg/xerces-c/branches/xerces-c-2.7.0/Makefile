NAME = xerces-c
VERSION = 2_7_0
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

MASTEarchive.apache.org/dist/xml/xerces-c/source/
DISTNAME = $(NAME)-src_$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

 solaris10-i386

VENDOR_URL = http://xerces.apache.org/xerces-c/

LICENSE = LICENSE

PACKAGES 27
SPKG_DESC_CSWlibxerces-c27 = Xerces XML parser for C++ providing libxerces-c.so.27
PKGFILES_CSWlibxerces-c27 = $(call pkgfiles_lib,libxerces-c.so.27)

PACKAGES += CSWlibxerces-depdom27
SPKG_DESC_CSWlibxerces-depdom27 = Xerces XML parser for C++ providing libxerces-depdom.so.27
PKGFILES_CSWlibxerces-depdom27 = $(call pkgfiles_lib,libxerces-depdom.so.27)

PACKAGES += CSWlibxerces-c27-dev
SPKG_DESC_CSWlibxerces-c27-dev = Development files for libxerces-c.so.27
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibxerces-c27-dev += CSWlibxerces-c27
CHECKPKG_OVERRIDES_CSWlibxerces-c27-dev += surplus-dependency|CSWlibxerces-c27
RUNTIME_DEP_PKGS_CSWlibxerces-c27-dev += CSWlibxerces-depdom27
CHECKPKG_OVERRIDES_CSWlibxerces-c27-dev += surplus-dependency|CSWlibxerces-depdom27

WORKSRC = $(WORKDIR)/$(DISTNAME)/src/xercesc

EXTRA_LINKER_FLAGS += -norunpath

EXTRA_BUILD_EXPORTS += XERCESCROOT
BUILD_ENV_XERCESCROOT = $(abspath $(WORKDIR)/$(DISTNAME))

EXTRA_INSTALL_EXPORTS += XERCESCROOT
INSTALL_ENV_XERCESCROOT = $(abspath $(WORKDIR)/$(DISTNAME))

# Arguments are not passed in the default Makefile
EXTRA_INSTALL_EXPORTS += MAKE
INSTALL_ENV_MAKE = gmake DESTDIR=$(DESTDIR)

# There is no testsuite
TEST_SCRIPTS =

EXTRA_PAX_ARGS += -s ',/include/,/include/xercesc-2.7.0/,'
EXTRA_PAX_ARGS += -s ',/lib/(.*\.so)$$,/lib/xercesc-2.7.0/$$1,'

include gar/category.mk

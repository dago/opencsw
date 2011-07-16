NAME = xapian-core
VERSION = 1.2.6
CATEGORIES = lib

DESCRIPTION = An open source search engine library
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xapian/$(VERSION)/

DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Fix-include-issue-on-Solaris-9.patch
PATCHFILES += 0002-Do-not-strip-norunpath-on-libtool.patch

VENDOR_URL = http://xapian.org/

PACKAGES += CSWxapian
CATALOGNAME_CSWxapian = xapian
SPKG_DESC_CSWxapian = Xapian search engine binaries
RUNTIME_DEP_PKGS_CSWxapian += CSWlibxapian22
RUNTIME_DEP_PKGS_CSWxapian += CSWstlport
RUNTIME_DEP_PKGS_CSWxapian += CSWzlib

PACKAGES += CSWlibxapian22
SPKG_DESC_CSWlibxapian22 = An open source search engine library, libxapian.so.22
PKGFILES_CSWlibxapian22 = $(call pkgfiles_lib,libxapian.so.22)
RUNTIME_DEP_PKGS_CSWlibxapian22 += CSWstlport
RUNTIME_DEP_PKGS_CSWlibxapian22 += CSWzlib

PACKAGES += CSWlibxapian-dev
SPKG_DESC_CSWlibxapian-dev = Xapian development files for libxapian.so.22
PKGFILES_CSWlibxapian-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxapian-dev += $(docdir)/xapian-core/apidoc/.*
PKGFILES_CSWlibxapian-dev += .*\.cmake
RUNTIME_DEP_PKGS_CSWlibxapian-dev += CSWlibxapian22

EXTRA_LD_FLAGS = -norunpath -lCrun

BUILD64 = 1
ISAEXEC = 1

# This is just an example of the default install location
CHECKPKG_OVERRIDES_CSWxapian += file-with-bad-content|/usr/local|root/opt/csw/share/doc/xapian-core/install.html

include gar/category.mk

NAME = xapian-core
VERSION = 1.3.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = An open source search engine library
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xaDISTFILES += $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0002-Do-not-strip-norunpath-on-libtool.patch

# This is strange and needs further examination
PATCHFILES += 0002-Somehow-round-is-missing-in-cmath.patch

# Use patch until this is fixed:
#   http://trac.xapian.org/ticket/627
PATCHFILES += 0003-log-is-ambigous-to-float-and-double.patch
mPATCHFILES += 0001-Force-float-to-disambiguise-float-double-invocation-.patch

ssing-.la.patch

VENDOR_URL = http://xapian.org/

PACKAGES += CSWxapian
SPKG_DESC_CSWxapian = Xapian search engine binaries
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWxapia1-3-1
RUNTIME_DEP_PKGS_CSWxapian += CSWlibstlport1

PACKAGES += CSWlibxapian1-3-1
SPKG_DESC_CSWlibxapian1-3-1 = An open source search engine library, libxapian-1.3.so.1
PKGFILES_CSWlibxapian1-3-1 = $(call pkgfiles_lib,libxapian-1.3.so.1)
RUNTIME_DEP_PKGS_CSWlibxapian1-3-1 += CSWlibstlport1
RUNTIME_DEP_PKGS_CSWlibxapian1-3-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibxapian1-3-1 += CSWlibuuidpian22 += CSWlibz1

PACKAGES += CSWlibxapian-dev
SPKG_DESC_CSWlibxapian-dev = Xapian development fi-1.3.so.1r libxapian.so.22
PKGFILES_CSWlibxapian-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxapian-dev += $(docdir)/xapian-core/apidoc/.*
PKGFILES_CSWlibxapian-dev += .*\.cmake
RUNTIME_DEP_PKGS_CSWlibxapian-de1-3-1

EXTRA_LD_FLAGS += -norunpath

# libuuid.so must be searched in /opt/csw/lib
EXTRA_CXXFLAGS += -L$(libdir)-norunpath -lCrun

BUILD64 = 1
ISAEXEC = 1

# This is just an example of the default install location
CHECKPKG_OVERRIDES_CSWxapian += file-with-bad-content|/usr/local|root/opt/csw/share/doc/xapian-core/install.html

include
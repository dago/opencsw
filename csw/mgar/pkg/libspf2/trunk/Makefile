NAME = libspf2
VERSION = 1.2.9
CATEGORIES = lib

DESCRIPTION = Library that implements Sender Policy Framework
define BLURB
  libspf2 implements the Sender Policy Framework, a part of the SPF/SRS protocol pair.
  libspf2 is a library which allows email systems such as Sendmail, Postfix, Exim,
  Zmailer and MS Exchange to check SPF records and make sure that the email is authorized
  by the domain name that it is coming from. This prevents email forgery, commonly used
  by spammers, scammers and email viruses/worms.
endef

MASTER_SITES = http://www.libspf2.org/spf/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.libspf2.org

LICENSE = LICENSES

PACKAGES += CSWlibspf2-2
SPKG_DESC_CSWlibspf2-2 = Library that implements Sender Policy Framework, libspf2.so.2
PKGFILES_CSWlibspf2-2 = $(call pkgfiles_lib,libspf2.so.2)
RUNTIME_DEP_PKGS_CSWlibspf2-2 += CSWlibintl8
OBSOLETED_BY_CSWlibspf2-2 = CSWlibspf2

PACKAGES += CSWlibspf2-utils
SPKG_DESC_CSWlibspf2-utils = Utility programs to query SPF
PKGFILES_CSWlibspf2-utils = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWlibspf2-utils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibspf2-utils += CSWlibspf2-2
OBSOLETED_BY_CSWlibspf2-utils = CSWlibspf2

PACKAGES += CSWlibspf2-dev
SPKG_DESC_CSWlibspf2-dev = Development files for libspf2.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibspf2-dev = CSWlibspf2-2

BUILD64 = 1

EXTRA_LINKER_FLAGS = -lresolv  -lsocket  -lnsl 

# These are the same as the ones without '_static', but linked statically
# against libspf2.a
# I guess nobody needs that as we always depend on the library package anyway
EXTRA_MERGE_EXCLUDE_FILES = $(bindir)/.*_static

include gar/category.mk

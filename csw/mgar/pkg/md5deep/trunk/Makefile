# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = md5deep
VERSION = 4.3
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Compute MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digests
define BLURB
  A set of programs to compute MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digests on an arbitrary number of files
endef

MASTER_SITES = $(SF_+= $(DISTNAME).tar.gz
DISTFILES += bootstrap.sh

# Use patch until pull request has been merged:
#   https://github.com/jessek/hashdeep/pull/291
PATCHFILES += 0001-Use-MAP_FILE-only-when-available.patch

PACKAGES += CSWmd5deep
SPKG_DESC_CSWmd5deep = Compute MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digests
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWmd5deep += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWmd5deep += CSWlibstdc++6
# Yes, we need vasprintf from 1.22.7
CHECKPKG_OVERRIDES_CSWmd5deep += forbidden-version-interface-dependencies

GARCOMPILER = GNU

BUILD64 = 1
ISAEXEC = 1

# We need vasprintf from a newer release than the frozen one
LINKER_MAPS =

# The testsuite seems broken, skip for now
SKIPTEST ?= 1

include gar/category.mk

pre-configure:
	cp $(WORKDIR)/bootstrap.sh $(WORKSRC)
	cd $(WORKSRC) && sh bootstrap.sh
	@$(MAKECOOKIE)

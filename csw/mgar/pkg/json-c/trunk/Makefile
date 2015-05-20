# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = json-c
VERSION = 0.12
GARTYPE = v2

DESCRIPTION = JSON objects in C
define BLURB
  JSON-C implements a reference counting object model that allows you to easily construct JSON
  objects in C, output them as JSON formatted strings and parse JSON formatted strings back
  into the C representation of JSON objects.
endef

MASTER_SITES += https://s3.amazonaws.com/json-c_releases/releases/
#DISTFILES += $(DISTNAME).tar.gz
DISTNAME = json-c-solaris
DISTFILES += $(DISTNAME)-branch.zip

# PATCHFILES = 0001-allow-to-use-public-vasprintf-symbol.patch

# Use these patches until this is merged:
#   https://github.com/json-c/json-c/pull/184
#PATCHFILES += 0001-Solaris-does-not-allow-POSIX-compliant-evaluation-in.patch
#PATCHFILES += 0002-Use-GCC-flags-only-when-compiling-with-GCC.patch

PACKAGES += CSWlibjson-c3
PKGFILES_CSWlibjson-c3 += $(call pkgfiles_lib,libjson-c.so.3)
SPKG_DESC_CSWlibjson-c3 += $(DESCRIPTION), libjson-c.so.3

PACKAGES += CSWjson-c-dev
SPKG_DESC_CSWjson-c-dev += $(DESCRIPTION), development files
# PKGFILES_CSWjson-c-dev += $(PKGFILES_DEVEL)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWjson-c-dev += CSWlibjson-c3

BUILD64 = 1

include gar/category.mk

post-patch:
	cd $(WORKSRC) && ./autogen.sh
	@$(MAKECOOKIE)

NAME    = libotr
VERSION = 4.0.0
GARTYPE = v2

DESCRIPTION = Off-The-Record Messaging plugin for pidgin
define BLURB
  Off-the-Record (OTR) Messaging allows you to have private conversations over instant messaging.
endef

MASTER_SITES = http://www.cypherpunks.ca/otr/
DISTFILES = $(DISTNAME).tar.gz

PACKAGES += CSWlibotr5
CATALOGNAME_CSWlibotr5 = libotr5
SPKG_DESC_CSWlibotr5  += $(DESCRIPTION), libotr.so.5
PKGFILES_CSWlibotr5 += $(call baseisadirs,$(libdir),libotr\.so\.5\.0\.0)
PKGFILES_CSWlibotr5 += $(call baseisadirs,$(libdir),libotr\.so\.5(\.\d+)*)

PACKAGES += CSWotr-dev
CATALOGNAME_CSWotr-dev = otr_dev
SPKG_DESC_CSWotr-dev += $(DESCRIPTION), development files
PKGFILES_CSWotr-dev += $(PKGFILES_DEVEL)

OBSOLETED_BY_CSWotr-dev += CSWotrdevel

PACKAGES += CSWotr
CATALOGNAME_CSWotr = otr
SPKG_DESC_CSWotr  += $(DESCRIPTION), utilities
# PKGFILES is catchall

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

BUILD64_LIBS_ONLY = 1

RUNTIME_DEP_PKGS_CSWlibotr5 += CSWlibgcrypt11

RUNTIME_DEP_PKGS_CSWotr-dev += CSWlibotr5

RUNTIME_DEP_PKGS_CSWotr += CSWlibotr2
RUNTIME_DEP_PKGS_CSWotr += CSWlibotr5
RUNTIME_DEP_PKGS_CSWotr += CSWlibgcrypt11

# On sparc, the dependencies end up different
ifeq ($(shell uname -p), sparc)
  RUNTIME_DEP_PKGS_CSWlibotr5 += CSWlibgpg-error0
  RUNTIME_DEP_PKGS_CSWotr += CSWlibgpg-error0
endif

CHECKPKG_OVERRIDES_CSWotr += surplus-dependency|CSWlibotr2

BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev

# Remove after pushing to catalog
CHECKPKG_OVERRIDES_CSWotr += dependency-on-nonexistent-package|CSWlibotr2

include gar/category.mk

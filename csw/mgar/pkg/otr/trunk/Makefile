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
SPKG_DESC_CSWotr-dev  += $(DESCRIPTION), development files
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

RUNTIME_DEP_PKGS_CSWotr += CSWlibotr5
RUNTIME_DEP_PKGS_CSWotr += CSWlibgcrypt11

# Don't know yet why but this dependency is only picked under sparc
RUNTIME_DEP_PKGS_CSWlibotr5_sparc = CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibotr5 += $(RUNTIME_DEP_PKGS_CSWlibotr5_$(GARCH))
RUNTIME_DEP_PKGS_CSWotr_sparc = CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWotr += $(RUNTIME_DEP_PKGS_CSWotr_$(GARCH))

BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev

include gar/category.mk

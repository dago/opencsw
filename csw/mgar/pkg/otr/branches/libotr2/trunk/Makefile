NAME    = libotr
VERSION = 3.2.1
GARTYPE = v2

DESCRIPTION = Off-The-Record Messaging plugin for pidgin
define BLURB
  Off-the-Record (OTR) Messaging allows you to have private conversations over instant messaging.
endef

MASTER_SITES = http://www.cypherpunks.ca/otr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += heartbeat.patch

PACKAGES += CSWlibotr2
CATALOGNAME_CSWlibotr2 = libotr2
PKGFILES_CSWlibotr2 += $(call baseisadirs,$(libdir),libotr\.so\.2\.2\.1)
PKGFILES_CSWlibotr2 += $(call baseisadirs,$(libdir),libotr\.so\.2(\.\d+)*)
PKGFILES_CSWlibotr2 += $(bindir)/.*
PKGFILES_CSWlibotr2 += $(sharedir)/man/.*
SPKG_DESC_CSWlibotr2 += $(DESCRIPTION), libotr.so.5

OBSOLETED_BY_CSWlibotr2 += CSWotr

PACKAGES += CSWotr-dev
CATALOGNAME_CSWotr-dev = otr_dev
SPKG_DESC_CSWotr-dev += $(DESCRIPTION), development files
# PKGFILES is catchall

OBSOLETED_BY_CSWotr-dev += CSWotrdevel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

BUILD64_LIBS_ONLY = 1

RUNTIME_DEP_PKGS_CSWlibotr2 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibotr2 += CSWlibgpg-error0

RUNTIME_DEP_PKGS_CSWotr-dev += CSWlibotr2

BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev

include gar/category.mk

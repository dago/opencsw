NAME    = pidgin-otr
VERSION = 4.0.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Off-The-Record Messaging plugin for pidgin
define BLURB
  Off-the-Record (OTR) Messaging allows you to have private conversations over instant messaging.
endef

MASTER_SITES = http://www.cypherpunks.ca/otNAME)-$(VERSION).tar.gz
#PATCHFILES = otr_priority.patch

PACKAGES                 = CSWpidginotr
CATALOGNAME_CSWpidginotr = pidginotr
SPKG_DESC_CSWpidginotr   = Off-The-Record messaging for Pidgin(?:\For msgfmt, msgmerge, xgettext and gettext to be used from GNU
CONFIGURE_ENV_PATH = $(prefix)/gnu:$(PATH)(?CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWpidginotr += CSWlibotr5
RUNTIME_DEP_PKGS_CSWpidginotr += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWpidginotr += CSWpidgin

# On sparc, the dependencies end up different
ifeq ($(shell uname -p), sparc)
  RUNTIME_DEP_PKGS_CSWpidginotr += CSWlibgpg-error0
endif

CHECKPKG_OVERRIDES_CSWpidginotr += surplus-dependency|CSWpidgin

BUILD_DEP_PKGS += CSWotr-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev


include gar/category.mk

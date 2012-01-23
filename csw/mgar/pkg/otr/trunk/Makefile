NAME = libotr
VERSION = 3.2.0
CATEGORIES = lib

DESCRIPTION = Off-The-Record Messaging plugin for pidgin
define BLURB
  Off-the-Record (OTR) Messaging allows you to have private conversations over instant messaging.
endef

PACKAGES = CSWotr CSWotrdevel

MASTER_SITES = http://www.cypherpunks.ca/otr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = heartbeat.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64_LIBS_ONLY = 1

MERGE_EXCLUDE_FILES = /opt/csw/bin/$(ISA)/.*

RUNTIME_DEP_PKGS_CSWotr = CSWgcrypt CSWgpgerr
RUNTIME_DEP_PKGS_CSWotrdevel = CSWotr

PKGFILES_CSWotrdevel = $(PKGFILES_DEVEL)

include gar/category.mk

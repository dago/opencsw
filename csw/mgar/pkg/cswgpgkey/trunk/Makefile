# $Id$
NAME = cswpki
VERSION = 1.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = The OpenCSW PKI Collection
define BLURB
  A collection of any public keys used by OpenCSW.
endef

MASTER_SITES = http://www.opencsw.org/
DISTFILES  = CSWcswpki.postinstall gpl-2.0.txt
DISTFILES += cswpki
DISTFILES += csw_legacy_catalog_verification.asc
DISTFILES += csw_catalog_signing_2011-09.asc

RUNTIME_DEP_PKGS = CSWgnupg

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWcswpki += surplus-dependency|CSWgnupg

PROTOTYPE_MODIFIERS = var_pki_perms
PROTOTYPE_FILES_var_pki_perms = /var/opt/csw/.*
PROTOTYPE_PERMS_var_pki_perms = 0700

include gar/category.mk

install-custom: PKIDIR=$(DESTDIR)/etc/opt/csw/pki/
install-custom: DOC=$(DESTDIR)/$(docdir)/$(NAME)/
install-custom: BIN=$(DESTDIR)/$(bindir)/
install-custom: VAR=$(DESTDIR)/var/opt/csw/pki
install-custom:
	( mkdir -p $(PKIDIR) $(DOC) $(BIN) $(VAR); \
		for f in $(filter %.asc,$(DISTFILES)); do \
			cp $(WORKDIR)/$$f $(PKIDIR); \
		done; \
		cp $(WORKDIR)/cswpki $(BIN); \
		cp $(WORKDIR)/gpl-2.0.txt $(DOC)/license; \
		chmod 700 $(VAR) )
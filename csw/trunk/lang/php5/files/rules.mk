
INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

PHP5ROOT    = $(DESTDIR)$(prefix)/php5
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin

# Build the imap client library first
pre-configure:
	( cd $(WORKDIR)/$(IMAPVERSION) ; $(BUILD_ENV) make soc )
	@$(MAKECOOKIE)

# This is required so that we don't try to regen the
# sqlite parser.
#pre-build:
#	@touch $(WORKSRC)/ext/sqlite/libsqlite/src/parse.c
#	@$(MAKECOOKIE)


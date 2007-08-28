
INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

PHP5ROOT    = $(DESTDIR)$(prefix)/php5
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin


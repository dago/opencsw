#
# funcion Definitions and mGar Extra Scripts
#

define _get_php_config
$(abspath $(shell gfind $(1) -name php-config -print))
endef

define _get_php_prefix
$(shell $(call _get_php_config,$(1)) --prefix)
endef

define _get_php_ini_path
$(shell $(call _get_php_prefix,$(1))/bin/php -i | grep "Configuration File .* Path" | gawk '{print $$NF}')
endef

PI_SCRIPTS  = install-extras
PI_SCRIPTS += install-cleanup

post-install-modulated: $(PI_SCRIPTS)
	@$(MAKECOOKIE)

install-extras:
	@echo "[====> Fixing Admin Scripts <====]"
	gcp $(DOWNLOADDIR)/php.ini.CSW $(DOWNLOADDIR)/php.ini.CSW.fixed
	perl -i -pne "s|x_PHPEXTDIR_x|_PHPEXTDIR_|" $(DOWNLOADDIR)/php.ini.CSW.fixed
	perl -i -pne "s|_PHPINIFILE_|$(call _get_php_ini_path,$(DESTDIR))/php.ini|" `gfind $(DOWNLOADDIR) -type f -print`
	perl -i -pne "s|_PHPLIBDIR_|$(call _get_php_ini_path,$(DESTDIR))|" `gfind $(DOWNLOADDIR) -type f -print`
	perl -i -pne "s|_PHPBINDIR_|$(call _get_php_prefix,$(DESTDIR))/bin|" `gfind $(DOWNLOADDIR) -type f -print`
	perl -i -pne "s|_PHPETCDIR_|$(call _get_php_prefix,$(DESTDIR))/etc|" `gfind $(DOWNLOADDIR) -type f -print`
	perl -i -pne 's|_PHPEXTDIR_|$(shell $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/bin/php-config --extension-dir)|' `gfind $(DOWNLOADDIR) -type f -print`
	@echo "[====> Installing Extra Files <====]"
	ginstall -m 0755 $(DOWNLOADDIR)/phpext $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/bin
	gcp $(DOWNLOADDIR)/php.ini.CSW.fixed $(DESTDIR)$(call _get_php_ini_path,$(DESTDIR))/php.ini.CSW
	gmv $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/etc/pear.conf $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/etc/pear.conf.CSW
	gchmod 0644 $(DESTDIR)$(call _get_php_ini_path,$(DESTDIR))/php.ini.CSW
	@$(MAKECOOKIE)

install-cleanup:
	@echo "[====> Cleaning Up Extra Install Files <====]"
	gfind $(DESTDIR) -name \.[a-z]\* -print |xargs grm -fr
	gfind $(DESTDIR)$(prefix)/apache* -mindepth 1 -type d | egrep -v "etc|libexec" | xargs grm -fr
	$(GARBIN)/stripbin $(DESTDIR)$(shell $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/bin/php-config --extension-dir)
	$(GARBIN)/stripbin $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/bin
	$(MAKECOOKIE)

EXTFILES = $(shell find extensions/*/files/* -prune -type f)
pre-fetch:
	$(foreach F,$(EXTFILES),$(shell cp $(F) $(DOWNLOADDIR)))


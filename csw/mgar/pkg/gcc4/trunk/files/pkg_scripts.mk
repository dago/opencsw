
post-patch-modulated:
	@(echo "==> Running autoheader and autoconf")
	@(cd $(PATCHDIR)/gcc && autoheader)
	@(cd $(PATCHDIR)/gcc && autoconf)
	@$(MAKECOOKIE)

## Create $(OBJECT_DIR) to build in
post-extract-$(addprefix post-extract-,$(MODULATIONS)):
	@(echo "==> Creating Object Dir for Building")
	@( mkdir $(OBJECT_DIR) )
	$(MAKECOOKIE)

## instead of changing to $(WORKSRC) and running configure
## Run it from the $(OBJECT_DIR)
configure-objdir:
	echo "==> Running Configure from $(OBJECT_DIR)"
	cd $(OBJECT_DIR) && $(CONFIGURE_ENV) \
		../$(DISTNAME)/configure $(CONFIGURE_ARGS)
	$(MAKECOOKIE)

## Set the CFLAGS so the correct architecture is used
fix-bootflags:
	@(perl -i -plne "s|^BOOT_CFLAGS.*|BOOT_CFLAGS= $(BOOT_CFLAGS)|" \
		$(WORKSRC)/Makefile)
	@(perl -i -plne "s|^BOOT_LDFLAGS.*|BOOT_LDFLAGS= $(BOOT_LDFLAGS)|" \
		$(WORKSRC)/Makefile)
	@$(MAKECOOKIE)

test-skip:
	@$(MAKECOOKIE)


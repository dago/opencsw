
## Create lib links to conform to multi-arch standards
post-merge-isa-sparcv8:
	@(cd $(PKGROOT)/opt/csw/gcc4/lib && ln -s sparcv9 64)
	@(cd $(PKGROOT)/opt/csw/gcc4/lib && ln -s . 32)
	@(cd $(PKGROOT)/opt/csw/gcc4/lib && ln -s . sparcv8)
	@$(MAKECOOKIE)

post-merge-isa-i386:
	@(cd $(PKGROOT)/opt/csw/gcc4/lib && ln -s amd64 64)
	@(cd $(PKGROOT)/opt/csw/gcc4/lib && ln -s . 32)
	@(cd $(PKGROOT)/opt/csw/gcc4/lib && ln -s . i386)
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


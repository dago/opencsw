
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

post-merge-modulated:
	@( gecho "[===> Creating Runtime Package files <===]" )
	@( ginstall -d $(PKGROOT)/opt/csw/lib )
	@( gcp -d $(PKGROOT)/opt/csw/gcc4/lib/*.so* $(PKGROOT)/opt/csw/lib/ )
	@( gchmod 0755 $(PKGROOT)/opt/csw/lib/*.so* )
	@( gcp -d $(PKGROOT)/opt/csw/gcc4/lib/gcc/*/*/adalib/*.so* \
		$(PKGROOT)/opt/csw/lib/ )
	@( if [ "`uname -p`" = 'i386' ]; then \
	    if [ "`uname -r`" = '5.10' ]; then \
			ginstall -d $(PKGROOT)/opt/csw/lib/amd64; \
			gcp -d $(PKGROOT)/opt/csw/gcc4/lib/amd64/*.so* \
					$(PKGROOT)/opt/csw/lib/amd64/; \
			gchmod 0755 $(PKGROOT)/opt/csw/lib/amd64/*.so*; \
		fi; \
	fi ) 
	@( if [ "`uname -p`" = 'sparc' ]; then \
		ginstall -d $(PKGROOT)/opt/csw/lib/sparcv9; \
		gcp -d $(PKGROOT)/opt/csw/gcc4/lib/sparcv9/*.so* \
				$(PKGROOT)/opt/csw/lib/sparcv9/; \
		gchmod 0755 $(PKGROOT)/opt/csw/lib/sparcv9/*.so*; \
	fi )
	@$(MAKECOOKIE)

test-skip:
	@$(MAKECOOKIE)


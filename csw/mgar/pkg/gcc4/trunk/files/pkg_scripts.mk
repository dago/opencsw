ifeq ($(PKG_DEBUG),)
	_DBG=@
else
	_DBG=
endif


## Create $(OBJECT_DIR) to build in
post-extract-$(addprefix post-extract-,$(MODULATIONS)):
	$(_DBG)(echo "==> Creating Object Dir for Building")
	$(_DBG)(mkdir $(OBJECT_DIR))
	$(_DBG)$(MAKECOOKIE)

## instead of changing to $(WORKSRC) and running configure
## Run it from the $(OBJECT_DIR)
configure-objdir:
	$(_DBG)(echo "==> Running Configure from $(OBJECT_DIR)")
	$(_DBG)(cd $(OBJECT_DIR) && $(CONFIGURE_ENV) \
		../$(DISTNAME)/configure $(CONFIGURE_ARGS))
	$(_DBG)$(MAKECOOKIE)

## Set the CFLAGS so the correct architecture is used
fix-bootflags:
	$(_DBG)(perl -i -plne "s|^BOOT_CFLAGS.*|BOOT_CFLAGS= $(BOOT_CFLAGS)|" \
		$(WORKSRC)/Makefile)
	$(_DBG)(perl -i -plne "s|^BOOT_LDFLAGS.*|BOOT_LDFLAGS= $(BOOT_LDFLAGS)|" \
		$(WORKSRC)/Makefile)
	$(_DBG)$(MAKECOOKIE)

post-merge-modulated:
	$(_DBG)( gmv $(PKGROOT)/opt/csw/gcc4/lib/gcc/*/*/adalib/*.so* \
			$(PKGROOT)/opt/csw/gcc4/lib/ )
	$(_DBG)$(MAKECOOKIE)

test-skip:
	$(_DBG)$(MAKECOOKIE)


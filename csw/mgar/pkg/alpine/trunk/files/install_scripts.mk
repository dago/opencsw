PI_SCRIPTS  = cleanup-web
PI_SCRIPTS += install-mlock
PI_SCRIPTS += install-web

post-install-modulated: $(PI_SCRIPTS)


install-mlock:
	@(echo "==> Installing mlock")
	(ginstall -d $(DESTDIR)$(sbindir))
	@(gcp $(WORKSRC)/imap/mlock/mlock $(DESTDIR)$(sbindir))
	@$(MAKECOOKIE)

cleanup-web:
	@(grm -fr $(DESTDIR)/home)

install-web:
	@(echo "==> Installing Web Interface")
	@(ginstall -d $(DESTDIR)$(libexecdir)/alpine-2.00)
	@(gcp -R $(WORKSRC)/web/* $(DESTDIR)$(libexecdir)/alpine-2.00)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_gssapi_proxy \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_tclsh \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_uidmapper \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/wp_umc \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(gcp $(WORKSRC)/web/src/pubcookie/debug.cgi \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin)
	@(grm -fr $(DESTDIR)$(libexecdir)/alpine-2.00/src)
	@(grm -f $(DESTDIR)$(libexecdir)/alpine-2.00/bin/tclsh)
	@(gln -s $(bindir)/tclsh  \
		$(DESTDIR)$(libexecdir)/alpine-2.00/bin/tclsh)
	@(cd $(DESTDIR)$(libexecdir); gln -s ./alpine-2.00 ./alpine)




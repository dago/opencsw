pre-configure-modulated: install-layout install-dbd-drivers apu-make-configure

install-layout:
	@gsed -e s,INSTALL_PREFIX,$(prefix)/apache2,g \
		$(WORKDIR)/config.layout > $(WORKDIR)/$(GARNAME)-$(GARVERSION)/config.layout
	@$(MAKECOOKIE)

install-dbd-drivers:
	@$(MAKECOOKIE)
#	@gcp -v $(FILEDIR)/apr_dbd_mysql.c $(WORKSRC)/srclib/apr-util/dbd

apu-make-configure:
	@( cd $(WORKDIR)/$(GARNAME)-$(GARVERSION)/srclib/apr-util ; autoconf )
	@$(MAKECOOKIE)


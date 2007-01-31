pre-configure: install-config-layout apu-make-configure

install-config-layout:
	@sed -e s,INSTALL_PREFIX,$(prefix)/apache2,g \
		$(WORKDIR)/config.layout > $(WORKSRC)/config.layout
	@$(MAKECOOKIE)

apu-make-configure:
	@( cd $(WORKSRC)/srclib/apr-util ; autoconf )
	@$(MAKECOOKIE)


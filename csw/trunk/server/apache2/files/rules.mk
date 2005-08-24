pre-configure:
	@sed -e s,INSTALL_PREFIX,$(prefix)/apache2,g \
		$(WORKDIR)/config.layout > $(WORKSRC)/config.layout
	@$(MAKECOOKIE)

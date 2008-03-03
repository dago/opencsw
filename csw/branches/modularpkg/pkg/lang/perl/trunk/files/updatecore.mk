# Rules for updating modules in the Perl core

# Install core updates
install-core-updates: remove-obsolete-modules
	@for d in "" $(CORE_UPDATES) ; do \
		test -z "$$d" && continue ; \
		echo " ==> Applying core update: $$d" ; \
		( cd $(WORKDIR)/$$d ; \
		$(CONFIGURE_ENV) perl Makefile.PL ; \
		$(BUILD_ENV) make ; \
		$(TEST_ENV) make test ; \
		$(INSTALL_ENV) make install INSTALLDIRS=perl DESTDIR=$(DESTDIR) ) ; \
	done
	@$(MAKECOOKIE)

# Remove obsolete modules
remove-obsolete-modules:
	@echo " ==> Removing obsolete modules"
	@( cd $(DESTDIR)$(datadir)/perl/$(GARVERSION) ; \
		grm -vrf $(CORE_OBSOLETE) )
	@$(MAKECOOKIE)


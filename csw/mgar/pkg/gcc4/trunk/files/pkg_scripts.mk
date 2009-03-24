

#pre-fetch:
	#@(echo "==> Creating Prototype Files from prototype-$(GARCH) files")
	#@(cd $(FILEDIR) && for file in `ls *-$(GARCH)`; do \
            #nfile=`echo $$file | gsed 's/-$(GARCH)//'`; \
            #gcp $$file $$nfile; \
        #done)
	#$(DONADA)

#post-checksum:
	#@(cd $(FILEDIR) && grm *.prototype)
	#$(DONADA)

## Create $(OBJECT_DIR) to build in
post-extract-$(addprefix post-extract-,$(MODULATIONS)):
	@(echo "==> Creating Object Dir for Building")
	@( mkdir $(OBJECT_DIR) )
	#@(gcp $(WORKDIR)/$(GARNAME)-$(GARVERSION)/COPYING $(OBJECT_DIR))
	$(DONADA)

## instead of changing to $(WORKSRC) and running configure
## Run it from the $(OBJECT_DIR)
configure-objdir:
	echo "==> Running Configure from $(OBJECT_DIR)"
	cd $(OBJECT_DIR) && $(CONFIGURE_ENV) \
		../$(DISTNAME)/configure $(CONFIGURE_ARGS)
	$(DONADA)

## Set the CFLAGS so the correct architecture is used
fix-bootflags:
	@(perl -i -plne "s|^BOOT_CFLAGS.*|BOOT_CFLAGS= $(BOOT_CFLAGS)|" \
		$(WORKSRC)/Makefile)
	@(perl -i -plne "s|^BOOT_LDFLAGS.*|BOOT_LDFLAGS= $(BOOT_LDFLAGS)|" \
		$(WORKSRC)/Makefile)
	@$(DONADA)

test-skip:
	@$(DONADA)


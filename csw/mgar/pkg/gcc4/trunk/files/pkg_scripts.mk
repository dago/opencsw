
## Create $(OBJECT_DIR) to build in
post-extract-$(addprefix post-extract-,$(MODULATIONS)):
	echo "==> Creating Object Dir for Building"
	@( mkdir $(OBJECT_DIR) )
	$(DONADA)

## instead of changing to $(WORKSRC) and running configure
## Run it from the $(OBJECT_DIR)
configure-objdir:
	echo "==> Running Configure from $(OBJECT_DIR)"
	cd $(OBJECT_DIR) && $(CONFIGURE_ENV) ../configure $(CONFIGURE_ARGS)
	$(DONADA)

test-skip:
	$(DONADA)


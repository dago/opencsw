GARNAME = x11common
GARVERSION = 1.0
CATEGORIES = x11

DESCRIPTION = X11 common directories
define BLURB
endef

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	gln -s . $(DESTDIR)$(libdir)/32
	mkdir -p $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)
	gln -s $(ISA_DEFAULT64) $(DESTDIR)$(libdir)/64
	@$(MAKECOOKIE)

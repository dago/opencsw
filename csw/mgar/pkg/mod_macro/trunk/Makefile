GARNAME = mod_macro
GARVERSION = 1.1.10
CATEGORIES = lib

DESCRIPTION = Create macros inside apache2 config files 
define BLURB
  Long description
endef

MASTER_SITES = http://cri.ensmp.fr/~coelho/mod_macro/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES  += CSWap2modmacro.postinstall CSWap2modmacro.preremove
LICENSE = LICENSE

PACKAGES = CSWap2modmacro
CATALOGNAME = ap2_modmacro
REQUIRED_PKGS = CSWap2prefork

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk
include ../../apache2/trunk/files/extensionbuild.mk

build-custom:
	$(APXS2_BUILD) $(WORKSRC)/mod_macro.c
	@$(MAKECOOKIE)

# Ideally, we could use 
# 
#	$(APXS2_INSTALL) $(WORKSRC)/mod_macro.c
#
# but this tries to just copy mod_macro.c instead of mod_macro.so
install-custom: DOCDEST = $(DESTDIR)$(docdir)/$(CATALOGNAME)
install-custom: EXTRA_DOCS = CHANGES mod_macro.html
install-custom:
	ginstall -d $(DOCDEST)
	ginstall -D $(WORKSRC)/.libs/mod_macro.so $(AP2_LIBEXEC)/mod_macro.so
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(WORKSRC)/CHANGES $(DOCDEST)/changelog
	cp $(WORKSRC)/mod_macro.html $(DOCDEST)
	@$(MAKECOOKIE)

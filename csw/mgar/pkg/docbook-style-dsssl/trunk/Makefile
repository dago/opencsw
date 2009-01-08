GARNAME = docbookdsssl
GARVERSION = 1.79
PATCHLEVEL = 4.1
CATEGORIES = xtra

DESCRIPTION = Norman Walsh's modular stylesheets for DocBook
define BLURB
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML)
format.  They are highly customizable.
endef

SF_PROJ = docbook
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = docbook-dsssl-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWdocbookdsssl,postinstall preremove)
PATCHFILES = add_makefile.patch fix_perl_path.patch

REQUIRED_PKGS = CSWdocbookdtds CSWsgmlcommon CSWopenjade CSWperl

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

tar-gz-extract-docbook-dsssl-$(GARVERSION).tar.gz:
	@echo " ==> Extracting $(DOWNLOADDIR)/docbook-dsssl-$(GARVERSION).tar.gz"
	@mkdir -p $(WORKSRC)
	@gzip -dc $(DOWNLOADDIR)/docbook-dsssl-$(GARVERSION).tar.gz | gtar $(TAR_ARGS) -xf - -C $(WORKSRC) --strip-components 1
	@$(MAKECOOKIE)

#nothing to configure or test
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

INSTALL_ARGS = DESTDIR=$(DESTDIR)
INSTALL_ARGS += bindir=$(bindir) datadir=$(datadir)

post-install-modulated:
	@echo "Symlinking dsssl-stylesheets"
	@(cd $(INSTALLISADIR)/$(datadir)/sgml/docbook; \
		ln -s dsssl-stylesheets-$(GARVERSION) dsssl-stylesheets )

include gar/category.mk

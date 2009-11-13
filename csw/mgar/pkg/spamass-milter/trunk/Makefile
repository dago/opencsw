GARNAME = spamass-milter
GARVERSION = 0.3.1
CATEGORIES = net

DESCRIPTION = Plugin for the Sendmail Milter library for SpamAssassin
define BLURB
  Plugin for the Sendmail Milter library for SpamAssassin
endef

MASTER_SITES = http://mirrors.aixtools.net/sv/spamass-milt/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWspamass-milter
CATALOGNAME = spamass_milter
REQUIRED_PKGS = CSWspamassassin

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

DOCLIST = AUTHORS Changelog NEWS README TODO

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),ginstall -m 444 $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	@$(MAKECOOKIE)

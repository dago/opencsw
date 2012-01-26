NAME = spamass-milter
VERSION = 0.3.1
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Plugin for the Sendmail Milter library for SpamAssassin
define BLURB
  Plugin for the Sendmail Milter library for SpamAssassin
endef

MASTER_SITES = http://mirrors.aixtools.net/sv/spamass-milt/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWspamass-milter
CATALOGNAME = spamass_milter
RUNTIME_DEP_PKGS = CSWspamassassin

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

DOCLIST = AUTHORS Changelog NEWS README TODO

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),ginstall -m 444 $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	@$(MAKECOOKIE)

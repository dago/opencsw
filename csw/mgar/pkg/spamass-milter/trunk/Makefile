NAME = spamass-milter
VERSION = 0.3.2
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Plugin for the Sendmail Milter library for SpamAssassin
define BLURB
  Plugin for the Sendmail Milter library for SpamAssassin
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/spamass-milt/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswspamass-milter
DISTFILES += spamass-milter.CSW
DISTFILES += README.CSW
DISTFILES += changelog.CSW
DISTFILES += COPYING

PATCHFILES  = 0000-Workaround-for-missing-paths.h.patch

INITSMF = $(sysconfdir)/init.d/cswspamass-milter
PRESERVECONF = $(sysconfdir)/spamass-milter

PACKAGES = CSWspamass-milter
RUNTIME_DEP_PKGS = CSWspamassassin

BUILD_DEP_PKGS  = CSWspamassassin
BUILD_DEP_PKGS += CSWsendmail
BUILD_DEP_PKGS += CSWlibmilter

LICENSE = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SENDMAIL = $(libdir)/sendmail

EXTRA_CONFIGURE_ENV = SENDMAIL=$(SENDMAIL)
EXTRA_CXX_FLAGS = -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

DOCLIST = AUTHORS ChangeLog NEWS README TODO

post-merge-modulated:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(PKGROOT)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),ginstall -m 444 $(WORKSRC)/$(DOC) $(PKGROOT)$(docdir)/$(NAME);)
	@$(MAKECOOKIE)

post-merge:
	@echo " ==> Installing startup script"
	@ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/init.d
	@ginstall -m 755 $(FILEDIR)/cswspamass-milter $(PKGROOT)$(sysconfdir)/init.d/
	@ginstall -m 755 $(FILEDIR)/spamass-milter.CSW $(PKGROOT)$(sysconfdir)/
	@$(MAKECOOKIE)

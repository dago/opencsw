NAME = clamavsigs
VERSION = 3.7.1
DISTNAME = clamav-unofficial-sigs-$(VERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = ClamAV Unofficial Signature Databases Update Script
define BLURB
  ClamAV Unofficial Signature Databases Update Script
endef

MASTER_SITES = http://www.inetmsg.com/pub/
DISTFILES    = clamav-unofficial-sigs-$(VERSION).tar.gz

PATCHFILES  = 0001-use-ksh-instead-of-sh-on-solaris.patch
PATCHFILES += 0002-make-defaults-match-csw-clamav.patch

LICENSE = LICENSE
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWgnupg CSWrsync CSWcurl CSWsocat

CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWrsync
CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWsocat
CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWcurl
CHECKPKG_OVERRIDES_CSWclamavsigs += file-with-bad-content|/usr/local|root/etc/opt/csw/clamav-unofficial-sigs.conf.CSW
CHECKPKG_OVERRIDES_CSWclamavsigs += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamavsigs/CHANGELOG
CHECKPKG_OVERRIDES_CSWclamavsigs += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamavsigs/INSTALL

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

SAMPLECONF = /etc/opt/csw/clamav-unofficial-sigs.conf
POSTMSG    = /opt/csw/share/doc/clamavsigs/README.CSW
CRONTABS   = /etc/opt/csw/pkg/CSWclamavsigs/crontabs/root

include gar/category.mk

DOCLIST = CHANGELOG INSTALL README

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@echo worksrc: $(WORKSRC)
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWclamavsigs/crontabs
	@ginstall -m 644 $(WORKSRC)/clamav-unofficial-sigs.conf $(DESTDIR)/etc/opt/csw
	@ginstall -m 644 $(FILEDIR)/crontab.root $(DESTDIR)/etc/opt/csw/pkg/CSWclamavsigs/crontabs/root
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),cp $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/clamav-unofficial-sigs.sh $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 $(WORKSRC)/clamav-unofficial-sigs.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

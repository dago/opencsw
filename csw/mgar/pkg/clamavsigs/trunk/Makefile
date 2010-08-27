GARNAME = clamavsigs
GARVERSION = 3.7.1
DISTNAME = clamav-unofficial-sigs-$(GARVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = utils

DESCRIPTION = ClamAV Unofficial Signature Databases Update Script
define BLURB
  ClamAV Unofficial Signature Databases Update Script
endef

MASTER_SITES = http://www.inetmsg.com/pub/
DISTFILES  = clamav-unofficial-sigs-$(GARVERSION).tar.gz
PATCHFILES = 0001-use-ksh-instead-of-sh-on-solaris.patch
PATCHFILES += 0002-make-defaults-match-csw-clamav.patch

LICENSE = LICENSE
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWgnupg CSWrsync CSWcurl CSWsocat

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWrsync
CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWsocat
CHECKPKG_OVERRIDES_CSWclamavsigs += surplus-dependency|CSWcurl

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SAMPLECONF = /etc/opt/csw/clamav-unofficial-sigs.conf
POSTMSG = /opt/csw/share/doc/clamavsigs/README.CSW
CRONTABS = /etc/opt/csw/pkg/CSWclamavsigs/crontabs/root

include gar/category.mk

DOCLIST = CHANGELOG INSTALL README

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@echo worksrc: $(WORKSRC)
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWclamavsigs/crontabs
	@ginstall -m 644 $(WORKSRC)/clamav-unofficial-sigs.conf $(DESTDIR)/etc/opt/csw
	@ginstall -m 644 $(FILEDIR)/crontab.root $(DESTDIR)/etc/opt/csw/pkg/CSWclamavsigs/crontabs/root
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),cp $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/clamav-unofficial-sigs.sh $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 $(WORKSRC)/clamav-unofficial-sigs.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

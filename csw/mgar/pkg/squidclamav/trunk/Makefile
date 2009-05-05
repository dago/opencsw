GARNAME = squidclamav
GARVERSION = 4.0
CATEGORIES = apps

DESCRIPTION = A Dedicated ClamAV AntiVirus Redirector for Squid
define BLURB
	SquidClamAv is a dedicated ClamAV antivirus redirector for Squid. 
	It can run antivirus checks based on filename regex, 
	content-type regex, and more. It is easy to install and works 
	even with heavy Squid access. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += squidclamav.conf.CSW
DISTFILES += CSWsquidclamav.postinstall

PACKAGES = CSWsquidclamav
CATALOGNAME_CSWsquidclamav = squidclamav
SPKG_DESC_CSWsquidclamav = $(DESCRIPTION)

REQUIRED_PKGS_CSWsquidclamav = CSWcurlrt

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)

EXTRA_LINKER_FLAGS += -lrt -lnsl -lsocket

TEST_TARGET = check

EXTRA_DOCFILES = AUTHORS ChangeLog INSTALL NEWS README

post-install-modulated:
	@ginstall -d $(DESTDIR)$(sysconfdir)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(libexecdir)/cgi-bin
	@cp $(DOWNLOADDIR)/squidclamav.conf.CSW $(DESTDIR)$(sysconfdir)
	@( for file in $(EXTRA_DOCFILES); do \
		cp $(abspath $(WORKSRC)/$$file) $(DESTDIR)$(docdir)/$(GARNAME); \
	done )
	@cp $(WORKSRC)/clwarn.cgi* $(DESTDIR)$(libexecdir)/cgi-bin
	@$(MAKECOOKIE)

include gar/category.mk

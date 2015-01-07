NAME = squidclamav
VERSION = 6.12
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A Dedicated ClamAV AntiVirus Redirector for Squid
define BLURB
	SquidClamAv is a dedicated ClamAV antivirus redirector for Squid. 
	It can run antivirus checks based on filename regex, 
	content-type regex, and more. It is easy to install and works 
	even with heavy Squid access. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).taCSWsquidclamav.postinstall

PACKAGES = CSWsquidclamav
SPKG_DESC_CSWsquidclamav = A Dedicated ClamAV AntiVirus Redirector for Squid
RUNTIME_DEP_PKGS_CSWsquidclamav += CSWlibgcc-s1

GARCOMPILER = GNU

REINPLACEMENTS += squidguard
REINPLACE_MATCH_squidguard = /usr/local/squidGuard/bin
REINPLACE_WITH_squidguard = $(bindir)
REINPLACE_FILES_squidguard += etc/squidclamav.conf

EXTRA_MERGE_EXCLUDE_FILES += .*\.default

PRESERVECONF += /etc/opt/csw/c-icap/squidclamav.conf

EXTRA_DOCFILES = AUTHORS ChangeLog INSTALL NEWS README

post-install:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	R)$(sysconfdir)
	@( for file in $(EXTRA_DOCFILES); do \
		cp $(abspath $(WORKSRC)/$$file) $(DESTDIR)$(docdir)/$(N$(MAKECOOKIE)

include gar/category.mk

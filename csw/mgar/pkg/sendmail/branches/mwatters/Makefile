GARNAME = sendmail
GARVERSION = 8.14.3
CATEGORIES = apps

DESCRIPTION = Sendmail MTA
define BLURB
endef

MASTER_SITES = ftp://ftp.sendmail.org/pub/sendmail/
DISTFILES  = $(GARNAME).$(GARVERSION).tar.gz

PACKAGES = CSWsendmail
CATALOGNAME_CSWsendmail = sendmail
SPKG_DESC_CSWsendmail = $(DESCRIPTION)
SPKG_SOURCEURL = http://www.sendmail.org/

REQUIRED_PKGS_CSWsendmail  = CSWolddaprt CSWsasl CSWosslrt CSWbdb

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

STRIP_LIBTOOL = 1

DISTFILES += site.config.m4

CONFIGURE_SCRIPTS  = custom
BUILD_SCRIPTS  = custom

include gar/category.mk

configure-custom:
	@( cp $(DOWNLOADDIR)/site.config.m4 $(WORKSRC)/devtools/Site/ )
	@$(MAKECOOKIE)

build-custom:
	@gmake -C $(WORKSRC) fresh
	@$(MAKECOOKIE)


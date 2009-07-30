GARNAME = sendmail
GARVERSION = 8.14.3
CATEGORIES = apps

DESCRIPTION = Sendmail MTA
define BLURB
endef

MASTER_SITES = http://ftp.sendmail.org/pub/sendmail/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWsendmail
CATALOGNAME_CSWsendmail = sendmail
SPKG_DESC_CSWsendmail = $(DESCRIPTION)
SPKG_SOURCEURL = http://www.sendmail.org/

REQUIRED_PKGS_CSWsendmail  = CSWolddaprt CSWsasl CSWosslrt CSWbdb

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk

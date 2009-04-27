GARNAME = squirrelmail
GARVERSION = 1.4.17
CATEGORIES = apps

DESCRIPTION = A standards-based webmail package written in PHP.
define BLURB
	SquirrelMail is a standards-based webmail package written in PHP. 
	It includes built-in pure PHP support for the IMAP and SMTP protocols, 
	and all pages render in pure HTML 4.0 (with no JavaScript required) 
	for maximum compatibility across browsers. It has very few requirements 
	and is very easy to configure and install. SquirrelMail has all the 
	functionality you would want from an email client, including strong 
	MIME support, address books, and folder manipulation. 
endef

ARCHALL = 1
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWsquirrelmail
CATALOGNAME_CSWsquirrelmail = squirrelmail
SPKG_DESC_CSWsquirrelmail = $(DESCRIPTION)

REQUIRED_PKGS_CSWsquirrelmail  = CSWimap CSWapache2c

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS = cswize

configure-cswize:
	@(perl -i -pe 's|/var/local|/opt/csw|' $(WORKSRC)/config/config_default.php)
	@(perl -i -pe 's|/usr/sbin/sendmail|/usr/lib/sendmail|' \
		        $(WORKSRC)/config/config_default.php)
	@$(MAKECOOKIE)

include gar/category.mk

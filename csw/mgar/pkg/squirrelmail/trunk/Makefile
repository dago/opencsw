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

LICENSE = COPYING
ARCHALL = 1

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWsquirrelmail.postinstall CSWsquirrelmail.preremove
DISTFILES += httpd-squirrelmail.conf.CSW

PACKAGES = CSWsquirrelmail
CATALOGNAME_CSWsquirrelmail = squirrelmail
SPKG_DESC_CSWsquirrelmail = $(DESCRIPTION)

REQUIRED_PKGS_CSWsquirrelmail  = CSWphp5 CSWapache2c

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS = cswize
BUILD_SCRIPTS = 
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

ALLOW_RELOCATE = 1
RELOCATE_PREFIX = /opt/csw/share/www
configure-cswize:
	@(perl -i -pe 's|/var/local|/var/opt/csw|' \
		$(WORKSRC)/config/config_default.php)
	@(perl -i -pe 's|/usr/sbin/sendmail|/usr/lib/sendmail|' \
		        $(WORKSRC)/config/config_default.php)
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(RELOCATE_PREFIX)/$(GARNAME)/contrib
	cd $(WORKSRC); /usr/bin/pax -rw -v * $(DESTDIR)$(RELOCATE_PREFIX)/$(GARNAME)
	gcp $(DOWNLOADDIR)/httpd-squirrelmail.conf.CSW \
		$(DESTDIR)$(RELOCATE_PREFIX)/$(GARNAME)/contrib
	@$(MAKECOOKIE)
	
include gar/category.mk

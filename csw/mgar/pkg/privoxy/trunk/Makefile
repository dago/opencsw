#
# WARNING. This is still a (non-maintainer) stub and needs to be checked
# against the current CSWprivoxy package by someone with regards to (at
# least) log rotation.
#
GARNAME = privoxy
GARVERSION = 3.0.12
CATEGORIES = net

DESCRIPTION = A web proxy with advanced filtering capabilities
define BLURB
Privoxy is a non-caching web proxy with advanced filtering capabilities
for enhancing privacy, modifying web page data and HTTP headers,
controlling access, and removing ads and other obnoxious Internet junk.
Privoxy has a flexible configuration and can be customized to suit
individual needs and tastes. It has application for both stand-alone
systems and multi-user networks.
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = ijbswa
DISTFILES  = $(GARNAME)-$(GARVERSION)-stable-src.tar.gz
DISTNAME = $(GARNAME)-$(GARVERSION)-stable

SPKG_SOURCEURL = http://www.privoxy.org/
SPKG_CLASSES = none cswusergroup cswcpsampleconf cswinitsmf

REQUIRED_PKGS = CSWclassutils CSWpcrert CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-stable-src.tar.gz

TEST_SCRIPTS =

sysconfdir = /opt/csw/etc/privoxy
localstatedir = /var/opt/csw/privoxy

CONFIGURE_ARGS = $(DIRPATHS)

# Supress sub directories for logs and pid file
INSTALL_ARGS = LOGS_DEST=$(localstatedir) PIDS_DEST=$(localstatedir)

PROTOTYPE_FILTER  = awk '\
        $$$$3 ~ /\/init.d\/cswprivoxy$$$$/ { $$$$2 = "cswinitsmf" } \
        $$$$3 ~ /cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
        $$$$3 ~ /.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
         { print }'

include gar/category.mk

pre-configure-modulated:
		@perl -pi -e 's|-Wall||' $(WORKSRC)/GNUmakefile.in
		@cd $(WORKSRC) && autoheader && autoconf
		@$(MAKECOOKIE)


post-install-modulated: CONFFILES := config user.action user.filter
post-install-modulated:
		@echo --- Installing cswusergroup file ---
		@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWprivoxy/
		@cp $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWprivoxy/

		@echo --- Installing cpsampleconf config files ---
		$(foreach C,$(CONFFILES), \
			mv $(DESTDIR)$(sysconfdir)/$(C) $(DESTDIR)$(sysconfdir)/$(C).CSW; )

		@echo --- Installing cswinitsmf file ---
		@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
		@cp $(FILEDIR)/cswprivoxy $(DESTDIR)/etc/opt/csw/init.d/
		@$(MAKECOOKIE)

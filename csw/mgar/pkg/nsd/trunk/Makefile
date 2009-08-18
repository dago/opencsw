GARNAME = nsd
GARVERSION = 3.2.3
CATEGORIES = server

DESCRIPTION = An authoritative only non-recursive name server
define BLURB
  NSD (Name Server Daemon) is a complete implementation of an
  authoritative DNS nameserver.
endef

MASTER_SITES = http://www.nlnetlabs.nl/projects/nsd/

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://www.nlnetlabs.nl/downloads/nsd/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWnsd
REQUIRED_PKGS = CSWcswclassutils CSWosslrt
CATALOGNAME = nsd
SPKG_DESC = An authoritative only non-recursive name server

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += cswusergroup
DISTFILES += cswnsd

SPKG_CLASSES = none cswusergroup ugfiles cswcpsampleconf cswinitsmf
PROTOTYPE_FILTER = awk '$$$$3 ~ /\/init.d\/cswnsd$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/CSWnsd\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } $$$$3 ~ /\/nsd\/nsd.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$2 = "ugfiles" }  $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$5 = "nsd" } $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$6 = "nsd" } { print }'

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-pidfile=/var/run/nsd.pid
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --with-dbfile=/var/opt/csw/nsd/nsd.db
CONFIGURE_ARGS += --with-difffile=/var/opt/csw/nsd/ixfr.db
CONFIGURE_ARGS += --with-xfrdfile=/var/opt/csw/nsd/xfrd.state

post-install-modulated:
	@ginstall -d $(DESTDIR)/var/opt/csw/nsd
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswnsd $(DESTDIR)/etc/opt/csw/init.d/cswnsd
	@mv $(DESTDIR)/etc/opt/csw/nsd/nsd.conf.sample $(DESTDIR)/etc/opt/csw/nsd/nsd.conf.CSW
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWnsd
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWnsd/cswusergroup

include gar/category.mk

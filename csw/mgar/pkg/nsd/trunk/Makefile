GARNAME = nsd
GARVERSION = 3.2.1
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

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnsd,)
DISTFILES += cswusergroup
DISTFILES += cswnsd

SPKG_CLASSES = none cswusergroup cswcpsampleconf cswinitsmf
PROTOTYPE_FILTER = awk '$$$$3 ~ /\/init.d\/cswnsd$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/nsd\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } $$$$3 ~ /\/nsd\/nsd.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$5 = "nsd" } $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$6 = "nsd" } { print }'

REQUIRED_PKGS = CSWcswclassutils

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

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
	@ginstall -m 755 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/nsd/cswusergroup

include gar/category.mk

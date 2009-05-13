GARNAME = unbound
GARVERSION = 1.2.1
CATEGORIES = server

DESCRIPTION = A validating, recursive, and caching DNS resolver
define BLUR
  Unbound is designed as a set of modular components, so that also
  DNSSEC (secure DNS) validation and stub-resolvers (that do not run as
  a server, but are linked into an application) are easily possible.
endef

MASTER_SITES = http://unbound.net/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWunbound)
DISTFILES += cswunbound
DISTFILES += cswusergroup

GARCOMPILER = GCC4

SPKG_CLASSES = none cswusergroup cswcpsampleconf cswinitsmf
PROTOTYPE_FILTER = awk '$$$$3 ~ /\/init.d\/cswunbound$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/CSWunbound\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } $$$$3 ~ /\/unbound\/unbound.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } { print }'

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGUTE_ARGS += --with-solaris-threads
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-pidfile=/var/run/unbound.pid
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw

REQUIRED_PKGS = CSWosslrt CSWgcc4corert CSWcswclassutils

post-install-modulated:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswunbound $(DESTDIR)/etc/opt/csw/init.d/cswunbound
	@ginstall -d 755 $(DESTDIR)/etc/opt/csw/pkg/CSWunbound
	@ginstall -m 755 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWunbound/cswusergroup
	@mv $(DESTDIR)/etc/opt/csw/unbound/unbound.conf $(DESTDIR)/etc/opt/csw/unbound/unbound.conf.CSW
	@chmod 444 $(DESTDIR)/etc/opt/csw/unbound/unbound.conf.CSW
	@$(MAKECOOKIE)

include gar/category.mk

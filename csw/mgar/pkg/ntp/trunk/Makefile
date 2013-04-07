NAME = ntp
VERSION = 4.2.6p5
GARTYPE = v2

DESCRIPTION = The Network Time Protocol Distribution
define BLURB
endef

MASTER_SITES = http://archive.ntp.org/ntp4/ntp-4.2/
DISTFILES = $(DISTNAME).tar.gz

SPKG_SOURCEURL = http://www.isc.org/software/ntp

PACKAGES += CSWntp
CATALOGNAME_CSWntp = ntp
SPKG_DESC_CSWntp = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWntp += CSWlibssl1-0-0

PACKAGES += CSWntp-snmp
CATALOGNAME_CSWntp-snmp = ntp_snmp
SPKG_DESC_CSWntp-snmp = $(DESCRIPTION) (SNMP)
RUNTIME_DEP_PKGS_CSWntp-snmp += CSWlibnetsnmp25
RUNTIME_DEP_PKGS_CSWntp-snmp += CSWlibnetsnmpagent25
RUNTIME_DEP_PKGS_CSWntp-snmp += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWntp-snmp += CSWntp
PKGFILES_CSWntp-snmp = .*ntpsnmpd.*

INITSMF = /etc/opt/csw/init.d/cswntp

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl-libdir=/opt/csw/lib
CONFIGURE_ARGS += --with-openssl-incdir=/opt/csw/include

# Doesn't make much sense without parent package
CHECKPKG_OVERRIDES_CSWntp-snmp += surplus-dependency|CSWntp                     

include gar/category.mk

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswntp $(DESTDIR)/etc/opt/csw/init.d/
	ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	ginstall -m 755 $(FILEDIR)/ntp $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)/
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)
	touch $(DESTDIR)/var/opt/csw/$(NAME)/ntp.drift

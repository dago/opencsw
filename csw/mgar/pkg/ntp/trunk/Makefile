NAME = ntp
VERSION = 4.2.8
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

PACKAGES += CSWpm-ntp-util
CATALOGNAME_CSWpm-ntp-util = pm_ntp_util
SPKG_DESC_CSWpm-ntp-util = $(DESCRIPTION) (Perl)
PKGFILES_CSWpm-ntp-util = .*Util.pm.*
ARCHALL_CSWpm-ntp-util = 1
RUNTIME_DEP_PKGS_CSWpm-ntp-util += CSWperl
RUNTIME_DEP_PKGS_CSWpm-ntp-util += CSWntp

PACKAGES += CSWntp-sntp
CATALOGNAME_CSWntp-sntp = ntp_sntp
SPKG_DESC_CSWntp-sntp = $(DESCRIPTION) (sntp)
PKGFILES_CSWntp-sntp = .*sntp.*
RUNTIME_DEP_PKGS_CSWntp-sntp += CSWlibevent-pthreads2-0-5
RUNTIME_DEP_PKGS_CSWntp-sntp += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWntp-sntp += CSWlibevent-core2-0-5

#PACKAGES += CSWntp-snmp
#CATALOGNAME_CSWntp-snmp = ntp_snmp
#SPKG_DESC_CSWntp-snmp = $(DESCRIPTION) (SNMP)
#RUNTIME_DEP_PKGS_CSWntp-snmp += CSWlibnetsnmp25
#RUNTIME_DEP_PKGS_CSWntp-snmp += CSWlibnetsnmpagent25
#RUNTIME_DEP_PKGS_CSWntp-snmp += CSWlibssl1-0-0
#RUNTIME_DEP_PKGS_CSWntp-snmp += CSWntp
#PKGFILES_CSWntp-snmp = .*ntpsnmpd.*

INITSMF = /etc/opt/csw/init.d/cswntp

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl-libdir=/opt/csw/lib
CONFIGURE_ARGS += --with-openssl-incdir=/opt/csw/include
#CONFIGURE_ARGS += --with-ntpsnmpd
#CONFIGURE_ARGS += --with-net-snmp-config

# Doesn't make much sense without parent package
#CHECKPKG_OVERRIDES_CSWntp-snmp += surplus-dependency|CSWntp                     

include gar/category.mk

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswntp $(DESTDIR)/etc/opt/csw/init.d/
	ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	ginstall -m 755 $(FILEDIR)/ntp $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)/
	ginstall -m 755 $(FILEDIR)/ntp.conf $(DESTDIR)/etc/opt/csw/
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)
	touch $(DESTDIR)/var/opt/csw/$(NAME)/ntp.drift
	rm -rf $(DESTDIR)/opt/csw/share/doc
	rm -rf $(DESTDIR)/opt/csw/share/man/man8
	rm -rf $(DESTDIR)/opt/csw/share/lib
	ginstall -d $(DESTDIR)/opt/csw/share/perl/csw/NTP
	mv $(DESTDIR)/opt/csw/share/ntp/lib/NTP/Util.pm $(DESTDIR)/opt/csw/share/perl/csw/NTP
	@$(MAKECOOKIE)

GARNAME = netsnmp
GARVERSION = 5.4.2.1
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

SF_PROJ = net-snmp
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(SF_PROJ)-$(GARVERSION).tar.gz

DISTNAME = $(SF_PROJ)-$(GARVERSION)

SPKG_SOURCEURL = http://www.net-snmp.org/

REQUIRED_PKGS += CSWosslrt CSWtcpwrap

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=12694
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-snmp-version=1
CONFIGURE_ARGS += --with-sys-contact=unknown
CONFIGURE_ARGS += --with-sys-location=unknown
CONFIGURE_ARGS += --with-logfile=/var/log/snmpd.log
CONFIGURE_ARGS += --with-persistent-directory=/opt/csw/var/net-snmp
CONFIGURE_ARGS += '--with-mib-modules=ucd-snmp/diskio agentx mibII/mta_sendmail' 
CONFIGURE_ARGS += '--with-libwrap=/opt/csw/lib' 
CONFIGURE_ARGS += '--enable-ipv6' 
CONFIGURE_ARGS += '--with-transports=UDP TCP Unix' 
CONFIGURE_ARGS += '--with-perl-modules=no' 
CONFIGURE_ARGS += '--with-python-modules=no'

PATCHFILES = perl_makefiles.diff

LD_OPTIONS =
export LD_OPTIONS

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

include gar/category.mk

post-install-isa-sparcv8:
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/old_libs_s.tar.gz |tar xf -)
	@ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10
	@ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10
	@ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10
	@ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10
	@ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10

post-install-isa-i386:
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/old_libs_i.tar.gz |tar xf -)
	@ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10
	@ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10
	@ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10
	@ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10
	@ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10

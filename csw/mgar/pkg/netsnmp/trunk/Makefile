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

PREREQUISITE_PKGS = CSWpysetuptools

REQUIRED_PKGS += CSWosslrt CSWtcpwrap CSWpython

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=12694
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

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
#CONFIGURE_ARGS += '--disable-embedded-perl'
CONFIGURE_ARGS += '--with-perl-modules=yes' 
CONFIGURE_ARGS += '--with-python-modules=yes'

# Patch for perl modules
PATCHFILES = perl_makefiles.diff
# Patch for python module
PATCHFILES += Makefile.in.diff

#LD_OPTIONS =
#EXTRA_COMMON_EXPORTS = LD_OPTIONS

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

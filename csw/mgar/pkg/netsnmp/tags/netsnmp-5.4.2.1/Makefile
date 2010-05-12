GARNAME = netsnmp
GARVERSION = 5.4.2.1
CATEGORIES = apps

DESCRIPTION = A suite of applications used to implement SNMP
define BLURB
  Simple Network Management Protocol (SNMP) is a widely used protocol for monitoring
  the health and welfare of network equipment (eg. routers), computer equipment and
  even devices like UPSs. Net-SNMP is a suite of applications used to implement
  SNMP v1, SNMP v2c and SNMP v3 using both IPv4 and IPv6. The suite includes:
endef

SF_PROJ = net-snmp
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(SF_PROJ)-$(GARVERSION).tar.gz

DISTNAME = $(SF_PROJ)-$(GARVERSION)

SPKG_SOURCEURL = http://www.net-snmp.org/
SPKG_DESC_CSWnetsnmp-py = NetSNMP Python Bindings

PACKAGES = CSWnetsnmp CSWnetsnmp-py 
CATALOGNAME_CSWnetsnmp = netsnmp
CATALOGNAME_CSWnetsnmp-py = netsnmp_py

BUILD_DEP_PKGS = CSWpysetuptools

RUNTIME_DEP_PKGS_CSWnetsnmp += CSWosslrt CSWtcpwrap CSWperl
RUNTIME_DEP_PKGS_CSWnetsnmp-py += CSWnetsnmp CSWpython
PKGFILES_CSWnetsnmp-py = $(libdir)/python.*

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=12694
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

#BUILD64 = 1
#NOISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-snmp-version=1
CONFIGURE_ARGS += --with-sys-contact=unknown
CONFIGURE_ARGS += --with-sys-location=unknown
CONFIGURE_ARGS += --with-logfile=/var/log/snmpd.log
CONFIGURE_ARGS += --with-persistent-directory=/opt/csw/var/net-snmp
CONFIGURE_ARGS += '--with-mib-modules=ucd-snmp/diskio agentx mibII/mta_sendmail if-mib' 
CONFIGURE_ARGS += '--enable-mfd-rewrites' 
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

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc
EXTRA_MERGE_EXCLUDE_FILES += .*/perllocal.pod

#TEST_TARGET =

include gar/category.mk

post-install-isa-sparcv8:
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(CURDIR)/$(FILEDIR)/old_libs_s.tar.gz |tar xf -)
	@( if [ ! -r work/solaris8-sparc/install-isa-sparcv8/opt/csw/lib/libnetsnmp.so.10 ] ; then ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10 ] ; then ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10 ] ; then ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10 ] ; then ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10 ] ; then ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10 ; fi )

post-install-isa-i386:
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(CURDIR)/$(FILEDIR)/old_libs_i.tar.gz |tar xf -)
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10 ] ; then ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10 ] ; then ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10 ] ; then ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10 ] ; then ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10 ] ; then ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10 ; fi )

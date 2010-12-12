NAME = netsnmp
VERSION = 5.4.2.1
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
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

# Patch for perl modules
PATCHFILES = perl_makefiles.diff
# Patch for python module
PATCHFILES += Makefile.in.diff

SPKG_SOURCEURL = http://www.net-snmp.org/

BUILD_DEP_PKGS = CSWpysetuptools
RUNTIME_DEP_PKGS = CSWosslrt CSWtcpwrap CSWpython

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=12694
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# We must use the same compiler as Perl was compiled with or the compile
# flags will not be properly recognized
GARCOMPILER = SOS11

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS_mm-32  = --disable-embedded-perl --with-perl-modules=yes
CONFIGURE_ARGS_mm-32 += --with-python-modules=yes
CONFIGURE_ARGS_mm-32 += --with-libwrap=/opt/csw/lib
CONFIGURE_ARGS_mm-64  = --disable-embedded-perl --without-perl-modules
CONFIGURE_ARGS_mm-64 += --without-python-modules
CONFIGURE_ARGS_mm-64 += --without-libwrap

CONFIGURE_ARGS_os-5.10 = --with-mib-modules=if-mib --enable-mfd-rewrites

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-snmp-version=1
CONFIGURE_ARGS += --with-sys-contact=unknown
CONFIGURE_ARGS += --with-sys-location=unknown
CONFIGURE_ARGS += --with-logfile=/var/log/snmpd.log
CONFIGURE_ARGS += --with-persistent-directory=/opt/csw/var/net-snmp
CONFIGURE_ARGS += --with-mib-modules="ucd-snmp/diskio agentx mibII/mta_sendmail"
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-transports="UDP TCP Unix"
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_os-$(GAROSREL))

# Disable testsuite until this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3007318&group_id=12694&atid=112694
SKIPTEST ?= 1

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

MERGE_DIRS_isa-extra = $(libdir)

# Overriding specific libs is not possible right now. Refine when finished.
# CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found|opt/csw/lib/python/site-packages/netsnmp/client_intf.so
CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found
CHECKPKG_OVERRIDES_CSWnetsnmp += missing-dependency|CSWperl

CHECKPKG_OVERRIDES_CSWnetsnmp += discouraged-path-in-pkgmap|/opt/csw/lib/python/site-packages/netsnmp/__init__.pyc
CHECKPKG_OVERRIDES_CSWnetsnmp += discouraged-path-in-pkgmap|/opt/csw/lib/python/site-packages/netsnmp/client.pyc
CHECKPKG_OVERRIDES_CSWnetsnmp += discouraged-path-in-pkgmap|/opt/csw/lib/python/site-packages/netsnmp/tests/__init__.pyc
CHECKPKG_OVERRIDES_CSWnetsnmp += discouraged-path-in-pkgmap|/opt/csw/lib/python/site-packages/netsnmp/tests/test.pyc
CHECKPKG_OVERRIDES_CSWnetsnmp += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWnetsnmp += catalogname-does-not-start-with-py_

include gar/category.mk

post-install-isa-sparcv8:
	( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/old_libs_s.tar.gz |tar xf -)
	ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10
	ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10
	ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10
	ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10
	ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10
	@$(MAKECOOKIE)

post-install-isa-i386:
	( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/old_libs_i.tar.gz |tar xf -)
	ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10
	ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10
	ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10
	ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10
	@ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10
	@$(MAKECOOKIE)

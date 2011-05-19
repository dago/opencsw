NAME = netsnmp
VERSION = 5.6.1
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

VENDOR_URL = http://www.net-snmp.org/

BUILD_DEP_PKGS = CSWpysetuptools
RUNTIME_DEP_PKGS = CSWosslrt CSWtcpwrap CSWpython

BUILD64 = 1

# The -I/opt/csw/include pulls in installed version before built version and breaks testsuite
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS)

# CONFIGURE_ARGS_mm-32  = --disable-embedded-perl --with-perl-modules=yes
CONFIGURE_ARGS_mm-32  = --enable-embedded-perl --with-perl-modules=yes
# Disable MIBs due to LARGEFILE issue
CONFIGURE_ARGS_mm-32 += --with-out-mib-modules="ucd_snmp host mibII/ipv6 ucd_snmp/memory ucd_snmp/memory_solaris2 ucd_snmp/proc host/hr_swrun host/hr_storage"
#CONFIGURE_ARGS_mm-32 += --disable-perl-cc-checks
CONFIGURE_ARGS_mm-32 += enable_perl_cc_checks=no

enable_perl_cc_checks = no
EXTRA_CONFIGURE_EXPORTS = enable_perl_cc_checks

CONFIGURE_ARGS_mm-32 += --with-python-modules=yes
CONFIGURE_ARGS_mm-64  = --disable-embedded-perl --without-perl-modules
CONFIGURE_ARGS_mm-64 += --without-python-modules

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-snmp-version=1
CONFIGURE_ARGS += --with-sys-contact=unknown
CONFIGURE_ARGS += --with-sys-location=unknown
CONFIGURE_ARGS += --with-logfile=/var/log/snmpd.log
CONFIGURE_ARGS += --with-persistent-directory=/opt/csw/var/net-snmp
CONFIGURE_ARGS += --with-mib-modules="ucd-snmp/diskio agentx mibII/mta_sendmail"
CONFIGURE_ARGS += --with-libwrap=/opt/csw/lib
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-transports="UDP TCP Unix"
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))


# TBD: Make alternatives
# - with embedded Perl and disabled modules
#     --with-mib-modules="smux mibII/mta_sendmail"
#     --with-defaults --enable-ipv6 --with-out-mib-modules="ucd_snmp host mibII/ipv6 ucd_snmp/memory ucd_snmp/memory_solaris2 ucd_snmp/proc host/hr_swrun host/hr_storage" --with-perl-modules --enable-embedded-perl --disable-perl-cc-checks --enable-shared
# - without embedded Perl and all modules

# Disable testsuite until this has been fixed or /tmp will fill up:
#   https://sourceforge.net/tracker/?func=detail&aid=3006962&group_id=12694&atid=112694
SKIPTEST ?= 1

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

# Overriding specific libs is not possible right now. Refine when finished.
# CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found|opt/csw/lib/python/site-packages/netsnmp/client_intf.so
CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found
CHECKPKG_OVERRIDES_CSWnetsnmp += missing-dependency|CSWperl

include gar/category.mk

#post-install-isa-sparcv8:
#	( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/old_libs_s.tar.gz |tar xf -)
#	ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10
#	ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10
#	ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10
#	ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10
#	ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10
#	@$(MAKECOOKIE)

#post-install-isa-i386:
#	( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/old_libs_i.tar.gz |tar xf -)
#	ln -s libnetsnmp.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmp.so.10
#	ln -s libnetsnmpagent.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpagent.so.10
#	ln -s libnetsnmphelpers.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmphelpers.so.10
#	ln -s libnetsnmpmibs.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmpmibs.so.10
#	@ln -s libnetsnmptrapd.so.10.0.1 $(INSTALLISADIR)$(libdir)/libnetsnmptrapd.so.10
#	@$(MAKECOOKIE)

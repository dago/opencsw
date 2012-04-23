# TBD before release:
# - compile 64 bit version with embedded perl, this should resolve the largefile issue
# - reenable tcpwrappers for both 32 and 64 bit
# - reenable python bindings
#

NAME = netsnmp
VERSION = 5.6.1.1
CATEGORIES = apps
GARTYPE = v2

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
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWpython
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWperl


# BUILD64 = 1

# The -I/opt/csw/include pulls in installed version before built version and breaks testsuite
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS)
# link not to the old already installed libs
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS) -xnorunpath

CONFIGURE_ARGS_mm-32  = --disable-embedded-perl --with-perl-modules=yes
# Enable Perl for 64 bit later
#
# CONFIGURE_ARGS_mm-64  = --disable-embedded-perl --without-perl-modules
CONFIGURE_ARGS_mm-64  = --enable-embedded-perl --with-perl-modules
CONFIGURE_ARGS_mm-64 += --without-python-modules

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-snmp-version=1
CONFIGURE_ARGS += --with-sys-contact=unknown
CONFIGURE_ARGS += --with-sys-location=unknown
CONFIGURE_ARGS += --with-logfile=/var/log/snmpd.log
CONFIGURE_ARGS += --with-persistent-directory=/opt/csw/var/net-snmp
CONFIGURE_ARGS += --with-mib-modules="ucd-snmp/diskio agentx mibII/mta_sendmail"
# Disable for now
# CONFIGURE_ARGS += --with-libwrap=/opt/csw/lib
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-transports="UDP TCP Unix"
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# Solaris /bin/bash does not allow empty lists in "for i in ; do echo; done"
EXTRA_CONFIGURE_EXPORTS = CONFIG_SHELL
EXTRA_CONFIGURE_ENV_CONFIG_SHELL = /opt/csw/bin/bash

# TBD: Make alternatives
# - with embedded Perl and disabled modules
#     --with-mib-modules="smux mibII/mta_sendmail"
#     --with-defaults --enable-ipv6 --with-out-mib-modules="ucd_snmp host mibII/ipv6 ucd_snmp/memory ucd_snmp/memory_solaris2 ucd_snmp/proc host/hr_swrun host/hr_storage" --with-perl-modules --enable-embedded-perl --disable-perl-cc-checks --enable-shared
# - without embedded Perl and all modules

# Disable testsuite until this has been fixed or /tmp will fill up:
#   https://sourceforge.net/tracker/?func=detail&aid=3006962&group_id=12694&atid=112694
SKIPTEST ?= 1

TEST_TARGET = test

INSTALL_OVERRIDE_VARS += SHELL
INSTALL_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

# Overriding specific libs is not possible right now. Refine when finished.
# CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found|opt/csw/lib/python/site-packages/netsnmp/client_intf.so
# CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/site_perl/NetSNMP/TrapReceiver.pm
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/bin/ipf-mod.pl
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/snmp/mib2c-data/mfd-makefile.m2m
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/snmpcmd.1
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/snmpconf.1
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/snmpd.8
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/snmpd.conf.5
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/NetSNMP::TrapReceiver.3perl
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/share|root/opt/csw/bin/net-snmp-cert
# override bad-rpath-entry becasue of /opt/csw/lib/ in perl module libs
CHECKPKG_OVERRIDES_CSWnetsnmp += bad-rpath-entry

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && autoreconf
	@$(MAKECOOKIE)


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

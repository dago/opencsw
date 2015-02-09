# TBD before release:
# - compile 64 bit version with embedded perl, this should resolve the largefile issue
# - reenable tcpwrappers for both 32 and 64 bit
# - reenable python bindings
#

NAME = netsnmp
VERSION = 5.7.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A suite of applications used to implement SNMP
define BLURB
  Simple Network Management Protocol (SNMP) is a widely used protocol for monitoring
  the health and welfare of network equipment (eg. routers), computer equipment and
  even devices like UPSs. Net-SNMP is a suite of applications used to implement
  SNMP v1, SNMP v2c and SNMP v3 using both IPv4 and IPv6. The suite includECTes:
endef

SF_PROJ = net-snmp
MASTER_SITES = $(SF_MIRRORS)
DIECT)-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

REINPLACE_USRLOCAL += perl/TrapReceiver/TrapReceiver.pm
REINPLACE_USRLOCAL += local/ipf-mod.pl
REINPLACE_USRLOCAL += local/traptoemail$REINPLACE_USRSHARE += local/net-snmp-cert$(DISTNAME).tar.gz

# Patch for perl modules
PATCHFILES = perl_makefiles.diff
# Patch for python module
PATCHFILES += Makefile.in.diff
PATCHFILES PATCHFILES += 0001-fixing-init-scripts.patch
PATCHFILES += 0002-workaround-ksh-stop-alias-problem.patch
PATCHFILES += 0003-configure-disable-perl-cc-checks.patch
PATCHFILES += 0004-enable-python-version-select.patch
# bug https://sourceforge.net/p/net-snmp/bugs/2585/
PATCHFILES += 0005-autotools-config_os_progs.patch
# the following patches inspired by https://java.net/projects/solaris-userland of different authors
PATCHFILES += 0002-pkcs.patch
PATCHFILES += 0011-Makefile.in.patch
PATCHFILES += 0012-Makefile.PL.patch
PATCHFILES += 0015+0016-vmstat_solaris2.patch
PATCHFILES += 0024-kernel_sunos5.$(GAROSREL).patch
PATCHFILES += 0034-manpage-snmptrapd.conf.5.def.patch
PATCHFILES += 0035-bug-1849903.patch
PATCHFILES += 0048+0027-mnt-cache-hr_filesys.patch
PATCHFILES += 0051-CVE-2014-2285.patch
PATCHFILES += 0052-dyn-cpu-cpu_kstat.patch

VENDOR_URL = http://www.net-snmp.org/

# GARCOMPILER = SOS12U3
GARCOMPILER = GCC4

BUILD_DEP_PKGS = CSWpy-setuptools
BUILD_DEP_PKGS += CSWautomake
BUILD_DEP_PKGS += CSWautoconf
BUILD_DEP_PKGS += CSWlibtool
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWpython27-dev
 = CSWpysetuptools
PACKAGING_PLATFORMS += solaris10-sp solaris11-sparc solaris1110-sparINITSMF = $(sysconfdir)/init.d/netsnmpd
INITSMF += $(sysconfdir)/init.d/netsnmptrapdar
EXTRA_MODULATORS += PYTHON_VERSION
MODULATIONS_PYTHON_VERSION = 2.6 2.7
# We need 64 bit just once as it is without python anyway
SKIP_MODULATIONS += isa-sparcv9-python_version-2.7
SKIP_MODULATIONS += isa-amd64-python_version-2.7
PYTHON = $(bindir)/python$(PYTHON_VERSION)
MERGE_SCRIPTS_isa-default-python_version-2.6 += copy-all
MERGE_SCRIPTS_isa-default-python_version-2.7 += copy-all
MERGE_SCRIPTS_isa-default64-python_version-2.6 += copy-relocated-only
MERGE_DIRS_isa-default64-python_version-2.6 += $(libdir)arc solaris10-i386

PACKAGES += CSWnetsnmp-dev
CATALOGNAME_CSWnetsnmp-dev = netsnmp_dev
SPKG_DESC_CSWnetsnmp-dev += $(DESCRIPTION), development files
PKGFILES_CSWnetsnmp-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKS_CSWnetsnmp-dev += CS30
RUNTIME_DEP_PKGS_CSWnetsnmp-dev += CSWlibnetsnmpmibs30
RUNTIME_DEP_PKGS_CSWnetsnmp-dev += CSWlibnetsnmptrapd30
RUNTIME_DEP_PKGS_CSWnetsnmp-dev += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWnetsnmp-dev += CSWlibnetsnmpagent30W# libnetsnmpagent25
CHECKPKG_OVERRIDES_CSWnetsnmp-dev += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/NetSNMP::TrapReceiver.3perl

PACKAGE30
CATALOGNAME_CSWlibnetsnmp30 = libnetsnmp30
SPKG_DESC_CSWlibnetsnmp30 += $(DESCRIPTION), libsnmp.so.30
PKGFILES_CSWlibnetsnmp30 += $(call baseisadirs,$(libdir),libnetsnmp\.so\.30(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibnetsnmp30 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibnetsnmp30 += CSWlibgcc-s1


PACKAGES += CSWlibnetsnmpagent30
CATALOGNAME_CSWlibnetsnmpagent30 = libnetsnmpagent30
SPKG_DESC_CSWlibnetsnmpagent30 += $(DESCRIPTION), libsnmpagent.so.30
PKGFILES_CSWlibnetsnmpagent30 += $(call baseisadirs,$(libdir),libnetsnmpagent\.so\.30(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibnetsnmpagent30 += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWlibnetsnmpagent30 += CSWlibgcc-s1

PACKAGES += CSWlibnetsnmphelpers30
CATALOGNAME_CSWlibnetsnmphelpers30 = libnetsnmphelpers30
SPKG_DESC_CSWlibnetsnmphelpers30 += $(DESCRIPTION), libsnmphelpers.so.30
PKGFILES_CSWlibnetsnmphelpers30 += $(call baseisadirs,$(libdir),libnetsnmphelpers\.so\.30(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibnetsnmphelpers30 += CSWlibgcc-s1

PACKAGES += CSWlibnetsnmpmibs30
CATALOGNAME_CSWlibnetsnmpmibs30 = libnetsnmpmibs30
SPKG_DESC_CSWlibnetsnmpmibs30 += $(DESCRIPTION), libsnmpmibs.so.30
PKGFILES_CSWlibnetsnmpmibs30 += $(call baseisadirs,$(libdir),libnetsnmpmibs\.so\.30(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibnetsnmpmibs30 += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWlibnetsnmpmibs30 += CSWlibnetsnmpagent30
RUNTIME_DEP_PKGS_CSWlibnetsnmpmibs30 += CSWlibgcc-s1

PACKAGES += CSWlibnetsnmptrapd30
CATALOGNAME_CSWlibnetsnmptrapd30 = libnetsnmptrapd30
SPKG_DESC_CSWlibnetsnmptrapd30 += $(DESCRIPTION), libsnmptrapd.so.30
PKGFILES_CSWlibnetsnmptrapd30 += $(call baseisadirs,$(libdir),libnetsnmptrapd\.so\.30(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibnetsnmptrapd30 += CSWlibnetsnmpmibs30
RUNTIME_DEP_PKGS_CSWlibnetsnmptrapd30 += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWlibnetsnmptrapd30 += CSWlibnetsnmpagent30WRUNTIME_DEP_PKGS_CSWlibnetsnmptrapd30 += CSWlibgcc-s1W+= CSWlibssl1-0-0

EXTRA_MERGE_EXCLUDE_FILES += .*/perllocal.pod
PACKAGES += CSWpmnetsnmp
SPKG_DESC_CSWpmnetsnmp+= $(DESCRIPTION), Perl binding
PKGFILES_CSWpmnetsnmp += $(libdir)/perl.*
RUNTIME_DEP_PKGS_CSWpmn# etsnmp += CSWperl
RUNTIME_DEP_PKGS_CSWpmnetsnmp +=30
RUNTIME_DEP_PKGS_CSWpmnetsnmp += CSWlibnetsnmptrapd30
RUNTIME_DEP_PKGS_CSWpmnetsnmp += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWpmnetsnmp += CSWlibnetsnmpagent30W+= CSWlibssl1-0-0

EXTRA_MERGE_EXCLUDE_FILES += .*/*.pyc
PACKAGES#  += CSWpy-netsnmp
OBSOLETED_BY_CSWpy-netsnmp = CSWnetsnmp-py
SPKG_DESC_CSWpy-netsnmp += $(DESCRIPTION), Python binding
PKGFILES_CSWpy-netsnmp = $(libdir)/python.*
RUNTIME_DEP_PKGS_CSWpy-netsnmp += CSWpython
RUNTIME_DEP_PKGS_CSWpy-netsnmp += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-netsnm30+RUNTIME_DEP_PKGS_CSWpy-netsnmp += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-netsnmp += CSWlibpython2-7-1-0
CHECKPKG_OVERRIDES_CSWpy-netsnmp += surplus-dependency|CSWpython++= CSWlibssl1-0-0

PACKAGES += CSWnetsnmp
SPKG_DESC_CSWnetsnmp += $(DESCRIPTION), Base
RUNTIME_DEP_PKGS_CSWnetsnmp +=30
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWlibnetsnmptrapd30
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWlibnetsnmpagent30Wlibnetsnmpagent25
RUNTIME_DEP_PKGS_CSWnetsnmp += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWn# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/lshare/man/man1/snmpcmd.1
# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/lshare/man/man1/snmpconf.1
# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/lshare/man/man8/snmpd.8
# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/lshare/man/man5/snmpd.conf.5
# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/localtraptoemail
# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/c# w/bin/traptoemail
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/local|root/opt/csw/share/snmp/mib2c-data# /mfd-makefile.m2m
CHECKPKG_OVERRIDES_CSWnetsnmp += file-with-bad-content|/usr/share|root/opt/csw/bin/net-snmp-cert

# BUILD64 = 1
BUILD64_LIBS_ONLY = 1
NOISALIST = 1

# The -I/opt/csw/include pulls in installed version before built version and#  breaks testsuite
CPPFLAGS =
EXTRA_CFLAGS = $(INCLUDE_FLAGS)
# link not to the old alrea# LD_OPTIONS =
# EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS) -xnorunpath
# EXTRA_LDFLAGS = $(LD_OPTIONS)FLAGS) -xnorunpath

CONFIGURE_ARGS_mm-32  = --disable-embedded-perl
CONFIGURE_ARGS_mm-32  += --wit --disable-perl-cc-checkth-perl-modules=yes
CONFIGURE_ARGS_mm-32  += --with-python-modules=yes
# Enable Perl for 64 bit later
#
# we have no perl64 nr python64
CONFIGURE_ARGS_mm-64  = --disable-embedded-perl 
# CONFIGURE_ARGS_mm-64  = --enable-embedded-perl 
# CONFIGURE_ARGS_mm-64  += --with-perl-modules
CONFIGURE_ARGS_mm-64 += --without-perl-modules
CONFIGURE_ARGS_mm-64 += --without-python-modules

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-snmp-version=1
CONFIGURE_ARGS += --with-sys-contact=unknown
CONFIGURE_ARGS += --with-sys-location=unknown
CONFIGURE_ARGS += --with-logfile=/var/opt/csw/log/snmpd.log
CONFIGURE_ARGS += --with-persistent-directory=/var/opt/csw/net-snmp
CONFIGURE_ARGS += --host ucd-snmp/diskio agentx mibII/mta_sendmail ucd-snmp/lmSensorsmibII/mta_sendmail"
# Disable for now
# CONFIGURE_ARGS += --with-libwrap=/opt/csw/lib
CONFIGURE_ARGS += --enable-ipv6
COenable-mfd-rewritesS += --enable-ipv6
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-transports="UDP TCP Unix"
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# Solaris /bin/bash does not allow empty lists in "for i in ; do echo; done"NV += CONFIG_SHELL=NV_CONFIG_SHELL = # use gmake for make
EXTRA_BUILD_ENV += PATH=/opt/csw/gnu:$(PATH) PYTHON=$(PYTHON)
EXTRA_INSTALL_ENV += PATH=/opt/csw/gnu:$(PATH) PYTHON=$(PYTHON) /opt/csw/bin/bash

# TBD: Make alternatives
# - with embedded Perl and disabled modules
#     --with-mib-modules="smux mibII/mta_sendmail"
#     --with-defaults --enable-ipv6 --with-out-mib-modules="ucd_snmp host mibII/ipv6 ucd_snmp/memory ucd_snmp/memory_solaris2 ucd_snmp/proc host/hr_swrun host/hr_storage" --with-perl-modules --enable-embedded-perl --disable-perl-cc-checks --enable-shared
# - without embedded Perl and all modules

# Disable testsuite until this has been fixed or /tmp will fill up:
#   https://sourceforge.net/tracker/?func=detail&aid=3006962&group_id=12694&ati=112694
SKIPTEST ?= 1

TEST_TARGET = test

INSTALL_OVERRIDE_VARS += SHELL
INSTALL_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash


# Overriding specific libs is not possible right now. Refine when finished.
# CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found|opt/csw/lib/python/site-packages/netsnmp/client_intf.so
# CHECKPKG_OVERRIDES_CSWnetsnmp  = symbol-not-found

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && autoreconf
	@$(MAKECOOKIE)

# if find the header in /opt/csw/include first use the old header from
# installed older version, thats why remove /opt/csw/include
CFLAGS := $(filter-out -I/opt/csw/iCFLAGS := $(filter-out -march=%-I/opt/csw/include,$(CFLAGS))
# LDFLAGS := $(filter-out -R/opt/csw/lib% -L/opt/cswpost-install:
	ginstall -d $(DESTDIR)/$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)/$(sysconfdir)/snmp
	ginstall -d $(DESTDIR)/$(localstatedir)/log
	ginstall -m 755	$(WORKSRC)/dist/snmpd-init.d $(DESTDIR)/$(sysconfdir)/init.d/netsnmpd
	ginstall -m 755	$(WORKSRC)/dist/snmptrapd-init.d $(DESTDIR)/$(sysconfdir)/init.d/netsnmptrapd
	ginstall -m 755	$(WORKSRC)/EXAMPLE.conf $(DESTDIR)/$(sysconfdir)/snmp/snmpd.conf
	@$(MAKECOOKIEcs
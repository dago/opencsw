# $Id$
#
NAME = collectd
VERSION = 5.4.2
GARTYPE = v2

DESCRIPTION = Collects system performance statistics periodically

MASTER_SITES = http://collectd.org/files/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswcollectd

VENDOR_URL = http://collectd.org/

# Lots of others missing
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWnetsnmp-dev
BUILD_DEP_PKGS += CSWlibyajl-dev
BUILD_DEP_PKGS += CSWjdk7

EXTRA_CPPFLAGS = -D__EXTENSIONS__

GARCOMPILER = GNU

BUILD64 = 1
# BUILD64_ONLY = 1
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)

# Disable for now and probably try this patch:
#   http://mailman.verplant.org/pipermail/collectd/2010-February/003558.html
CONFIGURE_ARGS += --disable-dns

# Make sure net-snmp-config is found at the correct path for both 32 and 64 bit
CONFIGURE_ARGS += --with-snmp-config=$(bindir)/net-snmp-config

# Use only Java 8 and 64 bit until this is fixed:
#   https://github.com/collectd/collectd/issues/1007
# Also the detection uses "find" which does not follow symlinks

JAVA_ARCHDIR-sparc-32 = sparc
JAVA_ARCHDIR-sparc-64 = sparcv9
JAVA_ARCHDIR-i386-32 = i386
JAVA_ARCHDIR-i386-64 = amd64
JAVA_ARCHDIR = $(JAVA_ARCHDIR-$(GARCH)-$(MEMORYMODEL))

JAVA_HOME=/opt/csw/java/jdk/jdk7
JAVA_LIBDIR = $(JAVA_HOME)/jre/lib/$(JAVA_ARCHDIR)/server

JAVAC = $(JAVA_HOME)/bin/javac
JAR = $(JAVA_HOME)/bin/jar
JAVA_CPPFLAGS = -I$(JAVA_HOME)/include
JAVA_LDFLAGS = -L$(JAVA_LIBDIR) -R$(JAVA_LIBDIR)

CONFIGURE_ARGS += --enable-java
CONFIGURE_ARGS += JAVAC="$(JAVAC)"
CONFIGURE_ARGS += JAR="$(JAR)"
CONFIGURE_ARGS += JAVA_CPPFLAGS="$(JAVA_CPPFLAGS)"
CONFIGURE_ARGS += JAVA_LDFLAGS="$(JAVA_LDFLAGS)" 

CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

PACKAGES += CSWlibcollectdclient1
SPKG_DESC_CSWlibcollectdclient1 = $(DESCRIPTION), libcollectdclient.so.1
PKGFILES_CSWlibcollectdclient1 += $(call pkgfiles_lib,libcollectdclient.so.1)
RUNTIME_DEP_PKGS_CSWlibcollectdclient1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcollectdclient1 += CSWlibgcrypt20

PACKAGES += CSWcollectd-dev
SPKG_DESC_CSWcollectd-dev = Development files for libcollectdclient.so.1
PKGFILES_CSWcollectd-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWcollectd-dev += CSWlibcollectdclient1

PACKAGES += CSWcollectd
SPKG_DESC_CSWcollectd = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibcollectdclient1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWcollectd += CSWperl
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibyajl2
# These are pulled in because of a linker anomaly
RUNTIME_DEP_PKGS_CSWcollectd-sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcollectd-i386 += CSWlibmemcached8
RUNTIME_DEP_PKGS_CSWcollectd-i386 += CSWlibfl2
RUNTIME_DEP_PKGS_CSWcollectd += $(RUNTIME_DEP_PKGS_CSWcollectd-$(GARCH))

PACKAGES += CSWcollectd-plugin-dbi
SPKG_DESC_CSWcollectd-plugin-dbi = CollectD Plugin for DBI
PKGFILES_CSWcollectd-plugin-dbi += $(call pkgfiles_lib,collectd/dbi.so)
RUNTIME_DEP_PKGS_CSWcollectd-plugin-dbi += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-dbi += CSWlibdbi1

PACKAGES += CSWcollectd-plugin-gmond
SPKG_DESC_CSWcollectd-plugin-gmond = CollectD Plugin for Ganglia gmond
PKGFILES_CSWcollectd-plugin-gmond += $(call pkgfiles_lib,collectd/gmond.so)
RUNTIME_DEP_PKGS_CSWcollectd-plugin-gmond += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-gmond += CSWlibganglia0
# No 64 bit ganglia yet
CHECKPKG_OVERRIDES_CSWcollectd-plugin-gmond += 64-bit-binaries-missing

PACKAGES += CSWcollectd-plugin-java
SPKG_DESC_CSWcollectd-plugin-java = CollectD Plugin for Java
PKGFILES_CSWcollectd-plugin-java += $(call pkgfiles_lib,collectd/java.so)
PKGFILES_CSWcollectd-plugin-java += $(sharedstatedir)/java/.*
RUNTIME_DEP_PKGS_CSWcollectd-plugin-java += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-java += CSWjre7
# There are some symlinks that confuse checkpkg
CHECKPKG_OVERRIDES_CSWcollectd-plugin-java += soname-not-found|libjvm.so|is|needed|by|opt/csw/lib/sparcv9/collectd/java.so
CHECKPKG_OVERRIDES_CSWcollectd-plugin-java += soname-not-found|libjvm.so|is|needed|by|opt/csw/lib/amd64/collectd/java.so
CHECKPKG_OVERRIDES_CSWcollectd-plugin-java += soname-not-found|libjvm.so|is|needed|by|opt/csw/lib/collectd/java.so
CHECKPKG_OVERRIDES_CSWcollectd-plugin-java += surplus-dependency|CSWjre7

PACKAGES += CSWcollectd-plugin-mysql
SPKG_DESC_CSWcollectd-plugin-mysql = CollectD Plugin for MySQL
PKGFILES_CSWcollectd-plugin-mysql += $(call pkgfiles_lib,collectd/mysql.so)
RUNTIME_DEP_PKGS_CSWcollectd-plugin-mysql += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-mysql += CSWlibmysqlclient18

PACKAGES += CSWcollectd-plugin-postgresql
SPKG_DESC_CSWcollectd-plugin-postgresql = CollectD Plugin for PostgreSQL
PKGFILES_CSWcollectd-plugin-postgresql += $(call pkgfiles_lib,collectd/postgresql.so)
PKGFILES_CSWcollectd-plugin-postgresql += $(sharedstatedir)/collectd/postgresql_default.conf
RUNTIME_DEP_PKGS_CSWcollectd-plugin-postgresql += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-postgresql += CSWlibpq5

PACKAGES += CSWcollectd-plugin-python
SPKG_DESC_CSWcollectd-plugin-python = CollectD Plugin for Python
PKGFILES_CSWcollectd-plugin-python += $(call pkgfiles_lib,collectd/python.so)
PKGFILES_CSWcollectd-plugin-python += $(mandir)/man5/collectd-python.5
RUNTIME_DEP_PKGS_CSWcollectd-plugin-python += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-python += CSWlibpython2-7-1-0
# No 64 bit Python yet
CHECKPKG_OVERRIDES_CSWcollectd-plugin-python += 64-bit-binaries-missing

PACKAGES += CSWcollectd-plugin-rrdtool
SPKG_DESC_CSWcollectd-plugin-rrdtool = CollectD Plugin for RRDTool and RRDCache
PKGFILES_CSWcollectd-plugin-rrdtool += $(call pkgfiles_lib,collectd/rrdtool.so)
PKGFILES_CSWcollectd-plugin-rrdtool += $(call pkgfiles_lib,collectd/rrdcached.so)
RUNTIME_DEP_PKGS_CSWcollectd-plugin-rrdtool += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-rrdtool += CSWlibrrd-th4

PACKAGES += CSWcollectd-plugin-snmp
SPKG_DESC_CSWcollectd-plugin-snmp = CollectD Plugin for NetSNMP
PKGFILES_CSWcollectd-plugin-snmp += $(call pkgfiles_lib,collectd/snmp.so)
PKGFILES_CSWcollectd-plugin-snmp += $(mandir)/man5/collectd-snmp.5
RUNTIME_DEP_PKGS_CSWcollectd-plugin-snmp += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-snmp += CSWlibnetsnmp30

PACKAGES += CSWcollectd-plugin-xmms
SPKG_DESC_CSWcollectd-plugin-xmms = CollectD Plugin for XMMS
PKGFILES_CSWcollectd-plugin-xmms += $(call pkgfiles_lib,collectd/xmms.so)
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms += CSWlibxmms1
# This is due to a linker anomaly, these are pulled in also from libxmms.so.1
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms-sparc += CSWlibgdk1-2-0
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms-sparc += CSWlibglib1-2-0
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms-sparc += CSWlibgtk1-2-0
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms-sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms += $(RUNTIME_DEP_PKGS_CSWcollectd-plugin-xmms-$(GARCH))
# No 64 bit XMMS yet
CHECKPKG_OVERRIDES_CSWcollectd-plugin-xmms += 64-bit-binaries-missing

PACKAGES += CSWcollectd-plugins-all
SPKG_DESC_CSWcollectd-plugins-all = CollectD Metapackage that pulls in all plugins
PKGFILES_CSWcollectd-plugins-all = EMPTY
ARCHALL_CSWcollectd-plugins-all = 1
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-dbi
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-gmond
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-mysql
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-postgresql
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-python
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-rrdtool
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-snmp
RUNTIME_DEP_PKGS_CSWcollectd-plugins-all += CSWcollectd-plugin-xmms
# These are all sort of surplus as this is a meta package
CHECKPKG_OVERRIDES_CSWcollectd-plugins-all += surplus-dependency

INITSMF = $(sysconfdir)/init\.d/cswcollectd

PRESERVECONF += $(sysconfdir)/collectd.conf

include gar/category.mk

post-install-modulated:
	mv $(DESTDIR)/opt/csw/man $(DESTDIR)$(mandir)
	grm -f $(DESTDIR)/opt/csw/lib/perl/5.10.1/perllocal.pod
	ginstall -D -m 0755 $(WORKDIR)/cswcollectd $(DESTDIR)$(sysconfdir)/init.d/cswcollectd
	$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-ds-base
VERSION = 1.3.2.13
GARTYPE = v2

DESCRIPTION = The enterprise-class Open Source LDAP server
define BLURB
The enterprise-class Open Source LDAP server for Linux. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

BUNDLE = 389-ds

MASTER_SITES = http://port389.org/sources/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSW389-ds-base.postinstall
DISTFILES += CSW389-ds-base.postremove

# BUILD64	= 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

LICENSE = LICENSE

GARCOMPILER = SOS12U3

PATCHFILES += 0005-add-standard-path.patch
PATCHFILES += 0006-replace-SV-sh-with-Posix-sh.patch
PATCHFILES += 0005-smf-autoenable-no.patch
PATCHFILES += 0005-add-var-run-create-initconfig.in.patch
# until Red Hat Bugzilla Bug 773617 is open do it yourself
# PATCHFILES += 0006-add-i386-platform-in-configure.ac.patch
PATCHFILES += 0007-fixup-Makefile.am.patch
# PATCHFILES += 0007-fixup-plugin_syntax.c.patch
PATCHFILES += 0008-mntent-daemon.c.patch
# PATCHFILES += 0009-mozldap-pw.c.patch
# PATCHFILES += 0010-mntent-config.ac.patch
# PATCHFILES += 0011-Makefile.am.patch
# PATCHFILES += 0009-fix-for-550-memberuid-not-created.patch
# PATCHFILES += 0012-fix-for-47327.patch
PATCHFILES += 0013-use-posix-threads-configure.ac.patch
PATCHFILES += 0014-ldap-include-Makefile.am.patch


BUILD_DEP_PKGS += CSWautoconf
BUILD_DEP_PKGS += CSWautomake
BUILD_DEP_PKGS += CSWbdb48devel
BUILD_DEP_PKGS += CSWnspr-dev
BUILD_DEP_PKGS += CSWlibnss-dev
BUILD_DEP_PKGS += CSWnetsnmp-dev
BUILD_DEP_PKGS += CSWmozldap-dev
BUILD_DEP_PKGS += CSWmozldap-tools
BUILD_DEP_PKGS += CSWsasl-dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibsvrcore0-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev

INITSMF = /etc/opt/csw/init.d/dirsrv
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWperl
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWpython
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibsvrcore0
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnspr4
# RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnetsnmpmibs25
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnetsnmp25
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnetsnmpagent25
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibplds4
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnss3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibplc4
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWbdb48
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWpm-mozldap
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibssl3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibfreebl3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnssdbm3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibpcre1
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWpm-netaddr-ip
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSW389-ds-base_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSW389-ds-base_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSW389-ds-base_sparc += CSWlibicudata52
RUNTIME_DEP_PKGS_CSW389-ds-base += $(RUNTIME_DEP_PKGS_CSW389-ds-base_$(GARCH))


CHECKPKG_OVERRIDES_CSW389-ds-base += file-with-bad-content|/usr/share|root/opt/csw/lib/dirsrv/perl/DSUpdate.pm
CHECKPKG_OVERRIDES_CSW389-ds-base += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSW389-ds-base += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/dirsrv-snmp|class=none
# is needed for setup scripts!
CHECKPKG_OVERRIDES_CSW389-ds-base += surplus-dependency|CSWpm-mozldap
CHECKPKG_OVERRIDES_CSW389-ds-base += surplus-dependency|CSWpm-netaddr-ip
# will load via dlopen()
CHECKPKG_OVERRIDES_CSW389-ds-base += surplus-dependency|CSWlibfreebl3
CHECKPKG_OVERRIDES_CSW389-ds-base += surplus-dependency|CSWlibnssdbm3


EXTRA_LIB = /opt/csw/bdb48/lib
# remove -I/opt/csw/include
CPPFLAGS = 
EXTRA_LINKER_FLAGS = -xnorunpath -norunpath

GARFLAVOR = DBG

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --with-ldapsdk-inc=$(includedir)/dirsrv 
# CONFIGURE_ARGS += --with-ldapsdk-lib=$(libdir)
## CONFIGURE_ARGS += --with-ldapsdk-bin=$(abspath $(prefix)/dirsrv/bin/$(MM_BINDIR))
# CONFIGURE_ARGS += --with-ldapsdk-bin=$(bindir)
CONFIGURE_ARGS += --with-openldap=$(prefix)
CONFIGURE_ARGS += --with-openldap-inc=$(includedir)
CONFIGURE_ARGS += --with-db-inc=$(prefix)/bdb48/include 
CONFIGURE_ARGS += --with-db-lib=$(abspath $(prefix)/bdb48/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --with-icu-inc=$(includedir)
CONFIGURE_ARGS += --with-icu-lib=$(libdir)
CONFIGURE_ARGS += --with-icu-bin=$(bindir)
CONFIGURE_ARGS += --with-netsnmp-inc=$(includedir)
CONFIGURE_ARGS += --with-netsnmp-lib=$(libdir)
CONFIGURE_ARGS += --with-sasl-inc=$(includedir)/sasl 
CONFIGURE_ARGS += --with-sasl-lib=$(libdir)
CONFIGURE_ARGS += --with-nss-lib=$(libdir)
CONFIGURE_ARGS += --with-nss-inc=$(includedir)/nss 
CONFIGURE_ARGS += --with-nspr-lib=$(libdir)
CONFIGURE_ARGS += --with-nspr-inc=$(includedir)/nspr
CONFIGURE_ARGS_DBG += --enable-debug

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	cd $(WORKSRC) && autoheader
	@$(MAKECOOKIE)

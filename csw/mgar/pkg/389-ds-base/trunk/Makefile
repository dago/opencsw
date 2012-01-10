# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-ds-base
VERSION = 1.2.9.9
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = The enterprise-class Open Source LDAP server
define BLURB
The enterprise-class Open Source LDAP server for Linux. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

MASTER_SITES = http://port389.org/sources
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# BUILD64	= 1

PATCHFILES += 0005-add-standard-path.patch
PATCHFILES += 0006-replace-SV-sh-with-Posix-sh.patch
PATCHFILES += 0007-create-var-run-dirsrv.patch

RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibssldap60
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibprldap60
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWperl
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWpython
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWsasl
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibldif60
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibsvrcore0
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnspr4
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibicu46
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibldap60
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWnetsnmp
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibplds4
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWkrb5lib
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibpcre0
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibnss3
RUNTIME_DEP_PKGS_CSW389-ds-base += CSWlibplc4
CHECKPKG_OVERRIDES_CSW389-ds-base += file-with-bad-content|/usr/share|root/opt/csw/lib/dirsrv/perl/DSUpdate.pm
CHECKPKG_OVERRIDES_CSW389-ds-base += file-with-bad-content|/usr/share|root/opt/csw/share/dirsrv/updates/exampleupdate.ldif
CHECKPKG_OVERRIDES_CSW389-ds-base += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/dbgen.pl.1
CHECKPKG_OVERRIDES_CSW389-ds-base += license-missing|/opt/csw/share/doc/389_ds_base/license
CHECKPKG_OVERRIDES_CSW389-ds-base += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/dirsrv|class=none
CHECKPKG_OVERRIDES_CSW389-ds-base += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/dirsrv-snmp|class=none
CHECKPKG_OVERRIDES_CSW389-ds-base += soname-not-found|libdb-4.8.so|is|needed|by|opt/csw/lib/dirsrv/plugins/libback-ldbm.so
CHECKPKG_OVERRIDES_CSW389-ds-base += soname-not-found|libdb-4.8.so|is|needed|by|opt/csw/bin/dbscan-bin
CHECKPKG_OVERRIDES_CSW389-ds-base += soname-not-found|libdb-4.8.so|is|needed|by|opt/csw/lib/dirsrv/plugins/libreplication-plugin.so

# GARCOMPILER = SOS12U2

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS_OPT += --with-ldapsdk-inc=/opt/csw/include/dirsrv 
CONFIGURE_ARGS_OPT += --with-ldapsdk-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-ldapsdk-bin=/opt/csw/dirsrv/bin 
CONFIGURE_ARGS_OPT += --with-db-inc=/opt/csw/bdb48/include 
CONFIGURE_ARGS_OPT += --with-db-lib=/opt/csw/bdb48/lib
CONFIGURE_ARGS_OPT += --with-icu-inc=/opt/csw/include 
CONFIGURE_ARGS_OPT += --with-icu-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-icu-bin=/opt/csw/bin 
CONFIGURE_ARGS_OPT += --with-netsnmp-inc=/opt/csw/include 
CONFIGURE_ARGS_OPT += --with-netsnmp-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-sasl-inc=/opt/csw/include/sasl 
CONFIGURE_ARGS_OPT += --with-sasl-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-nss-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-nss-inc=/opt/csw/include/nss 
CONFIGURE_ARGS_OPT += --with-nspr-lib=/opt/csw/lib
CONFIGURE_ARGS_OPT += --with-nspr-inc=/opt/csw/include/nspr
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)

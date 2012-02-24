# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-dsgw
VERSION = 1.1.9
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Directory Server Gateway web apps
define BLURB
The enterprise-class Open Source LDAP server for Linux. It is hardened by real-world use, is full-featured, supports multi-master replication, and already handles many of the largest LDAP deployments in the world. The 389 Directory Server can be downloaded for free and set up in less than an hour using the graphical console.
endef

MASTER_SITES = http://port389.org/sources
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# BUILD64	= 1
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

LICENSE = LICENSE

GARCOMPILER = SOS12U2
EXTRA_LIB = /opt/csw/bdb48/lib
# remove -I/opt/csw/include
CPPFLAGS = 
EXTRA_LINKER_FLAGS = -xnorunpath -norunpath

RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibprldap60
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibldif60
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibicudata48
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibadmsslutil0
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibplc4
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibnspr4
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibldap60
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibadminutil0
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibnss3
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibplds4
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibssldap60
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibsoftokn3
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibsmime3
RUNTIME_DEP_PKGS_CSW389-dsgw += CSWlibssl3
CHECKPKG_OVERRIDES_CSW389-dsgw += file-with-bad-content|/usr/local|root/opt/csw/share/dirsrv/manual/en/dsgw/attribut.htm

PATCHFILES += 0001-change-include-path-preferences-in-Makefile.am.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ldapsdk-inc=/opt/csw/include/dirsrv 
CONFIGURE_ARGS += --with-ldapsdk-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ldapsdk-bin=/opt/csw/dirsrv/bin 
CONFIGURE_ARGS += --with-icu-inc=/opt/csw/include 
CONFIGURE_ARGS += --with-icu-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-icu-bin=/opt/csw/bin 
CONFIGURE_ARGS += --with-sasl-inc=/opt/csw/include/sasl 
CONFIGURE_ARGS += --with-sasl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-nspr-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-nspr-inc=/opt/csw/include/nspr
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	cd $(WORKSRC) && autoheader
	@$(MAKECOOKIE)

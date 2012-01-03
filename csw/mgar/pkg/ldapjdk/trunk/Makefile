# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ldapsdk_java
VERSION = 20020819
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = 389 Directory Server - Management Console
define BLURB
A Java based remote management console used for managing 389
Administration Server and 389 Directory Server.
endef

# MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/directory/java-sdk
MASTER_SITES = http://www-archive.mozilla.org/directory
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWldapsdk
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386


ARCHALL = 1

CATALOGNAME_CSWldapjdk = ldapjdk

WORKSRC = $(WORKDIR)
DISTDIR = mozilla/directory/java-sdk
LICENSE = COPYING
# LICENSE = $(WORKDIR)/$(DISTDIR)/relnotes.htm

JAVA_HOME = /usr/j2sdk1.4.2_17

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWldapsdk += pkginfo-description-not-starting-with-uppercase|389|Directory|Server|-|Management|Console

include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTDIR)/dist/packages/$(CATALOGNAME_CSWldapjdk).jar $(DESTDIR)$(datadir)/java
	@$(MAKECOOKIE)

build-custom:
	@( cd $(WORKSRC)/$(DISTDIR); \
	  JAVA_HOME=$(JAVA_HOME) gmake -f ldap.mk MOZ_SRC=. JAVA_VERSION=1.4 ; \
	  JAVA_HOME=$(JAVA_HOME) gmake -f ldap.mk basepackage )
	@$(MAKECOOKIE)

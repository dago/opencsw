# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ldapsdk_java
VERSION = 20020819
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = Mozilla LDAP SDK for Java
define BLURB
The source code for the Directory SDK for Java consists of the Java classes that implement the LDAP API. These include classes and methods that can establish sessions with LDAP servers, create and send LDAP requests to the servers, and retrieve responses from the servers. The SDK also includes classes for getting and editing schema information for the LDAP server.

In the LDAP protocol, requests and responses are encoded using the Basic Encoding Rules (BER). The SDK source code include classes for encoding and decoding data, according to these rules.
endef

# MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/directory/java-sdk
MASTER_SITES = http://www-archive.mozilla.org/directory
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWldapjdk
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

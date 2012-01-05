# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = idm-console-framework
VERSION = 1.1.7
MAJOR_VERSION = 1.1
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = 389 Directory Server - Management Console Framework
define BLURB
A Java based remote management console used for managing 389
Administration Server and 389 Directory Server.
endef

MASTER_SITES = http://port389.org/sources
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWidmconsolebase
# RUNTIME_DEP_PKGS = CSWldapjdk CSWjss4

ARCHALL = 1

CATALOGNAME_CSWidm-console-base = idm-console-base

LICENSE = LICENSE

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-base-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-mcc-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-mcc-$(VERSION)_en.jar $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-nmclf-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-nmclf-$(VERSION)_en.jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s idm-console-base-$(VERSION).jar idm-console-base-$(MAJOR_VERSION).jar ; \
	   ln -s idm-console-base-$(VERSION).jar idm-console-base.jar ; \
	   ln -s idm-console-mcc-$(VERSION).jar idm-console-mcc-$(MAJOR_VERSION).jar ; \
	   ln -s idm-console-mcc-$(VERSION).jar idm-console-mcc.jar ; \
	   ln -s idm-console-mcc-$(VERSION)_en.jar idm-console-mcc-$(MAJOR_VERSION)_en.jar ; \
	   ln -s idm-console-mcc-$(VERSION)_en.jar idm-console-mcc_en.jar ; \
	   ln -s idm-console-nmclf-$(VERSION).jar idm-console-nmclf-$(MAJOR_VERSION).jar ; \
	   ln -s idm-console-nmclf-$(VERSION).jar idm-console-nmclf.jar ; \
	   ln -s idm-console-nmclf-$(VERSION)_en.jar idm-console-nmclf-$(MAJOR_VERSION)_en.jar ; \
	   ln -s idm-console-nmclf-$(VERSION)_en.jar idm-console-nmclf_en.jar )
	@$(MAKECOOKIE)

build-custom:
	@( cd $(WORKSRC)/$(DISTNAME); \
	  pwd; \
	  ant -Dbuilt.dir=`pwd`/built -Dldapjdk.local.location=/opt/csw/share/java -Djss.local.location=/opt/csw/share/java )
	@$(MAKECOOKIE)

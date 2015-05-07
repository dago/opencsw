# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = idm-console-framework
VERSION = 1.1.9
MAJOR_VERSION = 1.1
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = 389 Directory Server - Management Console Framework
define BLURB
A Java based remote management console used for managing 389
Administration Server and 389 Directory Server.
endef

MASTER_SITES = http://www.port389.org/binaries/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

BUNDLE = 389-ds

PACKAGES = CSWidm-console-base
# RUNTIME_DEP_PKGS = CSWldapjdk CSWjss4
DEP_PKGS = CSWldapjdk CSWjss4

ARCHALL = 1
PACKAGING_PLATFORMS = solaris10-sparc

CATALOGNAME_CSWidm-console-base = idm_console_base

LICENSE = LICENSE

WORKSRC = $(WORKDIR)
EXTRAJARSPATH = /opt/csw/share/java
# EXTRAJARSPATH = /home/cgrzemba/java


CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWidm-console-base += pkginfo-description-not-starting-with-uppercase|389|Directory|Server|-|Management|Console|Framework

include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-base.jar $(DESTDIR)$(datadir)/java/
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-mcc.jar $(DESTDIR)$(datadir)/java/
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-mcc_en.jar $(DESTDIR)$(datadir)/java/
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-nmclf.jar $(DESTDIR)$(datadir)/java/
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/release/jars/idm-console-nmclf_en.jar $(DESTDIR)$(datadir)/java/
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s idm-console-base-$(VERSION).jar idm-console-base-$(MAJOR_VERSION).jar ; \
	   ln -s idm-console-base.jar idm-console-base-$(VERSION).jar ; \
	   ln -s idm-console-mcc.jar idm-console-mcc-$(VERSION).jar ; \
	   ln -s idm-console-mcc_en.jar idm-console-mcc-$(VERSION)_en.jar ; \
	   ln -s idm-console-nmclf.jar idm-console-nmclf-$(VERSION).jar ; \
	   ln -s idm-console-nmclf_en.jar idm-console-nmclf-$(VERSION)_en.jar )
	@$(MAKECOOKIE)

build-custom:
	@( cd $(WORKSRC)/$(DISTNAME); \
	  pwd; \
	  ant -Dbuilt.dir=`pwd`/built -Dldapjdk.local.location=$(EXTRAJARSPATH) -Djss.local.location=$(EXTRAJARSPATH) )
	@$(MAKECOOKIE)

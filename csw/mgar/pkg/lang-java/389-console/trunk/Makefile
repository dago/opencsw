# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-console
VERSION = 1.1.7
MAJOR_VERSION = 1.1
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = 389 Directory Server - Management Console Client
define BLURB
This is the client component which have to installed on an administration client
A Java based remote management console used for managing 389
Administration Server and 389 Directory Server.
endef

MASTER_SITES = http://port389.org/source
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSW389-console
# RUNTIME_DEP_PKGS = CSWidm-console-base CSWldapjdk CSWjss4
DEP_PKGS = CSWidm-console-base CSWldapjdk CSWjss4

ARCHALL = 1
PACKAGING_PLATFORMS = solaris10-sparc

CATALOGNAME_CSW389-console = 389_console

LICENSE = LICENSE

WORKSRC = $(WORKDIR)
EXTRAJARSPATH = /opt/csw/share/java
# EXTRAJARSPATH = /home/cgrzemba/java

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSW389-console += unidentified-dependency|CSWidm-console-base
CHECKPKG_OVERRIDES_CSW389-console += surplus-dependency|CSWidm-console-base
CHECKPKG_OVERRIDES_CSW389-console += surplus-dependency|CSWldapjdk
CHECKPKG_OVERRIDES_CSW389-console += surplus-dependency|CSWjss4
# CHECKPKG_OVERRIDES_CSW389-console += pkginfo-opencsw-repository-uncommitted
CHECKPKG_OVERRIDES_CSW389-console += pkginfo-description-not-starting-with-uppercase|389|Directory|Server|-|Management|Console|Client


include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/java
	@ginstall -d $(DESTDIR)$(bindir)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/$(NAME)-$(VERSION)_en.jar $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/389-console $(DESTDIR)$(bindir)
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION)_en.jar $(NAME)-$(MAJOR_VERSION)_en.jar ; \
	   ln -s $(NAME)-$(VERSION)_en.jar $(NAME)_en.jar )
	@$(MAKECOOKIE)

build-custom:
	@( cd $(WORKSRC)/$(DISTNAME); \
	  pwd; \
	  ant -Dbuilt.dir=`pwd`/built -Dldapjdk.local.location=$(EXTRAJARSPATH) -Djss.local.location=$(EXTRAJARSPATH) -Dconsole.local.location=$(EXTRAJARSPATH) )
	@$(MAKECOOKIE)

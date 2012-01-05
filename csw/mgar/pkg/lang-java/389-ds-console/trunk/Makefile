# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-ds-console
SHORTNAME = 389-ds
VERSION = 1.2.6
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = 389 Directory Server - Management Console
define BLURB
A Java based remote management console used for managing 389
Administration Server and 389 Directory Server.
endef

MASTER_SITES = http://port389/sources
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSW389-ds-console
RUNTIME_DEP_PKGS = CSWidm-console-base CSWldapjdk CSWjss4

ARCHALL = 1

CATALOGNAME_CSW389-ds-console = 389-ds-console

LICENSE = LICENSE

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/dirsrv/html/java
	@ginstall -d $(DESTDIR)$(datadir)/dirsrv/manual/en/admin/help
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/package/$(SHORTNAME)* $(DESTDIR)$(datadir)/dirsrv/html/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/help/en/*.html $(DESTDIR)$(datadir)/dirsrv/manual/en/admin
	@gcp -fp $(WORKSRC)/$(DISTNAME)/help/en/tokens.map $(DESTDIR)$(datadir)/dirsrv/manual/en/admin
	@gcp -fp $(WORKSRC)/$(DISTNAME)/help/en/help/*.html $(DESTDIR)$(datadir)/dirsrv/manual/en/admin/help
	@( cd $(DESTDIR)$(datadir)/dirsrv/html/java ; \
	   ln -s $(SHORTNAME)-$(VERSION).jar $(SHORTNAME)-$(MAJOR_VERSION).jar ; \
	   ln -s $(SHORTNAME)-$(VERSION).jar $(SHORTNAME).jar ; \
	   ln -s $(SHORTNAME)-$(VERSION)_en.jar $(SHORTNAME)-$(MAJOR_VERSION)_en.jar ; \
	   ln -s $(SHORTNAME)-$(VERSION)_en.jar $(SHORTNAME)_en.jar )
	@$(MAKECOOKIE)

build-custom:
	@( cd $(WORKSRC)/$(DISTNAME); \
	  ant -Dbuilt.dir=`pwd`/built -Dconsole.location=/opt/csw/share/java )
	@$(MAKECOOKIE)

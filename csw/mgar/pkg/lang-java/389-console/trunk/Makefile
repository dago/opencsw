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

MASTER_SITES = http://port389/source
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSW389console
RUNTIME_DEP_PKGS = CSWidm-console-base CSWldapjdk CSWjss4

ARCHALL = 1

CATALOGNAME_CSW389console = 389-console

LICENSE = LICENSE

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

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
	  ant -Dbuilt.dir=`pwd`/built -Dldapjdk.local.location=/opt/csw/share/java -Djss.local.location=/opt/csw/share/java -Dconsole.local.location=/opt/csw/share/java )
	@$(MAKECOOKIE)

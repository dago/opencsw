# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jenkins
VERSION = 1.515
GARTYPE = v2

DESCRIPTION = An extendable open source continuous integration server

MASTER_SITES += http://mirrors.jenkins-ci.org/war/$(VERSION)/
DISTFILES += jenkins.war
DISTFILES += COPYING

PACKAGES += CSWjenkins
SPKG_DESC_CSWjenkins = An extendable open source continuous integration server
# PKGFILES is catchall
ARCHALL_CSWjenkins = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(sharedstatedir)/webapps
	ginstall -m 0644 $(WORKDIR)/jenkins.war $(DESTDIR)$(sharedstatedir)/webapps
	@$(MAKECOOKIE)

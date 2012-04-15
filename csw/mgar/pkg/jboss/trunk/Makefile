# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jboss
VERSION = 7.1.1.Final
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = JBoss Application Server
define BLURB
 JBoss Application Server
endef

JBOSS_MAJMIN = $(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}')

MASTER_SITES = http://download.jboss.org/jbossas/$(JBOSS_MAJMIN)/jboss-as-$(VERSION)/
DISTNAME = jboss-as-$(VERSION)

DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS      = none
INSTALL_SCRIPTS   = jboss
prefix            = /

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

install-jboss:
	@echo "Installing into $(DESTDIR)"
	@$(MAKECOOKIE)

include gar/category.mk


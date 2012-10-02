# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = qpid
VERSION = 0.18
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Open Source AMQP Messaging

#MASTER_SITES += http://www.apache.org/dyn/closer.cgi/$(NAME)/$(VERSION)/
MASTER_SITES += http://apache.openmirror.de/$(NAME)/$(VERSION)/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://qpid.apache.org
LICENSE = python/LICENSE.txt

PACKAGES += CSWpy-qpid
SPKG_DESC_CSWmypkg = Open source AMQP messaging
# PKGFILES is catchall
ARCHALL_CSWpy-qpid = 1

WORKSRC = $(WORKDIR)/$(DISTNAME)/python

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk


# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = apache-cassandra
VERSION = 1.2.4
GARTYPE = v2

DESCRIPTION = NoSQL database

MASTER_SITES = http://ftp.heanet.ie/mirrors/www.apache.org/dist/cassandra/$(VERSION)/
DISTNAME = $(NAME)-$(VERSION)-src
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = foo

JAVA_HOME = /usr/j2se
ANT_HOME = /opt/csw

EXTRA_BUILD_EXPORTS = JAVA_HOME ANT_HOME

include gar/category.mk

build-custom:
	(cd $(WORKSRC); \
		$(BUILD_ENV) \
		/opt/csw/share/java/ant/bin/ant -autoproxy)
	false

PATH := $(ANT_HOME)/bin:$(PATH)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# Current problem: ant is unable to download dependencies. I tried to give it
# proxy setting in various ways, but nothing seems to work.
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

# http://docs.oracle.com/javase/6/docs/technotes/guides/net/proxies.html
proxy_host=web.bo.opencsw.org
proxy_host=proxy

JAVA_HOME = /usr/jdk1.6.0_20
ANT_HOME = /opt/csw
ANT_OPTS = -Dhttp.proxyHost=$(proxy_host) -Dhttp.proxyPort=3128
ANT_OPTS += -Dhttps.proxyHost=$(proxy_host) -Dhttps.proxyPort=3128

EXTRA_BUILD_EXPORTS = JAVA_HOME ANT_HOME ANT_OPTS http_proxy


include gar/category.mk

build-custom:
	(cd $(WORKSRC); \
		$(BUILD_ENV) \
		/opt/csw/share/java/ant/bin/ant --execdebug -autoproxy)
	false

PATH := $(ANT_HOME)/bin:$(PATH)

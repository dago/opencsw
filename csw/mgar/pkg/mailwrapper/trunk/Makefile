# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mailwrapper
VERSION = 1.0
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Run substitute program
define BLURB
  Run substitute program
endef

LICENSE_TEXT = BSD license

MASTER_SITES = http://sk.freebsd.org/pub/local/distfiles/
DISTNAME = $(NAME)-opencsw-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# No configure script
CONFIGURE_SCRIPTS=
SKIPTEST=1
ENABLE_CHECK=0

PRESERVECONF += $(sysconfdir)/mailer.conf
SAMPLECONF += $(sysconfdir)/mailer.conf

include gar/category.mk


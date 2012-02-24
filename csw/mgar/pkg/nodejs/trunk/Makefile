# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = nodejs
VERSION = 0.6.7
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Node.js JavaScript interpreter
define BLURB
endef

MASTER_SITES = http://nodejs.org/dist/v$(VERSION)/
DISTNAME = node-v$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --openssl-includes=$(includedir)
CONFIGURE_ARGS += --openssl-libpath=$(libdir)

#CONFIGURE_SCRIPTS = custom
TEST_TARGET = check

EXTRA_CONFIGURE_EXPORTS += PWD
CONFIGURE_ENV_PWD = $(abspath $(WORKSRC))

include gar/category.mk

configure-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(CONFIGURE_ENV) PWD=$(abspath $(WORKSRC)) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

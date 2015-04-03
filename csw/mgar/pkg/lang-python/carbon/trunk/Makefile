# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = carbon
VERSION = 0.9.13
CATEGORIES = python

DESCRIPTION = Backend data caching and persistence daemon for Graphite

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWpy-carbon
SPKG_DESC_CSWpy-carbon = Backend data caching and persistence daemon for Graphite
# PKGFILES is catchall
ARCHALL_CSWpy-carbon = 1

EXTRA_INSTALL_ARGS += --install-data=$(localstatedir)/graphite

# There is no testsuite
TEST_SCRIPTS =

CONFIG_FILES += aggregation-rules.conf
CONFIG_FILES += blacklist.conf
CONFIG_FILES += carbon.amqp.conf
CONFIG_FILES += carbon.conf
CONFIG_FILES += relay-rules.conf
CONFIG_FILES += rewrite-rules.conf
CONFIG_FILES += storage-aggregation.conf
CONFIG_FILES += storage-schemas.conf
CONFIG_FILES += whitelist.conf

PRESERVECONF += $(foreach F,$(CONFIG_FILES),$(localstatedir)/graphite/conf/$F)

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)

post-install:
	cd $(DESTDIR)$(localstatedir)/graphite/conf; $(foreach F,$(CONFIG_FILES),mv $F.example $F.CSW;)
	@$(MAKECOOKIE)

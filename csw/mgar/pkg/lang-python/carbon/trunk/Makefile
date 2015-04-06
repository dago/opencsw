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

CONFDIR = $(sysconfdir)/graphite
STORAGEDIR = $(localstatedir)/graphite

EXTRA_INSTALL_ARGS += --install-data=$(CONFDIR)

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

PRESERVECONF += $(foreach C,$(CONFIG_FILES),$(CONFDIR)/conf/$C)

#   GRAPHITE_ROOT        - Root directory of the graphite installation.
#                          Defaults to ../
#   GRAPHITE_CONF_DIR    - Configuration directory (where this file lives).
#                          Defaults to $GRAPHITE_ROOT/conf/
#   GRAPHITE_STORAGE_DIR - Storage directory for whipser/rrd/log/pid files.
#                          Defaults to $GRAPHITE_ROOT/storage/
#
# To change other directory paths, add settings to this file. The following
# configuration variables are available with these default values:
#
#   STORAGE_DIR    = $GRAPHITE_STORAGE_DIR
#   LOCAL_DATA_DIR = STORAGE_DIR/whisper/
#   WHITELISTS_DIR = STORAGE_DIR/lists/
#   CONF_DIR       = STORAGE_DIR/conf/
#   LOG_DIR        = STORAGE_DIR/log/
#   PID_DIR        = STORAGE_DIR/

REINPLACEMENTS += loc
REINPLACE_MATCH_loc = \#LOCAL_DATA_DIR.*
REINPLACE_WITH_loc = GRAPHITE_ROOT = $(prefix)\nGRAPHITE_CONF_DIR = $(CONFDIR)/conf\nGRAPHITE_STORAGE_DIR = $(STORAGEDIR)/storage\nPID_DIR = /var/run
REINPLACE_FILES_loc += conf/carbon.conf.example

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)

post-install:
	cd $(DESTDIR)$(CONFDIR)/conf; $(foreach F,$(CONFIG_FILES),mv $F.example $F.CSW;)
	ginstall -d -m 0755 $(DESTDIR)$(STORAGEDIR)
	mv $(DESTDIR)$(CONFDIR)/storage $(DESTDIR)$(STORAGEDIR)/storage
	@$(MAKECOOKIE)

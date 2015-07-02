# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = carbon
VERSION = 0.9.13
CATEGORIES = python

DESCRIPTION = Backend data caching and persistence daemon for Graphite

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
MANIFESTS += cswcarbon-aggregator.xml
MANIFESTS += cswcarbon-cache.xml
MANIFESTS += cswcarbon-relay.xml
DISTFILES += $(MANIFESTS)

# Apply patch until this is fixed:
#   https://github.com/graphite-project/carbon/issues/364
# Patch taken from
#   https://github.com/graphite-project/carbon/commit/2cc77752383288c27c4623a659cd0a76ef95b5a9
PATCHFILES += 0001-Fix-for-351.patch

PACKAGES += CSWpy-carbon
SPKG_DESC_CSWpy-carbon = Backend data caching and persistence daemon for Graphite
# PKGFILES is catchall
ARCHALL_CSWpy-carbon = 1
# The binaries like carbon-cache.py need this
RUNTIME_DEP_PKGS_CSWpy-carbon += CSWpython27
# From setup.py
RUNTIME_DEP_PKGS_CSWpy-carbon += CSWpy-twisted
RUNTIME_DEP_PKGS_CSWpy-carbon += CSWpy-txamqp
CHECKPKG_OVERRIDES_CSWpy-carbon += surplus-dependency|CSWpython27
CHECKPKG_OVERRIDES_CSWpy-carbon += surplus-dependency|CSWpy-twisted
CHECKPKG_OVERRIDES_CSWpy-carbon += surplus-dependency|CSWpy-txamqp

# This is for the SMF DTD
CHECKPKG_OVERRIDES_CSWpy-carbon += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswcarbon-aggregator.xml
CHECKPKG_OVERRIDES_CSWpy-carbon += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswcarbon-cache.xml
CHECKPKG_OVERRIDES_CSWpy-carbon += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswcarbon-relay.xml

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

PRESERVECONF += $(foreach C,$(CONFIG_FILES),$(CONFDIR)/$C)

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
REINPLACE_WITH_loc = GRAPHITE_ROOT = $(prefix)\nGRAPHITE_CONF_DIR = $(CONFDIR)\nGRAPHITE_STORAGE_DIR = $(STORAGEDIR)\nPID_DIR = /var/run
REINPLACE_FILES_loc += conf/carbon.conf.example

# This is only useful on Linux and causes warning on Solaris
REINPLACEMENTS += nofalloc
REINPLACE_MATCH_nofalloc = WHISPER_FALLOCATE_CREATE = .*
REINPLACE_WITH_nofalloc = WHISPER_FALLOCATE_CREATE = False
REINPLACE_FILES_nofalloc += conf/carbon.conf.example

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = join\(graphite_root, "conf"\)
REINPLACE_WITH_conf = "$(CONFDIR)"
REINPLACE_FILES_conf += lib/carbon/conf.py

REINPLACEMENTS += stor
REINPLACE_MATCH_stor = join\(graphite_root, "storage"\)
REINPLACE_WITH_stor = "$(STORAGEDIR)"
REINPLACE_FILES_stor += lib/carbon/conf.py

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += $(foreach F,$(MANIFESTS),/var/opt/csw/svc/manifest/$F)
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)

post-install:
	cd $(DESTDIR)$(CONFDIR)/conf; $(foreach F,$(CONFIG_FILES),mv $F.example $(DESTDIR)$(CONFDIR)/$F.CSW;)
	rmdir $(DESTDIR)$(CONFDIR)/conf
	ginstall -d -m 0755 $(DESTDIR)$(STORAGEDIR)
	mv $(DESTDIR)$(CONFDIR)/storage/* $(DESTDIR)$(STORAGEDIR)
	rmdir $(DESTDIR)$(CONFDIR)/storage
	$(foreach F,$(MANIFESTS),ginstall -D -m 0644 $(WORKDIR)/$F $(DESTDIR)/var/opt/csw/svc/manifest/$F;)
	@# Fix binary names not to include .py
	cd $(DESTDIR)$(bindir); $(foreach F,carbon-aggregator carbon-cache carbon-client carbon-relay validate-storage-schemas,mv $F.py $F;)
	@$(MAKECOOKIE)

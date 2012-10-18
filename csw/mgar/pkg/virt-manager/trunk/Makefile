# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = virt-manager
VERSION = 0.9.3
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://virt-manager.org/download/sources/virt-manager/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = SOS12U3

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

ARCHALL_CSWvirt-manager = 1
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpython

# CONFIGURE_SCRIPTS =
# BUILD_SCRIPTS = $(WORKSRC)/setup.py
# TEST_SCRIPTS =
# INSTALL_SCRIPTS = $(WORKSRC)/setup.py
# INSTALL_ARGS = --root=$(DESTDIR)

CONFIGURE_ARGS += $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

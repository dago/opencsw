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
DEP_PKGS += CSWpython

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

ARCHALL_CSWvirt-manager = 1
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-virtinst
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-curl
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-dbus

# CONFIGURE_SCRIPTS =
# BUILD_SCRIPTS = $(WORKSRC)/setup.py
# TEST_SCRIPTS =
# INSTALL_SCRIPTS = $(WORKSRC)/setup.py
# INSTALL_ARGS = --root=$(DESTDIR)

CONFIGURE_ARGS += $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

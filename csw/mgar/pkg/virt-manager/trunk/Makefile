# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = virt-manager
VERSION = 0.9.3
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION =  Virtual Machine Manager
define BLURB
  Long description
endef

MASTER_SITES = http://virt-manager.org/download/sources/virt-manager/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = SOS12U3
DEP_PKGS += CSWpython

REINPLACE_MATCH = /usr/bin/python
REINPLACE_WITH = /opt/csw/bin/python
REINPLACE_FILES += src/virt-manager.in
REINPLACE_FILES += src/virt-manager-tui.in

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

ARCHALL_CSWvirt-manager = 1
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-virtinst
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-curl
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-dbus
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-urlgrabber
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-gobject
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-gtk
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-libxml2
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-gnome
RUNTIME_DEP_PKGS_CSWvirt-manager += CSWpy-gtkvnc

# CONFIGURE_SCRIPTS =
# BUILD_SCRIPTS = $(WORKSRC)/setup.py
# TEST_SCRIPTS =
# INSTALL_SCRIPTS = $(WORKSRC)/setup.py
# INSTALL_ARGS = --root=$(DESTDIR)

CONFIGURE_ARGS += $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

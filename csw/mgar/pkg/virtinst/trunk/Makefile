# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = virtinst
VERSION = 0.600.3
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Interface for managing virtual machines
define BLURB
  virtinst is a module that helps build and install libvirt based virtual
  machines. Currently supports KVM, QEmu and Xen virtual machines. Package
  includes several command line utilities, including virt-install (build
  and install new VMs) and virt-clone (clone an existing virtual machine).
endef

MASTER_SITES = http://virt-manager.org/download/sources/virtinst/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = SOS12U3

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

# from RPM spec
# Requires: libvirt-python >= 0.2.0
# Requires: urlgrabber
# Requires: libxml2-python
# Requires: python-urlgrabber

# BuildRequires: gettext
# BuildRequires: python
BUILD_DEP_PKGS += CSWgettext
DEP_PKGS += CSWpython

PACKAGES += CSWpy-virtinst
# no file cpu_map.xml available at the moment
CHECKPKG_OVERRIDES_CSWpy-virtinst += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/virtinst/CapabilitiesParser.py


CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

# CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

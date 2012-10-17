# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = virtualbricks
VERSION = 0.6.352
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = GUI for qemu
define BLURB
  It is a GTK frontend for VDE and QEMU/KVM.
endef

MASTER_SITES = http://launchpad.net/virtualbrick/0.5-maintainance/0.6/+download/
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES = LICENSE
LICENSE = LICENSE

# PACKAGING_PLATFORMS = Solaris11-i386 # only Illumos has KVM :-o

REINPLACE_USRLOCAL += virtualbricks/gui/graphics.py
REINPLACE_USRLOCAL += setup.py

PACKAGES = CSWpy-virtualbricks
CATALOGNAME = py_virtualbricks
ARCHALL_CSWpy-virtualbricks = 1
RUNTIME_DEP_PKGS_CSWpy-virtualbricks += CSWpython

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

CHECKPKG_OVERRIDES_CSWpy-virtualbricks += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/virtualbricks/__init__.py
CHECKPKG_OVERRIDES_CSWpy-virtualbricks += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/virtualbricks/gui/graphics.py
CHECKPKG_OVERRIDES_CSWpy-virtualbricks += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/virtualbricks/gui/gui.py

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = py
TEST_SCRIPTS =
INSTALL_SCRIPTS = py

build-py:
	(cd $(WORKSRC); python setup.py build)
	@$(MAKECOOKIE)

install-py:
	(cd $(WORKDIR)/$(NAME); python setup.py install --root=$(DESTDIR) --record .filesinstalled)
	@$(MAKECOOKIE)


include gar/category.mk

WORKSRC := $(WORKDIR)/$(NAME)
PATH := /opt/csw/gnu:$(PATH)

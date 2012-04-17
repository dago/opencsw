# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = meld
VERSION = 1.5.4
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Visual diff and merge tool
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/meld/1.5/
DISTFILES  = $(DISTNAME).tar.xz

# PATCHFILES += 0001-Allow-to-use-a-different-install-utility.patch
PATCHFILES += 0001-Use-conditionals-for-installation-places.patch

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = meld
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[co]

ARCHALL_CSWmeld = 1
RUNTIME_DEP_PKGS_CSWmeld += CSWpython

CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/opt/csw/bin/meld
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/meld/paths.py
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/opt/csw/lib/meld/meld/paths.py
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/opt/csw/share/omf/meld/meld-fr.omf
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/opt/csw/share/omf/meld/meld-C.omf
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/opt/csw/share/omf/meld/meld-es.omf
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/scrollkeeper_docs
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/fr/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/fr/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/es/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/es/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/C/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWmeld += file-with-bad-content|/usr/local|root/var/opt/csw/lib/scrollkeeper/C/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWmeld += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWmeld += catalogname-does-not-start-with-py_

include gar/category.mk

install-meld:
	cd $(WORKSRC) && gmake \
		prefix=$(prefix) \
		localstatedir=$(localstatedir) \
		sysconfdir=$(sysconfdir) \
		DESTDIR=$(DESTDIR) \
		libdir_=$(libdir)/python/site-packages \
		install
	@$(MAKECOOKIE)

# msgfmt, install
PATH := /opt/csw/gnu:$(PATH)

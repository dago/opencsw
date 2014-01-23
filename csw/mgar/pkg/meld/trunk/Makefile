# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = meld
VERSION = 1.8.3
GARTYPE = v2

DESCRIPTION = Visual diff and merge tool
define BLURB
  Meld is a visual diff and merge tool targeted at developers. Meld
  helps you compare files, directories and version controlled
  projects. It provides tow- and three-way comparison of both files
  and directories and has support for many popular version control
  systems.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/meld/$(basename $(VERSION))E/sources/meld/1.5/
DISTFILES  = $(DISTNAME).tar.xz

# PATCHFILES += 0001-Allow-to-use-a-different-install-utility.patch
PATCHFILES += 0001-Use-conditionals-for-installatREINPLACEMENTS += python
REINPLACE_MATCH_python = \#!.*python.*
REINPLACE_WITH_python = \#!$(bindir)/python
REINPLACE_FILES_python += bin/meldation-places.patch

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = meld
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[co]

ARCHALL_CSWmeld = 1
RUNTIME_DEP_PKG-gtk CSWpy-gobject

CHECKPKG_OVERRIDES_CSWmeld += surplus-dependency|CSWpy-gobject
CHECKPKG_OVERRIDES_CSWmeld += surplus-dependency|CSWpy-gtkcrollkeeper_cl.xml
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
PATH := /op
# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = multiple-versions
BASE_VERSION = 0.1
VERSION = $(BASE_VERSION).0
CATEGORIES = apps
GARTYPE = v2
DESCRIPTION = Example layout that supports multiple versions of a program.
define BLURB

  This package description is an example of a layout supporting multiple
  versions of the packaged software.  It's been created for testing purposes.

endef
SPKG_SOURCEURL =

version_dependent = /lib/$(NAME)/$(BASE_VERSION)
bindir_install = $(prefix)$(version_dependent)/bin
bindir = $(prefix)$(version_dependent)/bin
sbindir_install = $(prefix)$(version_dependent)/sbin
sbindir = $(prefix)$(version_dependent)/sbin
libdir_install = $(prefix)$(version_dependent)/lib
libdir = $(prefix)$(version_dependent)/lib
localstatedir = /var$(prefix)/$(NAME)/$(BASE_VERSION)
sysconfdir = /etc$(prefix)/$(NAME)/$(BASE_VERSION)
datadir = $(prefix)/share/$(NAME)/$(BASE_VERSION)
docdir = $(prefix)/share/doc/$(NAME)-$(BASE_VERSION)
includedir = $(prefix)/include/$(NAME)/$(BASE_VERSION)
infodir = $(datadir)/info
libexecdir_install = $(prefix)/libexec/$(NAME)/$(BASE_VERSION)
lispdir = $(datadir)/emacs/site-lisp
mandir = $(datadir)/man
sharedstatedir = $(prefix)/share/$(NAME)/$(BASE_VERSION)
sourcedir = $(prefix)/src/$(NAME)/$(BASE_VERSION)

MASTER_SITES =
DISTFILES  = hello-$(VERSION).tar.gz
CATALOGNAME = multiple_versions
TEST_SCRIPTS =
WORKSRC = $(WORKDIR)/hello-$(VERSION)
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1

include gar/category.mk

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(prefix)/share/checkpkg/overrides
	echo "CSWmultiple-versions: license-missing" \
	  > $(PKGROOT)$(prefix)/share/checkpkg/overrides/$(CATALOGNAME)
	@$(MAKECOOKIE)

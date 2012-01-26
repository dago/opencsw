# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# => Installing CSWusers-and-groups-0.1,REV=2010.01.03
# pkgadd: ERROR: unable to create package object </opt/csw/share/users_and_groups>.
#     pathname does not exist
#     group name <cswgroup> not found in group table(s)
#     owner name <cswuser> not found in passwd table(s)
# ERROR: attribute verification of </opt/csw/share/users_and_groups> failed
#     group name <cswgroup> not found in group table(s)
#     owner name <cswuser> not found in passwd table(s)
# Installing class <cswusergroup> ...
# Group cswgroup has been added
# User cswuser has been added


NAME = users_and_groups
VERSION = 0.1
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = An example build adding users, groups and files owned by them
define BLURB
endef
MASTER_SITES =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = example
TEST_SCRIPTS =

MAIN_PKGNAME = CSWusers-and-groups
PACKAGES = $(MAIN_PKGNAME)
CATALOGNAME_$(MAIN_PKGNAME) = users_and_groups
USERGROUP = /etc/opt/csw/pkg/$(MAIN_PKGNAME)/cswusergroup

PROTOTYPE_MODIFIERS = example
PROTOTYPE_FILES_example = $(datadir)/$(NAME)
PROTOTYPE_USER_example = cswuser
PROTOTYPE_GROUP_example = cswgroup
PROTOTYPE_PERMS_example = 0700
PROTOTYPE_CLASS_example = ugfiles

SPKG_CLASSES = none ugfiles

include gar/category.mk

install-example:
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/$(MAIN_PKGNAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/$(MAIN_PKGNAME)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(datadir)/$(NAME)

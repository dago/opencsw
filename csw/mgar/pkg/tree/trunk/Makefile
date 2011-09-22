# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = tree
VERSION = 1.6.0
CATEGORIES = utils
DESCRIPTION = A recursive directory listing program
define BLURB
  Tree is a recursive directory listing program that produces a depth indented
  listing of files, which is colorized ala dircolors if the LS_COLORS
  environment variable is set and output is to tty. 
endef
SPKG_SOURCEURL = http://mama.indstate.edu/users/ice/tree/
MASTER_SITES  = ftp://mama.indstate.edu/linux/tree/
MASTER_SITES += http://www.sfr-fresh.com/linux/misc/
PATCHFILES += 0001-opt-csw-prefix.patch
PATCHFILES += 0002-comment-out-Linux-defaults.patch
PATCHFILES += 0003-Solaris-settings.patch
PATCHFILES += 0004-Using-GNU-install.patch
PATCHFILES += 0005-Allowing-CFLAGS-from-GAR.patch
PATCHFILES += 0006-Undefine-S_ISDOOR-on-Solaris.patch
PATCHFILES += 0007-dash-e-is-not-available-in-bin-sh.patch
DISTFILES  = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz
CONFIGURE_SCRIPTS =
SKIPTEST = 1
LICENSE = LICENSE
include gar/category.mk

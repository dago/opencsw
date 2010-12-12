# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = tree
VERSION = 1.5.3
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
PATCHFILES += solaris.patch
PATCHFILES += 0002-Allowing-CFLAGS-from-GAR.patch
DISTFILES  = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz
CONFIGURE_SCRIPTS =
SKIPTEST = 1
LICENSE = LICENSE
include gar/category.mk

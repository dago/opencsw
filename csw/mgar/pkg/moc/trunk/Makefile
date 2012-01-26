# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = moc
VERSION = 2.4.4
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Music On Console
define BLURB
endef
SPKG_SOURCEURL = http://moc.daper.net/
MASTER_SITES = ftp://ftp.daper.net/pub/soft/moc/stable/
PATCHFILES = remove-export-dynamic.patch
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LDFLAGS = -lsocket

# Doesn't compile yet.
#
# The current problem is that the configure script checks for soundcard.h and
# when it's not there, it concludes that there's no OSS.  It might be explained
# by moc never having been built on Solaris yet.

include gar/category.mk

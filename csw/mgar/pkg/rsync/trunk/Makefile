# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = rsync
GARVERSION = 3.0.7
CATEGORIES = utils
DESCRIPTION = utility which provides fast incremental file transfer
define BLURB
  rsync is an open source utility that provides fast incremental file transfer.
  rsync is freely available under the GNU General Public License and is
  currently being maintained by Wayne Davison.
endef
SPKG_SOURCEURL = http://rsync.samba.org/
MASTER_SITES   = http://samba.anu.edu.au/ftp/rsync/
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX   = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1
RUNTIME_DEP_PKGS_CSWrsync  = CSWiconv
RUNTIME_DEP_PKGS_CSWrsync += CSWlibpopt
include gar/category.mk

# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = rsync
VERSION = 3.1.0dev_fd91c3b
CATEGORIES = utils

DESCRIPTION = Utility which provides fast incremental file transfer

define BLURB
  rsync is an open source utility that provides fast incremental file transfer.
  rsync is freely available under the GNU General Public License and is
  currently being maintained by Wayne Davison.
endef

MASTER_SITES = http://samba.anu.edu.au/ftp/rsync/
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://rsync.samba.org/

RUNTIME_DEP_PKGS_CSWrsync  = CSWlibiconv2
RUNTIME_DEP_PKGS_CSWrsync += CSWlibpopt

# The location of rsyncd.conf to OpenCSW standard has been done in 3.0.8
MIGRATE_FILES = rsyncd.conf
MIGRATE_SOURCE_DIR = /etc

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-rsyncd-conf=$(sysconfdir)/rsyncd.conf
CONFIGURE_ARGS += --enable-xattr-support

include gar/category.mk

pre-configure-modulated:
	@(cd $(WORKSRC); ./support/git-set-file-times; ./prepare-source)
	@$(MAKECOOKIE)

post-install-modulated:
	perl -pi \
		-e 's,/etc/rsyncd\.conf,$(sysconfdir)/rsyncd.conf,g;' \
		$(DESTDIR)$(mandir)/man5/rsyncd.conf.5
	perl -pi \
		-e 's,/usr/local,$(prefix),g;' \
		-e 's,/etc/rsyncd.conf,$(sysconfdir)/rsyncd.conf,g;' \
		$(DESTDIR)$(mandir)/man1/rsync.1

# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = oracle
GARVERSION = 10.2.0
CATEGORIES = apps
define BLURB
endef
SPKG_SOURCEURL =
MASTER_SITES =
DISTFILES  =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = oracle
TEST_SCRIPTS =

prefix = /opt/oracle

PACKAGES = GOOGoracle
CATALOGNAME_GOOGoracle = oracle
SPKG_DESC_GOOGoracle = The Oracle database

REQUIRED_PKGS = CSWggettextrt CSWlibxext CSWunixodbc

PROTOTYPE_FILTER = awk '$$$$3 ~/\/extjob$$$$/ \
	{ $$$$4 = 3755; $$$$5 = "nobody"; $$$$6 = "nobody" } \
	{ print }'

ORACLE_HOME = $(prefix)/product/$(GARVERSION)/Db_1

include gar/category.mk

install-oracle:
	ginstall -m 755 -d $(DESTDIR)$(prefix)
	@$(MAKECOOKIE)

post-merge:
	# This takes a really long time.
	gtar -cf - -C $(prefix) . | gtar -xpf - -C $(PKGROOT)$(prefix)
	# echo foo > $(PKGROOT)$(prefix)/bar
	grm -f $(PKGROOT)$(ORACLE_HOME)/inventory/Templates/perl/lib/5.8.3/sun4-solaris-thread-multi/perllocal.pod
	grm -f $(PKGROOT)$(ORACLE_HOME)/perl/lib/5.8.3/sun4-solaris-thread-multi/perllocal.pod
	# Removing one shared library, because:
	# ERROR: Couldn't find a package providing libEntrust.so
	grm -f $(PKGROOT)$(ORACLE_HOME)/lib32/libnnzentr10.so
	# ERROR: Couldn't find a package providing libc.so.6
	grm -f $(PKGROOT)$(ORACLE_HOME)/lib/libcxa.so.3
	grm -f $(PKGROOT)$(ORACLE_HOME)/bin/rtsora32
	@$(MAKECOOKIE)

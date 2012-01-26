# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = oracle
VERSION = 10.2.0
CATEGORIES = apps
GARTYPE = v2
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

PACKAGES = CSWoracle
CATALOGNAME_CSWoracle = oracle
SPKG_DESC_CSWoracle = The Oracle database

RUNTIME_DEP_PKGS =
# Maybe CSWunixodbc, but how would it know how to locate the shared library?

PROTOTYPE_FILTER = awk '$$$$3 ~/\/extjob$$$$/ \
	{ $$$$4 = 3755; $$$$5 = "nobody"; $$$$6 = "nobody" } \
	{ print }'

ORACLE_HOME = $(prefix)/product/$(VERSION)/Db_1

include gar/category.mk

install-oracle:
	ginstall -m 755 -d $(DESTDIR)$(prefix)
	@$(MAKECOOKIE)

post-merge:
	# This takes a really long time.
	gtar -cf - -C $(prefix) . | gtar -xpf - -C $(PKGROOT)$(prefix)
	# echo foo > $(PKGROOT)$(prefix)/bar
	grm -fv $(PKGROOT)$(ORACLE_HOME)/inventory/Templates/perl/lib/5.8.3/sun4-solaris-thread-multi/perllocal.pod
	grm -fv $(PKGROOT)$(ORACLE_HOME)/perl/lib/5.8.3/sun4-solaris-thread-multi/perllocal.pod
	# Removing shared libraries, because they depend on other shared
	# libraries that aren't there.
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib32/libnnzentr10.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib/libcxa.so.3
	grm -fv $(PKGROOT)$(ORACLE_HOME)/bin/rtsora32
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib32/hsdb_inf.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib/hsdb_inf.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib32/hsdb_syb.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib/hsdb_syb.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/jre/1.4.2/lib/sparcv9/libJdbcOdbc.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/jre/1.4.2/lib/sparc/libJdbcOdbc.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/jdk/jre/lib/sparcv9/libJdbcOdbc.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/jdk/jre/lib/sparc/libJdbcOdbc.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib/libcoresh10.so
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib32/libsqora.so.10.1
	grm -fv $(PKGROOT)$(ORACLE_HOME)/lib/libsqora.so.10.1
	grm -fv $(PKGROOT)$(ORACLE_HOME)/ctx/lib/libxml4c.so.54.0
	grm -fv $(PKGROOT)$(ORACLE_HOME)/ctx/lib/xmllib.so
	@$(MAKECOOKIE)

# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = myodbc
GARVERSION = 3.51.27
PATCHLEVEL = r695
DL_NAME = mysql-connector-odbc
CATEGORIES = lib
DESCRIPTION = MySQL Connector/ODBC 3.51
define BLURB
  This provides database connectivity for mysql, best used together with unixODBC
endef
SPKG_SOURCEURL = http://dev.mysql.com/downloads/connector/odbc/3.51.html#source
MASTER_SITES  = http://mirror.trouble-free.net/mysql_mirror//Downloads/Connector-ODBC/3.51/
MASTER_SITES += ftp://mirror.anl.gov/pub/mysql//Downloads/Connector-ODBC/3.51/
MASTER_SITES += http://opensource.become.com/mysql/Downloads/Connector-ODBC/3.51/
MASTER_SITES += ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-5.0/
DISTFILES  = $(DL_NAME)-$(GARVERSION)$(PATCHLEVEL).tar.gz
DISTFILES += mysql-5.0.84.tar.gz
UFILES_REGEX = $(DL_NAME)-(\d+(?:\.\d+)*)r(\d+).tar.gz
CATALOGNAME = myodbc

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

REQUIRED_PKGS  = CSWiconv
REQUIRED_PKGS += CSWlibtoolrt
REQUIRED_PKGS += CSWmysql5rt
REQUIRED_PKGS += CSWunixodbc
REQUIRED_PKGS += CSWzlib

PREREQUISITE_PKGS  = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWmysql5devel

# The tests act weird. They require a shared library that doesn't get built at all.
TEST_SCRIPTS =
WORKSRC = $(WORKDIR)/$(DL_NAME)-$(GARVERSION)$(PATCHLEVEL)
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-unixODBC=/opt/csw --with-mysql-path=/opt/csw/mysql5 --enable-gui=no
CONFIGURE_ARGS += --with-odbc-ini=/etc/opt/csw
EXTRA_INC = $(abspath $(WORKDIR))/mysql-5.0.84/include
include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PATCHLEVEL)

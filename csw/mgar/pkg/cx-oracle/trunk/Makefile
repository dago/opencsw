# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cx-oracle
VERSION = 5.0.2
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = a Python db API conforming module for Oracle database access
define BLURB
  cx_Oracle is a Python extension module that allows access to Oracle databases
  and conforms to the Python database API specification. This module is
  currently built against Oracle 9.2.0, 10.2.0 and 11.1.0. For more information
  on the database API specification, see  here. Use the provided setup.py to
  build and install the module which makes use of the DistUtils module made
  available in Python 2.0 and up.
endef
SPKG_SOURCEURL = http://cx-oracle.sourceforge.net/
CATALOGNAME = py_cx_oracle
MASTER_SITES = $(SF_MIRRORS)
DL_NAME = cx_Oracle
DISTNAME = $(DL_NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
BUILD_DEP_PKGS = $(REQUIRED_PKGS) CSWpython-devel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
ORACLE_HOME ?= /opt/oracle/product/10.2.0/Db_1
LICENSE = LICENSE.txt
CHECKPKG_OVERRIDES_CSWcx-oracle += orphan-soname|libclntsh.so.10.1
export ORACLE_HOME
include gar/category.mk

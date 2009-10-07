# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = autoproject
GARVERSION = 0.20

CATEGORIES = apps
DESCRIPTION = creates a source package which follows the GNU programming standards
define BLURB

  autoproject interviews the user, then creates a source package for a new
  program which follows the GNU programming standards. The new package uses
  autoconf to configure itself, and automake to create the Makefile. `make
  distcheck' succeeds.

  The idea is that you execute autoproject just once when you start a new
  project. It will ask a few questions, then create a new directory and populate
  it with standard files, customized for the new project.

endef
SPKG_SOURCEURL = http://packages.debian.org/unstable/devel/autoproject
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/a/$(GARNAME)/
DISTFILES  = $(GARNAME)_$(GARVERSION).orig.tar.gz
PATCHFILES = 0001-gawk-and-ggrep.patch
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
ARCHALL = 1
REQUIRED_PKGS = CSWautomake CSWbash CSWgawk CSWggrep
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
AWK=gawk
export AWK
GREP=ggrep
export GREP
include gar/category.mk

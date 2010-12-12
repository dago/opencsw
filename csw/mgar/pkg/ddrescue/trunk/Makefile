# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = ddrescue
VERSION = 1.13
CATEGORIES = utils

DESCRIPTION = A data recovery tool
define BLURB
  GNU ddrescue is a data recovery tool. It copies data from one file or block device
  (hard disc, cdrom, etc) to another, trying hard to rescue data in case of read errors.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.lz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.lz

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += CXX="$(CXX)" CPPFLAGS="$(CPPFLAGS)" CXXFLAGS="$(CXXFLAGS)" LDFLAGS="$(LDFLAGS)"

TEST_TARGET = check

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall

include gar/category.mk

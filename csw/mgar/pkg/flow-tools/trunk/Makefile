NAME = flow-tools
VERSION = 0.68.5.1
CATEGORIES = net
DESCRIPTION = Software for collection/processing NetFlow data from Cisco/Juniper.

define BLURB

  flow-tools is library and a collection of programs used to collect,
  send, process, and generate reports from NetFlow data. The tools
  can be used together on a single server or distributed to multiple
  servers for large deployments. The flow-tools library provides an
  API for development of custom applications for NetFlow export
  versions 1,5,6 and the 14 currently defined version 8 subversions. 

endef

GARTYPE = v2

MASTER_SITES = http://flow-tools.googlecode.com/files/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

BUILD_DEP_PKGS = CSWmysql5devel CSWossldevel CSWzlib
BUILD_OVERRIDE_VARS = AM_CFLAGS

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw 
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-mysql=/opt/csw

EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

RUNTIME_DEP_PKGS_CSWflow-tools += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWflow-tools += CSWosslrt
RUNTIME_DEP_PKGS_CSWflow-tools += CSWzlib
RUNTIME_DEP_PKGS_CSWflow-tools += CSWpostgresql

include gar/category.mk


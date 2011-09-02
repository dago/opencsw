# $Id$

NAME = flow-tools
VERSION = 0.68.5.1
CATEGORIES = net
DESCRIPTION = Software for collection/processing NetFlow data from Cisco/Juniper

# Issues:
# /usr/local is referenced by two binaries:
#  - /opt/csw/bin/flow-rptfmt
#  - /opt/csw/bin/flow-rpt2rrd

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

BUILD_DEP_PKGS = CSWmysql5devel CSWossldevel
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_OVERRIDE_VARS = AM_CFLAGS

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw 
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-mysql=/opt/csw

EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

PACKAGES = CSWflow-tools
SPKG_DESC_CSWflow-tools = $(DESCRIPTION)
# Catch-all package, no PKGFILES.
RUNTIME_DEP_PKGS_CSWflow-tools += CSWlibft0
RUNTIME_DEP_PKGS_CSWflow-tools += CSWosslrt
RUNTIME_DEP_PKGS_CSWflow-tools += CSWlibz1
# Doesn't link against PostgreSQL libraries in practice.
# RUNTIME_DEP_PKGS_CSWflow-tools += CSWpostgresql
RUNTIME_DEP_PKGS_CSWflow-tools += CSWlibmysqlclient15
OBSOLETED_BY_CSWflow-tools = CSWflowtools

PACKAGES += CSWlibft0
CATALOGNAME_CSWlibft0 = libft0
PKGFILES_CSWlibft0 += $(call baseisadirs,$(libdir),libft\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibft0 += Software for collection/processing NetFlow data from Cisco/Juniper., libft.so.0
RUNTIME_DEP_PKGS_CSWlibft0 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibft0 += CSWlibz1

PACKAGES += CSWflow-tools-dev
SPKG_DESC_CSWflow-tools-dev = Flow-tools development files
PKGFILES_CSWflow-tools-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWflow-tools-dev += CSWlibft0

include gar/category.mk

post-install-modulated:
	/opt/csw/gnu/sed -in 's#/usr/local/netflow/var/#/etc/opt/csw/#g' $(DESTDIR)/opt/csw/bin/flow-rpt2rrd
	/opt/csw/gnu/sed -in 's#/usr/local/netflow/var/#/etc/opt/csw/#g' $(DESTDIR)/opt/csw/bin/flow-rptfmt
	rm -f $(DESTDIR)/opt/csw/bin/flow-rpt2rrdn
	rm -f $(DESTDIR)/opt/csw/bin/flow-rptfmtn



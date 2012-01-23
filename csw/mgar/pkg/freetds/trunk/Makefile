# $Id$
NAME = freetds
VERSION = 0.91
CATEGORIES = lib

DESCRIPTION = Implementation of the TDS protocol used by MS SQL Server and Sybase
define BLURB
  FreeTDS is a set of libraries for Unix and Linux that allows your programs
  to natively talk to Microsoft SQL Server and Sybase databases.
endef

MASTER_SITES += http://ftp.ibiblio.org/pub/Linux/ALPHA/freetds/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.freetds.org/

BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWunixodbc-dev

PACKAGES = CSWfreetds
SPKG_DESC_CSWfreetds = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWfreetds += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWfreetds += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWfreetds += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWfreetds += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWfreetds += CSWlibsybdb5
# This is just an example
CHECKPKG_OVERRIDES_CSWfreetds += file-with-bad-content|/usr/local|root/opt/csw/bin/osql

PACKAGES += CSWlibct4
SPKG_DESC_CSWlibct4 = FreeTDS library, libct.so.4
PKGFILES_CSWlibct4 += $(call pkgfiles_lib,libct.so.4)
RUNTIME_DEP_PKGS_CSWlibct4 += CSWlibiconv2

PACKAGES += CSWlibsybdb5
SPKG_DESC_CSWlibsybdb5 += FreeTDS library, libsybdb.so.5
PKGFILES_CSWlibsybdb5 += $(call pkgfiles_lib,libsybdb.so.5)
RUNTIME_DEP_PKGS_CSWlibsybdb5 += CSWlibiconv2

PACKAGES += CSWlibtdsodbc0
SPKG_DESC_CSWlibtdsodbc0 = FreeTDS library, libtdsodbc.so.0
PKGFILES_CSWlibtdsodbc0 += $(call pkgfiles_lib,libtdsodbc.so.0)
RUNTIME_DEP_PKGS_CSWlibtdsodbc0 += CSWlibodbcinst2
RUNTIME_DEP_PKGS_CSWlibtdsodbc0 += CSWlibiconv2

PACKAGES += CSWfreetds-dev
SPKG_DESC_CSWfreetds-dev = Development files for libct.so.4, libsybdb.so.5 and libtdsodbc.so.0
PKGFILES_CSWfreetds-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWfreetds-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWfreetds-dev += CSWlibsybdb5
RUNTIME_DEP_PKGS_CSWfreetds-dev += CSWlibct4
RUNTIME_DEP_PKGS_CSWfreetds-dev += CSWlibtdsodbc0
OBSOLETED_BY_CSWfreetds-dev += CSWfreetdsdoc
CATALOGNAME_CSWfreetdsdoc = freetds_doc_stub
# There are lots of examples which would need careful adjustment, contributions welcome!
CHECKPKG_OVERRIDES_CSWfreetds-dev += file-with-bad-content

# Make sure library is self-sufficient
EXTRA_LINKER_FLAGS = -liconv

BUILD64_LIBS_ONLY = 1

# Testsuite needs a running Sybase/SQLServer database
SKIPTEST ?= 1

EXTRA_PAX_ARGS = -s ',.*{}$$,,p' -s ',/doc/$(NAME)-$(VERSION),/doc/$(NAME),p'

PRESERVECONF = $(addprefix $(sysconfdir)/,freetds.conf locales.conf pool.conf)
MIGRATE_FILES_CSWfreetds = freetds.conf locales.conf pool.conf

include gar/category.mk

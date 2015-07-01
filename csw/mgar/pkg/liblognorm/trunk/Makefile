# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = liblognorm
VERSION = 1.1.1
GARTYPE = v2

DESCRIPTION = Liblognorm shall help to make sense out of syslog data

MASTER_SITES = http://www.liblognorm.com/files/download/
DISTFILES += $(DISTNAME).tar.gz

# Use patch until this is fixed:
#   http://bugzilla.adiscon.com/show_bug.cgi?id=539
PATCHFILES += 0001-Use-substitute-for-strndup.patch

VENDOR_URL = http://www.liblognorm.com/

BUILD_DEP_PKGS += CSWpy-sphinx
BUILD_DEP_PKGS += CSWlibjson-c-dev
BUILD_DEP_PKGS += CSWlibestr-dev

PACKAGES += CSWliblognorm2
SPKG_DESC_CSWliblognorm2 = Liblognorm shall help to make sense out of syslog data, liblognorm.so.2
PKGFILES_CSWliblognorm2 += $(call pkgfiles_lib,liblognorm.so.2)
RUNTIME_DEP_PKGS_CSWliblognorm2 += CSWlibjson-c3
RUNTIME_DEP_PKGS_CSWliblognorm2 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWliblognorm2 += CSWlibestr0

PACKAGES += CSWliblognorm-dev
SPKG_DESC_CSWliblognorm-dev = Deevelopment files for liblognorm
RUNTIME_DEP_PKGS_CSWliblognorm-dev += CSWliblognorm2
RUNTIME_DEP_PKGS_CSWliblognorm-dev += CSWlibjson-c3
RUNTIME_DEP_PKGS_CSWliblognorm-dev += CSWlibestr0

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-regexp
CONFIGURE_ARGS += --enable-docs

# We GNU find as 'find'
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk


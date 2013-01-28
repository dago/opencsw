# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mosh
VERSION = 1.2.3
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Mobile shell

MASTER_SITES = https://github.com/downloads/keithw/mosh/
DISTFILES  = $PATCHFILES += 0001-Add-missing-include.patchrder_8h-source.html

BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWprotobuf-gxx-dev

PACKAGES += CSWmosh
SPKG_DESC_CSWmypkg = Mobile shell
RUNTIME_DEP_PKGS_CSWmosh += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWmosh += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWmosh += CSWlibprotobuf7-gxx
RUNTIME_DEP_PKGS_CSWmosh += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CRUNTIME_DEP_PKGS_CSWmosh += CSWlibssp0
RUNTIME_DEP_PKGS_CSWmosh += CSWlibssl1-0-0CSWmosh += CSWlibz1

# Needed by mosh perl script
RUNTIME_DEP_PKGS_CSWmosh += CSWpm-io-tty
CHECKPKG_OVERRIDES_CSWmosh += surplus-dependency|CSWpm-io-tty

REINPLACEMENTS += cswperl
REINPLACE_MATCH_cswperl = /usr/bin/env perl
REINPLACE_WITH_cswperl = $(bindir)/perl
REINPLACE_FILES_cswperl += scripts/mosh

# boost gxx is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

Galigned__=aligned

EXTRA_CONFIGURE_EXPORTS += PROTOC
CONFIGURE_ENV_PROTOC = $(prefix)/gxx/bin/protoc

EXTRA_INC += $(prefix)/gxx/include
EXTRA_LIB += include gar/category.mk


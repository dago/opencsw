# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dsh
VERSION = 0.25.9
GARTYPE = v2
CATEGORIES = devel
RUNTIME_DEP_PKGS_CSWdsh = CSWlibdshconfig
BUILD_DEP_PKGS = CSWlibdshconfig

DESCRIPTION = Distributed shell. Runs command through rsh or ssh on a cluster of machines.

MASTER_SITES = http://www.netfort.gr.jp/~dancer/software/downloads/dsh-0.25.9.tar.gz
DISTFILES  = $(DISTNAME).tar.gz

# for libintl_gettext, libintl_textdomain, libintl_bindtextdomain
EXTRA_LINKER_FLAGS = -lintl

CONFIGURE_ARGS = $(DIRPATHS) 

TEST_SCRIPTS = 

TEST_TARGET = 

include gar/category.mk


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

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# for libintl_gettext, libintl_textdomain, libintl_bindtextdomain
LIBS += -lintl
export LIBS

CONFIGURE_ARGS = $(DIRPATHS) 

TEST_SCRIPTS = 

TEST_TARGET = 

include gar/category.mk


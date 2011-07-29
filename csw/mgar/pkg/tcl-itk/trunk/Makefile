# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = itk
PACKAGES = CSWtclitk
CATALOGNAME_CSWtclitk = tcl-itk
VERSION = 3.4
GARTYPE = v2
CATEGORIES = lang
LICENSE = license.terms
DEPENDS = CSWtcl CSWtclitcl
BUILD_DEP_PKGS = CSWtclitcl
DESCRIPTION = [incr Tk] is a framework for building mega-widgets using [incr Tcl]

# Source code downloaded from here:
# cvs -d:pserver:anonymous@incrtcl.cvs.sourceforge.net:/cvsroot/incrtcl export -D 2007-12-31 -d itk-3.4 itk
MASTER_SITES = 
DISTFILES  = $(DISTNAME).tar.gz

# This package requires the soure code of Tk to be available on
# the system at the location defined in
# /opt/csw/lib/tkConfig.sh:
# TK_SRC_DIR='/opt/csw/src/tk'

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = 

include gar/category.mk


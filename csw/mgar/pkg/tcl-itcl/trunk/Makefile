# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = itcl
PACKAGES = CSWtclitcl
CATALOGNAME_CSWtclitcl = tcl-itcl
VERSION = 3.4
GARTYPE = v2
CATEGORIES = lang
LICENSE = license.terms
DEPENDS = CSWtcl
DISTNAME = $(NAME)$(VERSION)

DESCRIPTION = [incr Tcl] is a Tcl extension that provides object-oriented features

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME)b1.tar.gz

# This package requires the soure code of Tcl to be available on
# the system at the location defined in
# /opt/csw/lib/tclConfig.sh:
# TCL_SRC_DIR='/opt/csw/src/tcl'

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = 

# also include static libraries, as libitclstub$(VERSION).a
# is only available as static
MERGE_EXCLUDE_STATICLIBS =

include gar/category.mk


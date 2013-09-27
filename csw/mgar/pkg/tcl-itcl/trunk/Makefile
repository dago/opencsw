# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#

NAME = itcl
VERSION = 3.4.1

SF_PROJECT = incrtcl
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

DESCRIPTION = IncrTcl is a Tcl extension that provides object-oriented features

LICENSE = license.terms

PACKAGES = CSWtcl-itcl

BUILD64 = 1/opt/csw/src/tcl'

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = 

# also include static libraries, as libitclstub$(VERSION).a
# is only available as static
MERGE_EXCLUDE_STATICLIBS =

include
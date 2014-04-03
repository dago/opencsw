# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = filebench
VERSION = 1.4.9.1
GARTYPE = v2

DESCRIPTION = A file system and storage benchmark

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-dofile-must-not-be-static-as-it-is-used-as-extern-so.patch

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


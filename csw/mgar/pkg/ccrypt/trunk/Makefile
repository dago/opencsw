# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ccrypt
VERSION = 1.10
GARTYPE = v2

DESCRIPTION = Secure encryption and decryption of files and streams

MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWccrypt += CSWlibintl8
# This is just an optional .el file
CHECKPKG_OVERRIDES_CSWccrypt += missing-dependency|CSWemacs-common

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk


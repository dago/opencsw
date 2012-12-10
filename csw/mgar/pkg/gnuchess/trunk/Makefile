# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnuchess
VERSION = 6.0.2

DESCRIPTION = GNU Chess

GNU_PROJECT = chess
MASTER_SITES = $(GNU_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += book_1.02.pgn.gz

GARCOMPILER = GCC4

BUILD64 = 1
ISAEXEC = 1

PACKAGES += CSWgnuchess
SPKG_DESC_CSWgnuchess = GNU Chess
RUNTIME_DEP_PKGS_CSWgnuchess += CSWlibgcc-s1
OBSOLETED_BY_CSWgnuchess += CSWchss
CATALOGNAME_CSWchss = gnuchess_stub

include gar/category.mk

post-merge:
	cd $(PKGROOT)$(sharedstatedir)/gnuchess && $(PKGROOT)$(bindir)/gnuchess -a $(abspath $(WORKDIR_FIRSTMOD)/book_1.02.pgn)
	@$(MAKECOOKIE)

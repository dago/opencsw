# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = thttpd
VERSION = 2.25b
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = The tiny/turbo/throttling HTTP server

MASTER_SITES = http://www.acme.com/software/thttpd/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Honour-DESTDIR.patch

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

REINPLACEMENTS += nochown
REINPLACE_MATCH_nochown = -o bin -g bin
REINPLACE_WITH_nochown =
REINPLACE_FILES_nochown += Makefile.in

REINPLACEMENTS += nochgrp
REINPLACE_MATCH_nochgrp = chown.*|chgrp.*
REINPLACE_WITH_nochgrp = #
REINPLACE_FILES_nochgrp += extras/Makefile.in

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += prefix
INSTALL_OVERRIDE_VAR_prefix = $(DESTDIR)$(prefix)
INSTALL_OVERRIDE_VARS += MANDIR
INSTALL_OVERRIDE_VAR_MANDIR = $(DESTDIR)$(mandir)
INSTALL_OVERRIDE_VARS += DESTDIR
INSTALL_OVERRIDE_VAR_DESTDIR =

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = unzoo
VERSION = 4.4
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = ZOO archive extractor
define BLURB
endef

MASTER_SITES = http://archives.math.utk.edu/software/multi-platform/gap/util/
DISTFILES  = unzoo.c
DISTFILES += COPYING
DISTFILES += README
DISTFILES += unzoo.1

DISTNAME = 

EXTRA_CPPFLAGS = -DSYS_IS_UNIX

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(CC) $(CPPFLAGS) $(CFLAGS) $(LDFLAGS) unzoo.c -o unzoo
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/unzoo $(DESTDIR)$(bindir)/unzoo
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKDIR)/unzoo.1 $(DESTDIR)$(mandir)/man1/unzoo.1
	ginstall -d $(DESTDIR)$(docdir)/unzoo
	ginstall $(WORKDIR)/README $(DESTDIR)$(docdir)/unzoo/README
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = yodl
VERSION = 3.03.0
GARTYPE = v2

DESCRIPTION = Your Own Document Language

MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(NAME)_$(VERSION).orig.tar.gz
DISTFILES += INSTALL.im

PATCHFILES += 0001-getcwd-with-size-0-return-EINVAL-on-Solaris-even-whe.patch
PATCHFILES += 0002-realpath-does-not-like-second-argument-to-be-NULL-on.patch

EXPANDVARS += INSTALL.im

REINPLACEMENTS += icmake
REINPLACE_MATCH_icmake = /usr/bin/icmake
REINPLACE_WITH_icmake = $(bindir)/icmake
REINPLACE_FILES_icmake += build

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	cp $(WORKDIR)/INSTALL.im $(WORKSRC)/INSTALL.im
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && CFLAGS="$(CFLAGS)" ./build programs
	cd $(WORKSRC) && CFLAGS="$(CFLAGS)" ./build man
	cd $(WORKSRC) && CFLAGS="$(CFLAGS)" ./build manual
	cd $(WORKSRC) && CFLAGS="$(CFLAGS)" ./build macros
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && ./build install programs $(DESTDIR)
	cd $(WORKSRC) && ./build install man $(DESTDIR)
	cd $(WORKSRC) && ./build install manual $(DESTDIR)
	cd $(WORKSRC) && ./build install macros $(DESTDIR)
	cd $(WORKSRC) && ./build install docs $(DESTDIR)
	@$(MAKECOOKIE)

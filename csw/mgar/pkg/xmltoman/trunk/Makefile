# $Id$
NAME = xmltoman
VERSION = 0.4
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A man page creation tool
define BLURB
A special tool to convert xml files to man pages.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Override-default-hard-coded-prefix-with-opt-csw.patch
PATCHFILES += 0002-Use-CSW-perl-instead-of-system-perl.patch
PATCHFILES += 0003-Use-ginstall-not-system-install.patch
PATCHFILES += 0004-Patch-usr-share-references-out-of-the-manpages.patch

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWperl

include gar/category.mk

post-build-modulated:
	@(cd $(WORKSRC); for m in xmltoman xmlmantohtml; do gmake $$m.1; done)
	@$(MAKECOOKIE);

post-install-modulated:
	@(cd $(WORKSRC); \
		gmkdir -p $(DESTDIR)$(mandir)/man1 \
			$(DESTDIR)$(docdir)/$(NAME); \
		for m in xmltoman xmlmantohtml; do \
			cp $$m.1 $(DESTDIR)$(mandir)/man1; \
		done; \
		cp -pR xml $(DESTDIR)$(docdir)/$(NAME)/examples; )
	@$(MAKECOOKIE)
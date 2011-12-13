NAME = freeciv
VERSION = 2.3.1
CATEGORIES = apps

DESCRIPTION = Free turn-based multiplayer strategy game
define BLURB
Freeciv is a Free and Open Source empire-building strategy game inspired by the history of human civilization. The game commences in prehistory and your mission is to lead your tribe from the stone age to the space age...
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=138322
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibz1
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibintl8
RUNTIME_DEP_PKGS_CSWfreeciv += CSWftype2
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWgtk2
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWpango
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWfreeciv += CSWfconfig
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWsdlmixer
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgio2-0-0

GARCOMPILER = GNU

PATCHFILES += 0001-use-finite-instead-of-isfinite.patch

TEST_SCRIPTS =

CONFIGURE_ARGS += $(DIRPATHS)

# build package on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

post-install-modulated:

	perl -pi -e 's|/usr/local|/opt/csw|' \
		$(DESTDIR)/opt/csw/share/man/man6/freeciv-*.6

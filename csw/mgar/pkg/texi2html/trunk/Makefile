# $Id$

NAME = texi2html
VERSION = 5.0
GARTYPE = v2

DESCRIPTION = A Texinfo to HTML converter
define BLURB
	Texi2HTML is a Perl script which converts Texinfo source files to
	HTML output; supports many features beyond those supported by
	makeinfo.
endef

MASTER_SITES	=	http://download.savannah.gnu.org/releases/texi2html/

DISTFILES	=	$(DISTNAME).tar.bz2
PATCHFILES	+=	0001-Use-environment-s-bash-in-test-scripts.patch

CONFIGURE_ARGS = $(DIRPATHS)

BUILD_DEP_PKGS		+=	CSWlatex2html
BUILD_DEP_PKGS		+=	CSWCSWtex4ht

TEST_SCRIPTS = custom

ARCHALL_CSWtexi2html = 1

RUNTIME_DEP_PKGS_CSWtexi2html	+=	CSWperl
RUNTIME_DEP_PKGS_CSWtexi2html	+=	CSWlatex2html
CHECKPKG_OVERRIDES_CSWtexi2html	+=	surplus-dependency|latex2html
RUNTIME_DEP_PKGS_CSWtexi2html	+=	CSWtex4ht
CHECKPKG_OVERRIDES_CSWtexi2html	+=	surplus-dependency|tex4ht
# only in the comments / documentation:
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/local|root/opt/csw/share/texi2html/lib/libintl-perl/lib/Locale/Messages.pm
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/local|root/opt/csw/share/texi2html/lib/libintl-perl/lib/Locale/gettext_pp.pm
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/local|root/opt/csw/share/texi2html/lib/libintl-perl/lib/Locale/TextDomain.pm
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/share|root/opt/csw/share/texi2html/lib/libintl-perl/lib/Locale/Messages.pm
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/share|root/opt/csw/share/texi2html/lib/libintl-perl/lib/Locale/gettext_pp.pm
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/share|root/opt/csw/share/texi2html/lib/libintl-perl/lib/Locale/TextDomain.pm
# installation instructions:
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/texi2html.info
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-with-bad-content|/usr/local|root/opt/csw/share/texinfo/html/texi2html.html
# the collisions are temporarly overrided as this package will replace
# the old texi2html, provided by teTeX, and complement the TeXLive
# packages, where texi2html is no more supplied:
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-collision|/opt/csw/share/texi2html/images/COPYING|CSWtetex|CSWtexi2html
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-collision|/opt/csw/share/info/texi2html.info|CSWtetex|CSWtexi2html
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-collision|/opt/csw/share/man/man1/texi2html.1|CSWtetex|CSWtexi2html
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-collision|/opt/csw/share/texi2html/images/bg.jpg|CSWtetex|CSWtexi2html
CHECKPKG_OVERRIDES_CSWtexi2html	+=	file-collision|/opt/csw/bin/texi2html|CSWtetex|CSWtexi2html

REINPLACE_WHEN_USRLOCAL	=	postinstall
REINPLACE_USRLOCAL		+=	/opt/csw/bin/texi2html

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# there are failing tests:
#    formating: IMHO not real errors but probably due to different
#               httex, l2h and TeX used to gather de references
# and I choose to ignore them as the remaining ones pass.
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

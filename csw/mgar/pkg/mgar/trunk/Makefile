# TODO (release-critical prefixed with !, non release-critical with *)
# ! Check man pages for formatting/spelling bugs. Edit getting started to
#   include some common tasks (see mgar wiki page).
# * Add bash auto-completion configuration
NAME = mgar
VERSION = 0.90
CATEGORIES = apps

DESCRIPTION = Command line interface to the OpenCSW build system
define BLURB
  Long description
endef

VENDOR_URL = http://gar.opencsw.org
SVNROOT    = https://opencsw.svn.sourceforge.net/svnroot/opencsw/gar-wrapper
SVNREV     = 317

ARCHALL = 1

RUNTIME_DEP_PKGS  = CSWnamazu
RUNTIME_DEP_PKGS += CSWggrep
RUNTIME_DEP_PKGS += CSWgfind
RUNTIME_DEP_PKGS += CSWgmake
RUNTIME_DEP_PKGS += CSWsvn
RUNTIME_DEP_PKGS += CSWgardevel # Meta pkg. Pulls in deps required by GAR.

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	svn export --force -r $(SVNREV) $(SVNROOT)/ $(WORKSRC)
	a2x -d manpage -f manpage $(WORKSRC)/mgar.1.txt
	a2x -d manpage -f manpage $(WORKSRC)/mgar.5.txt
	$(MAKECOOKIE)

install-custom:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(mandir)/man1 $(DESTDIR)$(mandir)/man5
	cp $(WORKSRC)/mgar $(DESTDIR)$(bindir)
	cp $(WORKSRC)/mgar.1 $(DESTDIR)$(mandir)/man1/
	cp $(WORKSRC)/mgar.5 $(DESTDIR)$(mandir)/man5/
	$(MAKECOOKIE)

GARNAME = git
GARVERSION = 1.6.0.5
CATEGORIES = devel

PREREQUISITE_PKGS = CSWasciidoc CSWossldevel CSWxmlto CSWbash CSWcurl
PREREQUISITE_PKGS += CSWgsed CSWgnulinks CSWperl CSWtcl CSWtk

REQUIRED_PKGS_CSWgit = CSWzlib CSWperl CSWrsync CSWcurl CSWosslrt CSWpmgit
REQUIRED_PKGS_CSWgitk = CSWgit CSWtk
REQUIRED_PKGS_CSWgitgui = CSWgit CSWtk

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

MASTER_SITES = http://kernel.org/pub/software/scm/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgit,)
DISTFILES += $(call admfiles,CSWgitdoc,)
DISTFILES += $(call admfiles,CSWpmgit,)
DISTFILES += $(call admfiles,CSWgitgui,)
DISTFILES += $(call admfiles,CSWgitk,)

PATCHFILES = doc-makefile.patch

PKGFILES_CSWgitgui = $(bindir)/git-gui $(bindir)/git-citool \
			$(mandir)/man1/git-gui.* $(mandir)/man1/git-citool.* \
			$(datadir)/git-gui/.* $(datadir)/doc/git-gui.*
PKGFILES_CSWgitk = $(bindir)/gitk $(datadir)/doc/gitk.* $(datadir)/gitk.* \
			$(mandir)/man1/gitk.*
PKGFILES_CSWgitdoc = $(datadir)/doc/.*

PKGFILES_CSWpmgit = 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS) --with-shell=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-tcltk=/opt/csw/bin/tclsh
CONFIGURE_ARGS += --with-zlib=/opt/csw

BUILD_ARGS = MSGFMT=gmsgfmt SHELL_PATH=/opt/csw/bin/bash all doc

INSTALL_ARGS = install install-doc

include gar/category.mk

# for tail -n and to override things like, etc with the gnu counterparts
# gnu must come first so xpg4/sed isn't found first.
PATH := /opt/csw/gnu:/usr/xpg4/bin:$(PATH)

post-install-modulated:
	@echo Removing perllocal.pod
	@rm -f ${DESTDIR}/opt/csw/lib/perl/5.8.8/perllocal.pod*
	@chmod 644 ${DESTDIR}/${libdir}/perl5/site_perl/*pm
	@$(MAKECOOKIE)

GARNAME = git
GARVERSION = 1.6.0.5
CATEGORIES = devel

PREREQUISITE_PKGS = CSWasciidoc CSWossldevel CSWxmlto CSWbash CSWcurl
PREREQUISITE_PKGS += CSWgsed CSWgnulinks CSWperl CSWtk CSWexpat
PREREQUISITE_PKGS += CSWzlib CSWpmerror CSWpmsvn CSWcvs

REQUIRED_PKGS_CSWgit = CSWzlib CSWperl CSWrsync CSWcurlrt CSWosslrt
REQUIRED_PKGS_CSWgit += CSWossh CSWiconv CSWexpat CSWbash

REQUIRED_PKGS_CSWgitk = CSWgit CSWtk

REQUIRED_PKGS_CSWgitgui = CSWgit CSWtk

REQUIRED_PKGS_CSWgitsvn = CSWgit CSWpmsvn

REQUIRED_PKGS_CSWgitcvs = CSWgit CSWcvs

REQUIRED_PKGS_CSWgitdoc = CSWgit

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

MASTER_SITES = http://kernel.org/pub/software/scm/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgitsvn,)
DISTFILES += $(call admfiles,CSWgitgui,)
DISTFILES += $(call admfiles,CSWgitk,)
DISTFILES += $(call admfiles,CSWgitemacs,)
DISTFILES += $(call admfiles,CSWgitcvs,)
DISTFILES += $(call admfiles,CSWgitdoc,)
DISTFILES += $(call admfiles,CSWgit,)

PATCHFILES = doc-makefile.patch

PKGFILES_CSWgitsvn = .*svn.*
PKGFILES_CSWgitgui = .*git-gui.* .*git-citool.*
PKGFILES_CSWgitk = .*gitk.*
PKGFILES_CSWgitemacs = .*emacs.*
PKGFILES_CSWgitcvs = .*cvs.*
PKGFILES_CSWgitdoc = $(datadir)/doc/.*

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS) --with-shell=$(bindir)/bash
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-tcltk=$(bindir)/wish
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)

BUILD_ARGS = MSGFMT=gmsgfmt SHELL_PATH=/opt/csw/bin/bash \
		ETC_CONFIG=$(sysconfdir)/gitconfig \
		all doc

INSTALL_ARGS = ETC_CONFIG=$(sysconfdir)/gitconfig install-doc

include gar/category.mk

# for tail -n and to override things like, etc with the gnu counterparts
# gnu must come first so xpg4/sed isn't found first.
PATH := /opt/csw/gnu:/usr/xpg4/bin:$(PATH)

# force the elisp extension to be built too.
post-build-modulated:
	@echo Builing Emacs Git extension
	@( cd $(WORKSRC); $(MAKE) -C contrib/emacs )

post-install-modulated: GD=$(DESTDIR)/$(datadir)/doc/$(GARNAME)-$(GARVERSION)
post-install-modulated:
	@echo Cleaning up perl stuff
	@rm -rf $(DESTDIR)/$(libdir)/perl5/site_perl/5*
	@rm -rf $(DESTDIR)/$(perllib)/
	@chmod 644 $(DESTDIR)/$(libdir)/perl5/site_perl/*pm
	@echo Installing Emacs Git extension
	@( cd $(WORKSRC); $(MAKE) -C contrib/emacs install \
		emacsdir=$(DESTDIR)/$(datadir)/emacs/site-lisp )
	@echo Installing Documentation
	@( cd $(WORKSRC); \
		ginstall -c -m 0755 -d $(GD); \
		cp -R Documentation/*.txt $(GD)/; \
		cp -R contrib/hooks README COPYING $(GD)/; \
		cp -R Documentation/*.html Documentation/docbook-xsl.css $(GD)/; \
		cp -R Documentation/howto Documentation/technical $(GD)/; )
	@$(MAKECOOKIE)

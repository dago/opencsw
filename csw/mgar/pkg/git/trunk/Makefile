GARNAME = git
GARVERSION = 1.6.3.3
#xPATCHLEVEL = rc3
CATEGORIES = devel

# disable tests until next version bump (at the top so it stands out)
# TEST_SCRIPTS = 

PACKAGES = CSWgit CSWgitk CSWgitgui CSWgitsvn CSWgitcvs CSWgitemacs CSWgitdoc

CATALOGNAME_CSWgit = git
CATALOGNAME_CSWgitcvs = git_cvs
CATALOGNAME_CSWgitsvn = git_svn
CATALOGNAME_CSWgitemacs = git_emacs
CATALOGNAME_CSWgitgui = git_gui
CATALOGNAME_CSWgitdoc = git_doc
CATALOGNAME_CSWgitk = gitk

ARCHALL_CSWgitsvn = 1
ARCHALL_CSWgitcvs = 1
ARCHALL_CSWgitk = 1
ARCHALL_CSWgitgui = 1
ARCHALL_CSWgitemacs = 1
ARCHALL_CSWgitdoc = 1

PREREQUISITE_PKGS = CSWasciidoc CSWossldevel CSWxmlto CSWbash CSWcurldevel
PREREQUISITE_PKGS += CSWgsed CSWgnulinks CSWperl CSWtk CSWexpat
PREREQUISITE_PKGS += CSWzlib CSWpmerror CSWpmsvn CSWcvs CSWemacs
PREREQUISITE_PKGS += CSWautoconf

REQUIRED_PKGS_CSWgit = CSWzlib CSWperl CSWrsync CSWcurlrt CSWosslrt
REQUIRED_PKGS_CSWgit += CSWosshclient CSWiconv CSWexpat CSWbash CSWpmerror
REQUIRED_PKGS_CSWgit += CSWpmtermreadkey

REQUIRED_PKGS_CSWgitk = CSWgit CSWtk

REQUIRED_PKGS_CSWgitgui = CSWgit CSWtk

REQUIRED_PKGS_CSWgitsvn = CSWgit CSWpmsvn

REQUIRED_PKGS_CSWgitcvs = CSWgit CSWcvs CSWcvsps

REQUIRED_PKGS_CSWgitemacs = CSWgit CSWemacs

REQUIRED_PKGS_CSWgitdoc = CSWgit

LICENSE_CSWgit = COPYING
LICENSE_CSWgitk = COPYING
LICENSE_CSWgitgui = COPYING
LICENSE_CSWgitsvn = COPYING
LICENSE_CSWgitcvs = COPYING
LICENSE_CSWgitemacs = COPYING
LICENSE_CSWgitdoc = COPYING

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

SPKG_DESC_CSWgit = Fast Version Control System
SPKG_DESC_CSWgitk = Git revision tree visualiser
SPKG_DESC_CSWgitgui = Git GUI tool
SPKG_DESC_CSWgitsvn = Git tools for working with Subversion repositories
SPKG_DESC_CSWgitcvs = Git tools for working with CVS repositories
SPKG_DESC_CSWgitdoc = Documentation for Git
SPKG_DESC_CSWgitemacs = Git VCS support for Emacs

#NOTE: If you need to proxy git:// connections, set GIT_USE_PROXY in
#	your .garrc file.  (That leaves this recipe in a more generic form.)
GIT_REPOS  = git://git.kernel.org/pub/scm/git/git.git
GIT_TREEISH_git.git = v$(GARVERSION)$(if $(PATCHLEVEL),-$(PATCHLEVEL))

fdirs = $(bindir_install) $(mandir) $(libexecdir_install)
define _git_files
$(foreach d,$(fdirs),$(d)/.*$(1).*) $(sharedstatedir)/$(1).*
endef

PKGFILES_CSWgitsvn = $(call _git_files,git-svn)
PKGFILES_CSWgitgui = $(call _git_files,git-gui) $(call _git_files,git-citool)
PKGFILES_CSWgitk = $(call _git_files,gitk)
PKGFILES_CSWgitcvs = $(foreach d,$(fdirs),$(d)/.*cvs.*)
PKGFILES_CSWgitemacs = .*emacs.*
PKGFILES_CSWgitdoc = $(docdir)/.*

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

CONFIGURE_ARGS = $(DIRPATHS) --with-shell=$(bindir)/bash
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-tcltk=$(bindir)/wish
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --enable-pthreads="-D_REENTRANT -lpthread"

BUILD_ARGS = MSGFMT=gmsgfmt SHELL_PATH=/opt/csw/bin/bash \
		ETC_GITCONFIG=$(sysconfdir)/gitconfig V=1 \
		all doc

INSTALL_ARGS = ETC_GITCONFIG=$(sysconfdir)/gitconfig \
		INSTALLDIRS=vendor \
		install-doc

include gar/category.mk

# for tail -n and to override things like, etc with the gnu counterparts
# gnu must come first so xpg4/sed isn't found first.
PATH := /opt/csw/gnu:/usr/xpg4/bin:$(PATH)

# git doesn't track the configure file, it needs to be built when using
# source right from the repo.
pre-configure-modulated:
	@(cd $(WORKSRC); echo $(GARVERSION) > version; \
		$(MAKE) configure )
	@$(MAKECOOKIE)

# force the elisp extension to be built too.
post-build-modulated:
	@echo Builing Emacs Git extension
	@( cd $(WORKSRC); $(MAKE) -C contrib/emacs )

post-install-modulated: GD=$(DESTDIR)/$(datadir)/doc/$(GARNAME)
post-install-modulated:
	@echo Cleaning up perl stuff
	@rm -rf $(DESTDIR)/$(libdir)/perl5/site_perl/5*
	@rm -rf $(DESTDIR)/$(perllib)/
	@chmod 644 $(DESTDIR)/$(datadir)/perl/csw/*pm
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

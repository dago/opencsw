NAME = git
VERSION = 1.7.4
#PATCHLEVEL = rc1
CATEGORIES = devel

VENDOR_URL = http://git-scm.org/

# disable tests until next version bump (at the top so it stands out)
# 1.7.2.1 and 1.7.3 have a failure on current9s when fr.UFT-8 is
# detected as the first available utf8 locale.  the failure is
# harmless though.

TEST_SCRIPTS =

PACKAGES = CSWgit CSWgitk CSWgitgui CSWgitsvn CSWgitcvs CSWgitemacs CSWgitdoc
PACKAGES += CSWgitcompletion CSWgitdevel

CATALOGNAME_CSWgit = git
CATALOGNAME_CSWgitcvs = git_cvs
CATALOGNAME_CSWgitsvn = git_svn
CATALOGNAME_CSWgitemacs = git_emacs
CATALOGNAME_CSWgitgui = git_gui
CATALOGNAME_CSWgitdoc = git_doc
CATALOGNAME_CSWgitk = gitk
CATALOGNAME_CSWgitcompletion = git_completion
CATALOGNAME_CSWgitdevel = git_devel

ARCHALL_CSWgitsvn = 1
ARCHALL_CSWgitcvs = 1
ARCHALL_CSWgitk = 1
ARCHALL_CSWgitgui = 1
ARCHALL_CSWgitemacs = 1
ARCHALL_CSWgitdoc = 1
ARCHALL_CSWgitcompletion = 1

BUILD_DEP_PKGS = CSWasciidoc CSWossldevel CSWxmlto CSWbash CSWcurldevel
BUILD_DEP_PKGS += CSWgsed CSWgnulinks CSWperl CSWtk CSWexpat
BUILD_DEP_PKGS += CSWzlib CSWpmerror CSWpmsvn CSWcvs CSWemacs
BUILD_DEP_PKGS += CSWpython

RUNTIME_DEP_PKGS_CSWgit = CSWzlib CSWperl CSWrsync CSWcurlrt CSWosslrt
RUNTIME_DEP_PKGS_CSWgit += CSWosshclient CSWiconv CSWexpat CSWbash CSWpmerror
RUNTIME_DEP_PKGS_CSWgit += CSWpmtermreadkey CSWpmnetsmtpssl CSWless

RUNTIME_DEP_PKGS_CSWgitk = CSWgit CSWtk

RUNTIME_DEP_PKGS_CSWgitgui = CSWgit CSWtk

RUNTIME_DEP_PKGS_CSWgitsvn = CSWgit CSWpmsvn

RUNTIME_DEP_PKGS_CSWgitcvs = CSWgit CSWcvs CSWcvsps

RUNTIME_DEP_PKGS_CSWgitemacs = CSWgit CSWemacscommon

RUNTIME_DEP_PKGS_CSWgitdoc = CSWgit

RUNTIME_DEP_PKGS_CSWgitdevel = CSWgit

# We include bash here even though git itself depends on it because in theory
# git could use any other POSIX compliant shell and drop the dependency...
RUNTIME_DEP_PKGS_CSWgitcompletion = CSWgit CSWbash CSWbashcmplt

LICENSE = COPYING

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
SPKG_DESC_CSWgitcompletion = Bash completion support for Git
SPKG_DESC_CSWgitdevel = Headers and static libraries for Git

#NOTE: If you need to proxy git:// connections, set GIT_USE_PROXY in
#	your .garrc file.  (That leaves this recipe in a more generic form.)
GIT_REPOS  = git://git.kernel.org/pub/scm/git/git.git
GIT_TREEISH_git.git = v$(VERSION)$(if $(PATCHLEVEL),-$(PATCHLEVEL))

DISTFILES = CSWgit.postinstall

PATCHFILES += 0001-Update-path-in-documentation-to-be-CSW-proper.patch
PATCHFILES += 0002-Alter-the-value-of-_PATH_DEFPATH-when-paths.h-not-pr.patch
PATCHFILES += 0003-Update-path-in-sample-hook-file.patch
PATCHFILES += 0004-Use-bash-and-set-PATH-in-contributed-hook-file.patch

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
PKGFILES_CSWgitcompletion = .*/bash_completion.d/.*
PKGFILES_CSWgitdevel = $(includedir)/.* $(libdir)/.*

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
#set bashconfdir to sysconfdir when bash changes
bashconfdir = /opt/csw/etc/

CONFIGURE_ARGS = $(DIRPATHS) --with-shell=$(bindir)/bash
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-tcltk=$(bindir)/wish
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --enable-pthreads="-D_REENTRANT -lpthread"
CONFIGURE_ARGS += --with-gitconfig=$(sysconfdir)/gitconfig
CONFIGURE_ARGS += --with-pager=/opt/csw/bin/less
CONFIGURE_ARGS += --without-python

BUILD_ARGS = MSGFMT=gmsgfmt SHELL_PATH=/opt/csw/bin/bash \
		ASCIIDOC_NO_ROFF=YesPlease \
		all doc

INSTALL_ARGS = 	INSTALLDIRS=vendor \
		install-man install-html

# We want static libs installed for our devel package
MERGE_EXCLUDE_STATICLIBS =

ETCSERVICES = /opt/csw/etc/pkg/CSWgit/services

CHECKPKG_OVERRIDES_CSWgitcompletion += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWgitcompletion += surplus-dependency|CSWbashcmplt
CHECKPKG_OVERRIDES_CSWgitcompletion += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitdoc += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitdoc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgitdevel += discouraged-path-in-pkgmap|/opt/csw/lib/git/libgit.a
CHECKPKG_OVERRIDES_CSWgitdevel += discouraged-path-in-pkgmap|/opt/csw/lib/git/libxdiff.a
CHECKPKG_OVERRIDES_CSWgitdevel += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWpmerror
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWosshclient
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWrsync
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWless
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWpmnetsmtpssl
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWpmtermreadkey
CHECKPKG_OVERRIDES_CSWgit += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/git-config.1
CHECKPKG_OVERRIDES_CSWgit += file-with-bad-content|/usr/share|root/opt/csw/libexec/git-core/git-send-email
CHECKPKG_OVERRIDES_CSWgitgui += surplus-dependency|CSWtk
CHECKPKG_OVERRIDES_CSWgitgui += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitemacs += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitcvs += surplus-dependency|CSWcvsps
CHECKPKG_OVERRIDES_CSWgitcvs += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitcvs += surplus-dependency|CSWcvs
CHECKPKG_OVERRIDES_CSWgitk += surplus-dependency|CSWtk
CHECKPKG_OVERRIDES_CSWgitk += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitsvn += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgitsvn += surplus-dependency|CSWpmsvn

include gar/category.mk

# for tail -n and to override things like, etc with the gnu counterparts
# gnu must come first so xpg4/sed isn't found first.
PATH := /opt/csw/gnu:/usr/xpg4/bin:$(PATH)

# git doesn't track the configure file, it needs to be built when using
# source right from the repo.
pre-configure-modulated:
	@(cd $(WORKSRC); echo $(VERSION) > version; \
		$(MAKE) configure )
	@$(MAKECOOKIE)

# force the elisp extension to be built too.
post-build-modulated:
	@echo Builing Emacs Git extension
	@( cd $(WORKSRC); $(MAKE) -C contrib/emacs )

post-install-modulated: GD=$(DESTDIR)/$(datadir)/doc/$(NAME)
post-install-modulated: CONTHOOKS=$(GD)/contrib/hooks
post-install-modulated: BD=$(DESTDIR)/$(bashconfdir)/bash_completion.d
post-install-modulated: ID=$(DESTDIR)/$(includedir)/git
post-install-modulated: LD=$(DESTDIR)/$(libdir_install)/git
post-install-modulated:
	@echo Installing /etc/services definitions file
	@( ginstall -m 0755 -d $(DESTDIR)/opt/csw/etc/pkg/CSWgit/; \
	   echo "git 9418/tcp" >> $(DESTDIR)/$(ETCSERVICES); \
	   echo "git 9418/udp" >> $(DESTDIR)/$(ETCSERVICES); )
	@echo Cleaning up perl stuff
	@rm -rf $(DESTDIR)/$(libdir)/perl5/site_perl/5*
	@rm -rf $(DESTDIR)/$(perllib)/
	@chmod 644 $(DESTDIR)/$(datadir)/perl/csw/*pm
	@echo Installing Emacs Git extension
	@( cd $(WORKSRC); $(MAKE) -C contrib/emacs install \
		emacsdir=$(DESTDIR)/$(datadir)/emacs/site-lisp )
	@echo Installing devel files
	@( cd $(WORKSRC); \
		ginstall -c -m 0755 -d $(ID) $(LD); \
		for f in `find . -name "*.h"`; do \
			dn=`dirname $$f`; \
			ginstall -c -m 0755 -d $(ID)/$$dn; \
			ginstall -c -m 0644 $$f $(ID)/$$dn; \
		done; \
		ginstall -c -m 0444 libgit.a $(LD)/; \
		ginstall -c -m 0444 ./xdiff/lib.a $(LD)/libxdiff.a )
	@echo Installing Bash Completion files
	@( cd $(WORKSRC); \
		ginstall -c -m 0755 -d $(BD); \
		cp contrib/completion/* \
			$(BD)/ )
	@( cd $(WORKSRC)/contrib/hooks; \
		ginstall -c -d -m 0755 $(CONTHOOKS); \
		ginstall -c -m 0644 post-receive-email $(CONTHOOKS) )
	@$(MAKECOOKIE)

NAME = git
VERSION = 1.7.12
#PATCHLEVEL = rc4
DISTNAME = $(NAME)-$(VERSION)
CATEGORIES = devel
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

VENDOR_URL = http://git-scm.org/

# the getpassphrase patch is a non-build-related fix; mantis 4943
# polish for upstream, but local for now
VERSION_FLAG_PATCH = 1

NO_SVN_TESTS=YesPlease
GIT_TEST_OPTS=-i -v -d
EXTRA_TEST_EXPORTS = NO_SVN_TESTS GIT_TEST_OPTS

# disable tests until next version bump (at the top so it stands out)
# 1.7.2.1 and 1.7.3 have a failure on current9s when fr.UFT-8 is
# detected as the first available utf8 locale.  the failure is
# harmless though.
# TEST_SCRIPTS =
TEST_TARGET = test

PACKAGES  = CSWgit CSWgitk CSWgit-gui CSWgit-svn CSWgit-cvs
PACKAGES += CSWgit-emacs CSWgit-doc CSWgit-completion CSWgit-dev

OBSOLETED_BY_CSWgit-gui = CSWgitgui
CATALOGNAME_CSWgitgui = git_gui_stub
OBSOLETED_BY_CSWgit-svn = CSWgitsvn
CATALOGNAME_CSWgitsvn = git_svn_stub
OBSOLETED_BY_CSWgit-emacs = CSWgitemacs
CATALOGNAME_CSWgitemacs = git_emacs_stub
OBSOLETED_BY_CSWgit-doc = CSWgitdoc
CATALOGNAME_CSWgitdoc = git_doc_stub
OBSOLETED_BY_CSWgit-completion = CSWgitcompletion
CATALOGNAME_CSWgitcompletion = git_completion_stub
OBSOLETED_BY_CSWgit-dev = CSWgitdevel
CATALOGNAME_CSWgitdevel = git_devel_stub
OBSOLETED_BY_CSWgit-cvs = CSWgitcvs
CATALOGNAME_CSWgitcvs = git_cvs_stub

CATALOGNAME_CSWgit = git
CATALOGNAME_CSWgit-cvs = git_cvs
CATALOGNAME_CSWgit-svn = git_svn
CATALOGNAME_CSWgit-emacs = git_emacs
CATALOGNAME_CSWgit-gui = git_gui
CATALOGNAME_CSWgit-doc = git_doc
CATALOGNAME_CSWgitk = gitk
CATALOGNAME_CSWgit-completion = git_completion
CATALOGNAME_CSWgit-dev = git_dev

ARCHALL_CSWgit-svn = 1
ARCHALL_CSWgit-cvs = 1
ARCHALL_CSWgitk = 1
ARCHALL_CSWgit-gui = 1
ARCHALL_CSWgit-emacs = 1
ARCHALL_CSWgit-doc = 1
ARCHALL_CSWgit-completion = 1

BUILD_DEP_PKGS = CSWasciidoc CSWlibssl-dev CSWxmlto CSWbash CSWlibcurl-dev
BUILD_DEP_PKGS += CSWgsed CSWgnulinks CSWperl CSWtk CSWexpat
BUILD_DEP_PKGS += CSWzlib CSWpmerror CSWpmsvn CSWcvs CSWemacs
BUILD_DEP_PKGS += CSWpython
BUILD_DEP_PKGS += CSWlibiconv-dev

RUNTIME_DEP_PKGS_CSWgit = CSWlibz1 CSWperl CSWrsync CSWlibcurl4
RUNTIME_DEP_PKGS_CSWgit += CSWosshclient CSWlibiconv2 CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgit += CSWbash CSWpmerror CSWpmtermreadkey
RUNTIME_DEP_PKGS_CSWgit += CSWpmnetsmtpssl CSWless
RUNTIME_DEP_PKGS_CSWgit += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgit += CSWlibssl1-0-0

RUNTIME_DEP_PKGS_CSWgitk = CSWgit CSWtk

RUNTIME_DEP_PKGS_CSWgit-gui = CSWgit CSWtk

RUNTIME_DEP_PKGS_CSWgit-svn = CSWgit CSWpmsvn

RUNTIME_DEP_PKGS_CSWgit-cvs = CSWgit CSWcvs CSWcvsps

RUNTIME_DEP_PKGS_CSWgit-emacs = CSWgit CSWemacscommon

RUNTIME_DEP_PKGS_CSWgit-doc = CSWgit

RUNTIME_DEP_PKGS_CSWgit-dev = CSWgit

# We include bash here even though git itself depends on it because in theory
# git could use any other POSIX compliant shell and drop the dependency...
RUNTIME_DEP_PKGS_CSWgit-completion = CSWgit CSWbash CSWbashcmplt

LICENSE = COPYING

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

SPKG_DESC_CSWgit = Fast Version Control System
SPKG_DESC_CSWgitk = Git revision tree visualiser
SPKG_DESC_CSWgit-gui = Git GUI tool
SPKG_DESC_CSWgit-svn = Git tools for working with Subversion repositories
SPKG_DESC_CSWgit-cvs = Git tools for working with CVS repositories
SPKG_DESC_CSWgit-doc = Documentation for Git
SPKG_DESC_CSWgit-emacs = Git VCS support for Emacs
SPKG_DESC_CSWgit-completion = Bash completion support for Git
SPKG_DESC_CSWgit-dev = Headers and static libraries for Git

MASTER_SITES = http://git-core.googlecode.com/files/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += CSWgit.postinstall

PATCHFILES += 0001-Update-path-in-documentation-to-be-CSW-proper.patch
PATCHFILES += 0002-Alter-the-value-of-_PATH_DEFPATH-when-paths.h-not-pr.patch
PATCHFILES += 0003-Use-bash-and-set-PATH-in-contributed-hook-file.patch
PATCHFILES += 0004-Add-OpenCSW-apache2-path-to-instaweb-search-path.patch
# this patch is required on current9s (not necessarily all sparc boxes) due
# to the selection of available utf8 locales.
PATCHFILES_isa-sparcv8 += 0005-Force-en_US.UTF-8-for-a-git-svn-test.patch
PATCHFILES += 0006-Patch-out-a-few-usr-share-references.patch

fdirs = $(bindir_install) $(mandir) $(libexecdir_install)
define _git_files
$(foreach d,$(fdirs),$(d)/.*$(1).*) $(sharedstatedir)/$(1).*
endef

PKGFILES_CSWgit-svn = $(call _git_files,git-svn)
PKGFILES_CSWgit-gui = $(call _git_files,git-gui) $(call _git_files,git-citool)
PKGFILES_CSWgitk = $(call _git_files,gitk)
PKGFILES_CSWgit-cvs = $(foreach d,$(fdirs),$(d)/.*cvs.*)
PKGFILES_CSWgit-emacs = .*emacs.*
PKGFILES_CSWgit-doc = $(docdir)/git-doc.*
PKGFILES_CSWgit-completion = .*/bash_completion.d/.*
PKGFILES_CSWgit-dev = $(includedir)/.* $(libdir)/.*

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
		all

INSTALL_ARGS = 	INSTALLDIRS=vendor \
		install-man install-html

# We want static libs installed for our devel package
MERGE_EXCLUDE_STATICLIBS =

ETCSERVICES = /opt/csw/etc/pkg/CSWgit/services

CHECKPKG_OVERRIDES_CSWgit-completion += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWgit-completion += surplus-dependency|CSWbashcmplt
CHECKPKG_OVERRIDES_CSWgit-completion += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-doc += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-doc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgit-dev += discouraged-path-in-pkgmap|/opt/csw/lib/git/libgit.a
CHECKPKG_OVERRIDES_CSWgit-dev += discouraged-path-in-pkgmap|/opt/csw/lib/git/libxdiff.a
CHECKPKG_OVERRIDES_CSWgit-dev += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWpmerror
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWosshclient
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWrsync
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWless
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWpmnetsmtpssl
CHECKPKG_OVERRIDES_CSWgit += surplus-dependency|CSWpmtermreadkey
CHECKPKG_OVERRIDES_CSWgit += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/git-config.1
CHECKPKG_OVERRIDES_CSWgit += file-with-bad-content|/usr/share|root/opt/csw/libexec/git-core/git-send-email
CHECKPKG_OVERRIDES_CSWgit += file-with-bad-content|/usr/share|root/opt/csw/share/gitweb/gitweb.cgi
CHECKPKG_OVERRIDES_CSWgit += file-with-bad-content|/usr/local|root/opt/csw/libexec/git-core/git-instaweb
CHECKPKG_OVERRIDES_CSWgit-gui += surplus-dependency|CSWtk
CHECKPKG_OVERRIDES_CSWgit-gui += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-emacs += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-cvs += surplus-dependency|CSWcvsps
CHECKPKG_OVERRIDES_CSWgit-cvs += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-cvs += surplus-dependency|CSWcvs
CHECKPKG_OVERRIDES_CSWgitk += surplus-dependency|CSWtk
CHECKPKG_OVERRIDES_CSWgitk += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-svn += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgit-svn += surplus-dependency|CSWpmsvn

include gar/category.mk

# for tail -n and to override things like, etc with the gnu counterparts
# gnu must come first so xpg4/sed isn't found first.
PATH := /opt/csw/gnu:/usr/xpg4/bin:$(PATH)

post-configure-modulated:
	@echo "Forcing GIT_TEST_CMP tool"
	@( cd $(WORKSRC); echo 'GIT_TEST_CMP=gdiff' > config.mak )
	@( cd $(WORKSRC); echo 'EXTLIBS += -lintl' > config.mak )
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
		perl -pi -e 's!/usr/share/doc/git-core!/opt/csw/share/doc/git!' post-receive-email; \
		ginstall -c -d -m 0755 $(CONTHOOKS); \
		ginstall -c -m 0644 post-receive-email $(CONTHOOKS) )
	@$(MAKECOOKIE)

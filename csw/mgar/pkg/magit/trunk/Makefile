NAME = magit
VERSION = 0.7
PATCHLEVEL = magit_0.7
CATEGORIES = utils
GARTYPE = v2

ARCHALL = 1

VENDOR_URL = http://zagadka.vm.bytemark.co.uk/magit/

DESCRIPTION = An Git Mode for Emacs
define BLURB
Magit is an interface to the version control system Git, implemented
as an extension to Emacs. 
endef

BUILD_DEP_PKGS = CSWautoconf CSWautomake CSWtexinfo CSWemacs
RUNTIME_DEP_PKGS = CSWgit CSWemacscommon CSWemacssitestart

CHECKPKG_OVERRIDES_CSWmagit += surplus-dependency|CSWemacssitestart
CHECKPKG_OVERRIDES_CSWmagit += surplus-dependency|CSWgit

GIT_REPOS = git://gitorious.org/magit/magit.git
GIT_TREEISH = $(PATCHLEVEL)

# We define upstream file regex so we can be notifed of new upstream
# software release
# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	@(cd $(WORKSRC); ./autogen.sh )
	@$(MAKECOOKIE)

# When CSWemacs sprouts a nice auto-startup facility like Redhat or
# Debian, remove this...
post-install-modulated:
	@(cd $(WORKSRC); \
		mkdir -p $(DESTDIR)/$(docdir)/$(NAME); \
		cp README AUTHORS NEWS $(DESTDIR)/$(docdir)/$(NAME) )
	@echo Setting up emacs site-start...
	@(cd $(DESTDIR); mkdir -p opt/csw/share/emacs/site-lisp/site-start.d; \
		mv opt/csw/etc/emacs/site-start.d/50magit.el opt/csw/share/emacs/site-lisp/site-start.d/magit.el )
	@(cd $(DESTDIR); rm -rf opt/csw/etc opt/csw/share/info/dir )
	@$(MAKECOOKIE)

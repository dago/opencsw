GARNAME = magit
GARVERSION = 0.7
PATCHLEVEL = magit_0.7
CATEGORIES = utils

ARCHALL = 1

DESCRIPTION = An Emacs Mode for Git
define BLURB
Magit is an interface to the version control system Git, implemented
as an extension to Emacs. 
endef

BUILD_DEP_PKGS = CSWautoconf CSWautomake CSWtexinfo CSWemacs
RUNTIME_DEP_PKGS = CSWgit CSWemacscommon

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
	@(cd $(DESTDIR); rm -rf opt/csw/etc )
	@$(MAKECOOKIE)

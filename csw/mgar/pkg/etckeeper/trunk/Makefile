GARNAME = etckeeper
GARVERSION = 0.37
CATEGORIES = utils

DESCRIPTION = Versioning for /etc
define BLURB
etckeeper is a collection of tools to let /etc be stored in a git,
mercurial, darcs, or bzr repository. It hooks into apt (and other package
managers including yum and pacman-g2) to automatically commit changes made
to /etc during package upgrades. It tracks file metadata that revison
control systems do not normally support, but that is important for /etc,
such as the permissions of /etc/shadow. It's quite modular and configurable,
while also being simple to use if you understand the basics of working with
revision control.
endef

PACKAGES = CSWetckeeper
CATALOGNAME = etckeeper
ARCHALL_CSWetckeeper = 1

PREREQUISITE_PKGS = CSWgnulinks

REQUIRED_PKGS_CSWetckeeper = CSWgit CSWbash

SPKG_DESC_CSWetckeeper = Versioning for /etc

LICENSE_CSWetckeeper = GPL

GIT_REPOS = git://git.kitenet.net/etckeeper.git
GIT_TREEISH_etckeeper.git = 0.37
GIT_USE_PROXY = 1
PATCHFILES = autoconf.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 


sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-vcs=git --with-highlevel=apt --with-lowlevel=dpkg
CONFIGURE_ARGS += --disable-bash-completion --disable-cruft-filter

BUILD_SCRIPTS =

TEST_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	@(cd $(WORKSRC); aclocal; autoconf; automake --add-missing --foreign )
	@$(MAKECOOKIE)

post-install-modulated:
	( for d in apt; do \
		dir=$(DESTDIR)$(sysconfdir)/$$d; \
		[ -d $$dir ] && rm -rf $$dir; \
	    done; \
	  mkdir -p $(DESTDIR)/$(docdir)/$(GARNAME); \
	  gzip -c -9 $(WORKSRC)/README > $(DESTDIR)/$(docdir)/$(GARNAME)/README.gz  )
	@$(MAKECOOKIE)

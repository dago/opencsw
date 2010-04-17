GARNAME = gar_devel
GARVERSION = 1.0
CATEGORIES = devel

VENDOR_URL = http://opencsw.org

DESCRIPTION = Ease setting up a GAR development environment
define BLURB
Pull in all packages required to get started developing OpenCSW packages
with GAR.
endef

ARCHALL = 1
PACKAGES = CSWgardevel
CATALOGNAME_CSWgardevel = gar_devel

# git and netcat are required if a GAR repo is tracking a git repo instead
# of upstream tarballs.  svn is required for commiting gar recipes
RUNTIME_DEP_PKGS_CSWgardevel  = CSWgmake CSWgtar CSWggrep CSWdiffutils
RUNTIME_DEP_PKGS_CSWgardevel += CSWwget CSWfindutils CSWgsed CSWcoreutils
RUNTIME_DEP_PKGS_CSWgardevel += CSWgawk CSWbzip2 CSWlftp CSWgit CSWnetcat
RUNTIME_DEP_PKGS_CSWgardevel += CSWsvn CSWpython CSWpy-cheetah

MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWgardevel += unidentified-dependency|CSWcoreutils

include gar/category.mk

install-custom: DOCDIR=$(DESTDIR)/$(docdir)/$(GARNAME)
install-custom: $(WORKSRC)
	@(gmkdir -p $(DOCDIR); \
		cp $(FILEDIR)/README.csw $(DOCDIR) )
	@$(MAKECOOKIE)

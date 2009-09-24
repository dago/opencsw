GARNAME = gar_devel
GARVERSION = 1.0
CATEGORIES = devel

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
REQUIRED_PKGS_CSWgardevel  = CSWgmake CSWgtar CSWggrep CSWdiffutils CSWgfile
REQUIRED_PKGS_CSWgardevel += CSWtextutils CSWwget CSWfindutils CSWgsed
REQUIRED_PKGS_CSWgardevel += CSWgawk CSWbzip2 CSWlftp CSWgit CSWnetcat
REQUIRED_PKGS_CSWgardevel += CSWsvn

MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: DOCDIR=$(DESTDIR)/$(docdir)/$(GARNAME)
install-custom: $(WORKSRC)
	@(gmkdir -p $(DOCDIR); \
		cp $(FILEDIR)/README.csw $(DOCDIR) )
	@$(MAKECOOKIE)

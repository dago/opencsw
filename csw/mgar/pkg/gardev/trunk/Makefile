NAME = gar_dev
VERSION = 1.0
CATEGORIES = devel

VENDOR_URL = http://opencsw.org

DESCRIPTION = Ease setting up a GAR development environment
define BLURB
Pull in all packages required to get started developing OpenCSW packages
with GAR.
endef

ARCHALL = 1
PACKAGES = CSWgar-dev
CATALOGNAME_CSWgar-dev = gar_dev
SPKG_DESC_CSWgar-dev = $(DESCRIPTION)
OBSOLETED_BY_CSWgar-dev = CSWgardevel

# git and netcat are required if a GAR repo is tracking a git repo instead
# of upstream tarballs.  svn is required for commiting gar recipes
RUNTIME_DEP_PKGS_CSWgar-dev  = CSWgmake
RUNTIME_DEP_PKGS_CSWgar-dev += CSWbzip2
RUNTIME_DEP_PKGS_CSWgar-dev += CSWcoreutils
RUNTIME_DEP_PKGS_CSWgar-dev += CSWdiffutils
RUNTIME_DEP_PKGS_CSWgar-dev += CSWfindutils
RUNTIME_DEP_PKGS_CSWgar-dev += CSWgawk
RUNTIME_DEP_PKGS_CSWgar-dev += CSWgfile
RUNTIME_DEP_PKGS_CSWgar-dev += CSWggrep
RUNTIME_DEP_PKGS_CSWgar-dev += CSWgit
RUNTIME_DEP_PKGS_CSWgar-dev += CSWgsed
RUNTIME_DEP_PKGS_CSWgar-dev += CSWgtar
RUNTIME_DEP_PKGS_CSWgar-dev += CSWlftp
RUNTIME_DEP_PKGS_CSWgar-dev += CSWnetcat
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-cheetah
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-curl
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-hachoir-core
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-hachoir-parser
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-libmagic
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-mako
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-mox
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpymysql
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-progressbar
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-sqlobject
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-unittest2
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-yaml
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpython
RUNTIME_DEP_PKGS_CSWgar-dev += CSWsvn
RUNTIME_DEP_PKGS_CSWgar-dev += CSWwget
RUNTIME_DEP_PKGS_CSWgar-dev += CSWxz

MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWgar-dev += archall-devel-package

include gar/category.mk

install-custom: DOCDIR=$(DESTDIR)/$(docdir)/gar_dev
install-custom: OBS_DOCDIR=$(DESTDIR)/$(docdir)/gardevel_stub
install-custom: $(WORKSRC)
	@(gmkdir -p $(DOCDIR) $(OBS_DOCDIR); \
		cp $(FILEDIR)/README.csw $(DOCDIR); \
		echo 'This is a dummy package, covered by a dummy license.' >> $(DOCDIR)/license; \
		echo 'This is a dummy package, covered by a dummy license.' >> $(OBS_DOCDIR)/license)
	@$(MAKECOOKIE)

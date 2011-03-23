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
OBSOLETES_CSWgar-dev = CSWgardevel

# not sure why this is required...getting odd results in this one.
CATALOGNAME_CSWgardevel = gardevel

# git and netcat are required if a GAR repo is tracking a git repo instead
# of upstream tarballs.  svn is required for commiting gar recipes
RUNTIME_DEP_PKGS_CSWgar-dev  = CSWgmake CSWgtar CSWggrep CSWdiffutils
RUNTIME_DEP_PKGS_CSWgar-dev += CSWwget CSWfindutils CSWgsed CSWcoreutils
RUNTIME_DEP_PKGS_CSWgar-dev += CSWgawk CSWbzip2 CSWlftp CSWgit CSWnetcat
RUNTIME_DEP_PKGS_CSWgar-dev += CSWsvn CSWpython CSWpy-cheetah
RUNTIME_DEP_PKGS_CSWgar-dev += CSWxz CSWgfile CSWpy-hachoir-core
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-hachoir-parser CSWpy-libmagic
RUNTIME_DEP_PKGS_CSWgar-dev += CSWpy-progressbar CSWpy-sqlobject CSWpy-yaml

MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWgar-dev += archall-devel-package
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWlftp
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWgmake
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWgsed
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWggrep
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWgtar
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWwget
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWfindutils
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-cheetah
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWbzip2
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWsvn
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWgawk
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWdiffutils
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWnetcat
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWxz
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWgfile
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-hachoir-core
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-hachoir-parser
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-libmagic
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-progressbar
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-sqlobject
CHECKPKG_OVERRIDES_CSWgar-dev += surplus-dependency|CSWpy-yaml

include gar/category.mk

install-custom: DOCDIR=$(DESTDIR)/$(docdir)/gar_dev
install-custom: OBS_DOCDIR=$(DESTDIR)/$(docdir)/gardevel
install-custom: $(WORKSRC)
	@(gmkdir -p $(DOCDIR) $(OBS_DOCDIR); \
		cp $(FILEDIR)/README.csw $(DOCDIR); \
		echo 'This is a dummy package, covered by a dummy license.' >> $(DOCDIR)/license; \
		echo 'This is a dummy package, covered by a dummy license.' >> $(OBS_DOCDIR)/license)
	@$(MAKECOOKIE)

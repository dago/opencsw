NAME = gar_devel
VERSION = 1.0
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
RUNTIME_DEP_PKGS_CSWgardevel += CSWxz CSWgfile CSWpy-hachoir-core
RUNTIME_DEP_PKGS_CSWgardevel += CSWpy-hachoir-parser CSWpy-libmagic
RUNTIME_DEP_PKGS_CSWgardevel += CSWpy-progressbar CSWpy-sqlobject CSWpy-yaml

MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWgardevel += archall-devel-package
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWlftp
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWgmake
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWgsed
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWggrep
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWgtar
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWwget
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWfindutils
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-cheetah
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWbzip2
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWsvn
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWgit
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWgawk
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWdiffutils
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWnetcat
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWxz
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWgfile
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-hachoir-core
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-hachoir-parser
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-libmagic
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-progressbar
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-sqlobject
CHECKPKG_OVERRIDES_CSWgardevel += surplus-dependency|CSWpy-yaml

include gar/category.mk

install-custom: DOCDIR=$(DESTDIR)/$(docdir)/$(NAME)
install-custom: $(WORKSRC)
	@(gmkdir -p $(DOCDIR); \
		cp $(FILEDIR)/README.csw $(DOCDIR); \
		echo 'This is a dummy package, covered by a dummy license.' >> $(DOCDIR)/license)
	@$(MAKECOOKIE)

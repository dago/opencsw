NAME = tig
VERSION = 0.18
CATEGORIES = utils

DESCRIPTION = A git repository browser
define BLURB
Tig is a git repository browser that additionally can act as a pager
for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.
endef

MASTER_SITES = http://jonas.nitro.dk/tig/releases/
DISTFILES = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://jonas.nitro.dk/tig/

BUILD_DEP_PKGS += CSWncurses
BUILD_DEP_PKGS += CSWasciidoc
BUILD_DEP_PKGS += CSWxmlto
BUILD_DEP_PKGS += CSWiconv

RUNTIME_DEP_PKGS += CSWncurses
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWgit
# Yes, we do need git
CHECKPKG_OVERRIDES_CSWtig += surplus-dependency|CSWgit

GARCOMPILER = GNU

sysconfdir = /etc/opt/csw

EXTRA_CPPFLAGS = -I$(includedir)/ncursesw

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=$(prefix)

TEST_SCRIPTS =

INSTALL_ARGS = install install-doc

include gar/category.mk

# For GNU install to be available as "install"
PATH := /opt/csw/gnu:$(PATH)

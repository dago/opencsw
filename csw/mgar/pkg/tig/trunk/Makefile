NAME = tig
VERSION = 1.2.1
CATEGORIES = utils
GARTYPE = v2

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

BUlibncurses-dev
BUILD_DEP_PKGS += CSWasciidoc
BUILD_DEP_PKGS += CSWxmlto
BUILD_DEP_PKGS += CSWlibiconv-deDEP_PKGS += CSWiconv

RUNTIME_DEP_PKGS += CSWlibncursesw5
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWgit
# Yes, we do need git
CHECKPKG_OVERRIDES_CSWtig += surplus-dependency|CSWgit

ir = /etc/opt/csw

EXTRA_CPPFLAGS = -I$(includedir)/ncursesw

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-l# There is no testsuite
TEST_SCRIPTS =

# For GNU install to be available as "install"
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

# Installer uses $(...) idiom not available in /bin/sh
# CONFIG_SHELL is correctly detected as /bin/bash, but not used during make invocation
INSTALL_ARGS = SHELL=/opt/csw/bin/bash install install-doc 

include gar/category.mk


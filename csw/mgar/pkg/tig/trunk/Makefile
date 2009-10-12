GARNAME = tig
GARVERSION = 0.14.1
CATEGORIES = utils
PATCHLEVEL = 1e69632

DESCRIPTION = A git repository browser
define BLURB
Tig is a git repository browser that additionally can act as a pager
for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.
endef

GARCOMPILER = GNU

PREREQUISITE_PKGS = CSWncurses CSWasciidoc CSWxmlto CSWiconv

REQUIRED_PKGS = CSWncurses CSWiconv CSWgit CSWgcc4corert

GIT_REPOS = http://jonas.nitro.dk/tig/tig.git
GIT_TREEISH_tig.git = $(PATCHLEVEL)

PATCHFILES = 0001-add-install-detection-to-the-autoconf-setup.patch

sysconfdir = /etc/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=$(prefix)

TEST_SCRIPTS =

INSTALL_ARGS = install install-doc

include gar/category.mk

# Set a slightly altered revstamp to indicate that we're not using a
# pressed release.
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PATCHLEVEL)

# automake isn't used, but we want install-sh.  automake exits 1, so
# we run true after to keep gmake happy
pre-configure-modulated:
	@(cd $(WORKSRC); autoreconf; automake --add-missing; true)
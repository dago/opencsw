GARNAME = tig
GARVERSION = 0.14.1
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

PREREQUISITE_PKGS = CSWncurses CSWasciidoc CSWxmlto CSWiconv

GIT_REPOS = http://jonas.nitro.dk/tig/tig.git
GIT_TREEISH_tig.git = $(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

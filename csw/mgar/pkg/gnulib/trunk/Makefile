# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnulib
VERSION = X.Y
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = ISO C / POSIX substitutes part of gnulib
define BLURB
endef

GIT_REPOS = git://git.savannah.gnu.org/gnulib.git
GIT_USE_PROXY = 1

VENDOR_URL = http://www.gnu.org/software/gnulib/manual/html_node/POSIX-Substitutes-Library.html

WORKSRC = $(WORKDIR)/posixlib

include gar/category.mk

post-extract-modulated:
	-cd $(WORKDIR)/$(NAME)-$(VERSION) && ./gnulib-tool --create-testdir --source-base=lib \
                 --dir=$(abspath $(WORKSRC)) `./posix-modules`


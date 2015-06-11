# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# * next release don't use readline anymore (https://www.fossil-scm.org/fossil/info/851485657643dc2c)
# Recipe sent in by Freddy DISSAUX freddy.dsx free.fr

NAME = fossil
VERSION = 1.33
GARTYPE = v2

DESCRIPTION = DSCM with built-in wiki, http interface and server, tickets database
define BLURB
Fossil is an easy-to-use Distributed Source Control Management system (DSCM)
which supports access and administration over HTTP CGI or via a built-in HTTP
server, has a built-in wiki, file browser, ticket system, and more.
endef

MASTER_SITES = http://www.fossil-scm.org/download/
DISTFILES = $(NAME)-src-$(VERSION).tar.gz

VENDOR_URL = http://www.fossil-scm.org/

BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibz-dev

BUILD64 = 1

WORKSRC = $(WORKDIR)/$(NAME)-src-$(VERSION)

NODIRPATHS += --exec_prefix

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=auto
CONFIGURE_ARGS += --with-zlib=$(includedir)
CONFIGURE_ARGS += --disable-fusefs
# Find libreadline always fail
CONFIGURE_ARGS += --disable-lineedit

# No test/check target provided by fossil
TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWfossil += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWfossil += CSWlibz1

include gar/category.mk

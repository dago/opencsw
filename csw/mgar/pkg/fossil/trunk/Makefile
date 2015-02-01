# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# Recipe sent in by Freddy DISSAUX freddy.dsx free.fr
NAME = fossil
VERSION = 1.30
GARTYPE = v2
GARCOMPILER = GNU
DISTVERSION = 20150119112900
DESCRIPTION = DSCM with built-in wiki, http interface and server, tickets database
define BLURB
Fossil is an easy-to-use Distributed Source Control Management system (DSCM)
which supports access and administration over HTTP CGI or via a built-in HTTP
server, has a built-in wiki, file browser, ticket system, and more.
endef
VENDOR_URL = http://www.fossil-scm.org/

MASTER_SITES = http://www.fossil-scm.org/download/
DISTFILES = $(NAME)-src-$(DISTVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(NAME)-src-$(DISTVERSION)
PATCHDIR = $(WORKSRC)

BUILD_DEP_PKGS = CSWlibssl-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=$(includedir)

# Remove exec_prefix from DIRPATHS:
NODIRPATHS += --exec_prefix=/opt/csw
# No test/check target provided by fossil
TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWfossil = CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWfossil += CSWlibz1
RUNTIME_DEP_PKGS_CSWfossil += CSWlibreadline6

include gar/category.mk

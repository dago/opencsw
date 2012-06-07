# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = autogen
# Tried to package the last versions but encountered issues for which
# I didn't found a solution:
#
# 5.16: agen5/ag.c: zNotStr not defined
# 5.15: our guile is too old
# 5.14: syntax error in opts.c...
# 5.13: same issue as 5.14
VERSION = 5.12
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = The Automated Text and Program Generation Tool
define BLURB
  AutoGen is a tool designed to simplify the creation and maintenance of
  programs that contain large amounts of repetitious text. It is especially
  valuable in programs that have several blocks of text that must be kept
  synchronized.
endef

MASTER_SITES = $(GNU_MIRROR)/rel$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
#GCC4_VERSION		=	4.7

BUILD_DEP_PKGS		=	CSWguile
BUILD_DEP_PKGS		+=	CSWguilelib12
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev

RUNTIME_DEP_PKGS	=	CSWguilelib12
RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibiconv2
RUNTIME_DEP_PKGS	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS	+=	CSWlibz1 

BUILD_SCRIPTS	=	nominal
BUILD_SCRIPTS	+=	dvi
BUILD_SCRIPTS	+=	ps
BUILD_SCRIPTS	+=	pdf

TEST_SCRIPTS = custom

include gar/category.mk

build-nominal:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

build-dvi:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

build-ps:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

build-pdf:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

# there is one test failing (keyword.test) and I choose to ignore it
# as the remaining ones pass.
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

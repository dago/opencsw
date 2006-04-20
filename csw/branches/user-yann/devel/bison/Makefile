GARNAME = bison
GARVERSION = 1.875
CATEGORIES = devel

SPKG_PKGNAME = CSWbison
SPKG_BITNAME = bison

DESCRIPTION = GNU Project parser generator (yacc replacement)
define BLURB
  Bison is a parser generator in the style of yacc(1). It should be upwardly
  compatible with input files designed for yacc.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk


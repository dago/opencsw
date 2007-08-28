GARNAME = bison
GARVERSION = 2.3
CATEGORIES = devel

DESCRIPTION = GNU Project parser generator (yacc replacement)
define BLURB
  Bison is a parser generator in the style of yacc(1). It should be upwardly
  compatible with input files designed for yacc.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWbison,depend prototype)

TAR_ARGS =
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk

post-install:
	(cd $(DESTDIR)$(prefix)/bin; \
	/usr/ccs/bin/strip bison; \
	/usr/ccs/bin/mcs -d bison; \
	mv yacc gyacc)

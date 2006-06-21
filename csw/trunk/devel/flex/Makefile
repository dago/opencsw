GARNAME = flex
GARVERSION = 2.5.33
CATEGORIES = devel

DESCRIPTION = A tool for generating text-scanning programs.
define BLURB
  Flex is a tool for generating programs that recognize lexical patterns in
  text.  There are many applications for Flex, including writing compilers in
  conjunction with GNU Bison. Flex is a free implementation of the well known
  Lex program. It features a Lex compatibility mode, and also provides several
  new features such as exclusive start conditions.
endef

SPKG_SOURCEURL = http://flex.sourceforge.net/

SF_PROJ = lex
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = flex-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += CSWflex-new.gspec

# Fix lvalue assignment on fdopen()
PATCHFILES = suncc.diff

DEPENDS = devel/bison

CONFIGURE_ARGS = --prefix=$(prefix)/$(GARNAME)-$(GARVERSION)

TEST_TARGET = check
ENABLE_TEST = 0

include ../category.mk

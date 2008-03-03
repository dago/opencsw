GARNAME = flex
GARVERSION = 2.5.34
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

SF_PROJ = flex
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = flex-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += $(call admfiles,CSWflex-new,depend prototype)

DEPENDS = devel/bison

CONFIGURE_ARGS = --prefix=$(libexecdir)/$(GARNAME)-$(GARVERSION)

TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk

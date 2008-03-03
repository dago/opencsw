GARNAME = flex
GARVERSION = 2.5.4
CATEGORIES = devel

DESCRIPTION = older version of the 'flex' parser generator
define BLURB
  Flex is a tool for generating programs that recognize lexical patterns in
  text.  There are many applications for Flex, including writing compilers in
  conjunction with GNU Bison. Flex is a free implementation of the well known
  Lex program. It features a Lex compatibility mode, and also provides several
  new features such as exclusive start conditions.
endef

MASTER_SITES = $(GNU_NMIRROR)
DISTFILES  = $(DISTNAME)a.tar.gz
DISTFILES += CSWflex.gspec CSWflex.prototype

# Force Makefile to honor DESTDIR
PATCHFILES += install.diff

#DEPENDS = devel/bison

CONFIGURE_ARGS = --prefix=$(prefix)

include gar/category.mk

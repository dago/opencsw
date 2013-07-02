NAME = flex
VERSION = 2.5.4
GARTYPE = v1
CATEGORIES = devel

DESCRIPTION = older version of the 'flex' parser generator
define BLURB
  Flex is a tool for generating programs that recognize lexical patterns in
  text.  There are many applications for Flex, including writing compilers in
  conjunction with GNU Bison. Flex is a free implementation of the well known
  Lex program. It features a Lex compatibility mode, and also provides several
  new features such as exclusive start SF_PROJ = flex
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(call admfiles,CSWflex,)

# Force Makefile to honor DESTDIR
PATCHFILES += install.diffPENDS = devel/bison

CONFIGURE_ARGS = --prefix=$(prefix)

inclu
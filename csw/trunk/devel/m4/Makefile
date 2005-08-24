GARNAME = m4
GARVERSION = 1.4
CATEGORIES = devel

DESCRIPTION = Standard Unix macro processor with extensions
define BLURB
  gNU m4 is an implementation of the traditional Unix macro processor.  It is
  mostly SVR4 compatible, although it has some extensions (for example,
  handling more than 9 positional parameters to macros). GNU m4 also has
  built-in functions for including files, running shell commands, doing
  arithmetic, etc. Autoconf needs GNU m4 for generating 'configure' scripts,
  but not for running them.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS = --prefix=$(prefix)

TEST_TARGET = check

include ../category.mk

GARNAME = ruby
GARVERSION = 1.8.2
CATEGORIES = lang

SPKG_PKGNAME = CSWruby
SPKG_BITNAME = ruby

DESCRIPTION = An object-oriented language for quick and easy programming.
define BLURB
  Ruby is a language for quick and easy programming. Similar in scope to Perl
  and Python, it has high-level data types, automatic memory management,
  dynamic typing, a module system, exceptions, and a rich standard library.
  What sets Ruby apart is a clean and consistent language design where
  everything is an object. Other distinguishing features are CLU-style
  iterators for loop abstraction, singleton classes/methods and lexical
  closures.
endef

MASTER_SITES = ftp://www.ibiblio.org/pub/languages/ruby/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

LIBDEPS += lib/ncurses

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

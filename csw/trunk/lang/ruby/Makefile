GARNAME = ruby
GARVERSION = 1.8.2
CATEGORIES = lang

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

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
#DISTFILES += CSWruby.gspec CSWruby.depend CSWruby.prototype
DISTFILES += CSWruby.gspec

# Compile against OSSL 0.9.8
PATCHFILES += ossl-0.9.8.diff

#LIBDEPS += lib/ncurses

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pthread
CONFIGURE_ARGS += --with-tcl-dir=$(prefix)
CONFIGURE_ARGS += --with-tk-dir=$(prefix)
CONFIGURE_ARGS += --with-dbm-dir=$(prefix)
CONFIGURE_ARGS += --with-dbm-type=db
CONFIGURE_ARGS += --with-gdbm-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-readline-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

include ../category.mk


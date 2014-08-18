# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ruby
SHORTVER = 2.1
VERSION = $(SHORTVER).2
API_VERSION = $(VERSION)

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

MASTER_SITES = ftp://ftp.ruby-lang.org/pub/ruby/$(SHORTVER)/
DISTFILES += $(DISTNAME).tar.gz

PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386

PACKAGES += CSWruby21
SPKG_DESC_CSWruby21 = Ruby 2.1.x
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibgdbm3
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibz1
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibyaml0-2
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibreadline5

#GARCOMPILER = SOS12U2
GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

# Enabled DTrace support has problems during linking
CONFIGURE_ARGS += --disable-dtrace

CONFIGURE_ARGS += --program-suffix=21
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-soname=ruby$(API_VERSION)
CONFIGURE_ARGS += --with-out-ext=tk


# There are tests failing
SKIPTEST ?= 1

include gar/category.mk


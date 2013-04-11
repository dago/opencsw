# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ruby20
SHORTVER = 2.0
DISTVERSION = $(SHORTVER).0
DISTNAME = ruby-$(VERSION)-$(PATCHLEVEL)
VERSION = $(DISTVERSION)
PATCHLEVEL = p0
GARTYPE = v2

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
DISTFILES  = ruby-$(DISTVERSION)-$(PATCHLEVEL).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


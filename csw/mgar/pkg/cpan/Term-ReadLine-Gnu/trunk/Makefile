NAME = Term-ReadLine-Gnu
VERSION = 1.20
CATEGORIES = cpan
AUTHOR = HAYASHI

DESCRIPTION = Perl extension for the GNU Readline/History Library
define BLURB
  This is an implementation of Term::ReadLine using the GNU Readline/History
  Library.
endef

DISTFILES += COPYING

BUILD_DEP_PKGS += CSWlibreadline-dev

PACKAGES += CSWpm-term-readline-gnu
SPKG_DESC_CSWpm-term-readline-gnu = Perl extension for the GNU Readline library
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpm-term-readline-gnu += CSWlibreadline6
OBSOLETED_BY_CSWpm-term-readline-gnu += CSWpmtermreadlineg
CATALOGNAME_CSWpmtermreadlineg = pm_termreadlineg_stub

REINPLACEMENTS += cswperl
REINPLACE_MATCH_cswperl = \#!/usr/local/bin/perl
REINPLACE_WITH_cswperl = \#!$(bindir)/perl
REINPLACE_FILES_cswperl += Gnu/XS.pm

include gar/category.mk

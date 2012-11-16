NAME = Crypt-SmbHash
VERSION = 0.12
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BJKUIT

DESCRIPTION = Perl SmbHash encryption module
define BLURB
  The module implements the Crypt::SmbHash interface
  methods
endef

LICENSE = README 

REINPLACEMENTS += perl
REINPLACE_MATCH_perl = /usr/local/bin/perl
REINPLACE_WITH_perl = /opt/csw/bin/perl
REINPLACE_FILES_perl += SmbHash.pm blib/man3/Crypt::SmbHash.3perl

CATALOGNAME = pm_cryptsmb
PACKAGES = CSWpm-cryptsmb
ARCHALL_CSWpm-cryptsmb = 1


include gar/category.mk

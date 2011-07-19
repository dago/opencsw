# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = PPI
VERSION = 1.215
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = ADAMK

DESCRIPTION = Parse, Analyze and Manipulate Perl (without perl)
define BLURB
  Parse, Analyze and Manipulate Perl (without perl)
endef

PACKAGES = CSWpm-ppi
CATALOGNAME = pm_ppi
ARCHALL = 1

LICENSE = LICENSE

RUNTIME_DEP_PKGS  = CSWpm-test-object
RUNTIME_DEP_PKGS += CSWpm-test-nowarnings
RUNTIME_DEP_PKGS += CSWpm-test-subcalls
RUNTIME_DEP_PKGS += CSWpmclassinspector
RUNTIME_DEP_PKGS += CSWpmclone
RUNTIME_DEP_PKGS += CSWpmfileremove
RUNTIME_DEP_PKGS += CSWpmiostring
RUNTIME_DEP_PKGS += CSWpmlistmoreutils
RUNTIME_DEP_PKGS += CSWpmparamsutil
RUNTIME_DEP_PKGS += CSWpmtaskweaken

# Unreleased packages, remove next time
CHECKPKG_OVERRIDES_CSWpm-ppi += unidentified-dependency|CSWpm-test-subcalls
CHECKPKG_OVERRIDES_CSWpm-ppi += unidentified-dependency|CSWpm-test-object

include gar/category.mk


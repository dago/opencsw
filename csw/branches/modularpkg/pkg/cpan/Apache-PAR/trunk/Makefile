GARNAME = Apache-PAR
GARVERSION = 0.30
CATEGORIES = cpan
AUTHOR = NBYRD

DESCRIPTION = PAR extension for mod_perl
define BLURB
  Apache::PAR is a framework for including Perl ARchive files in a mod_perl
  (1.x or 2.x) environment. It allows an author to package up a web
  application, including configuration, static files, Perl modules, and
  Registry and PerlRun scripts to include in a single file. This archive can
  then be moved to other locations on the same system or distributed, and
  loaded with a single set of configuration options in the Apache
  configuration.
endef

DISTFILES += CSWpmapachepar.gspec

# Test changes for MP_COMPAT_1X=0
PATCHFILES = mp2_nocompat.diff

BUILDDEPS += cpan/Apache-Test

# Tests don't quite work right with MP2
# This is acknowledged by the module maintainer -- should be fixed soon.
TEST_SCRIPTS =

include gar/category.mk

pre-test:
	@chown -R nobody:nobody $(WORKSRC)

GARNAME = Test-Builder-Tester
GARVERSION = 1.01
CATEGORIES = cpan
AUTHOR = MARKF

DESCRIPTION = test testsuites built with Test::Builder
define BLURB
  The testing system is designed to be used by performing a three step process
  for each test you wish to test. This process starts with using test_out and
  test_err in advance to declare what the testsuite you are testing will
  output with Test::Builder to stdout and stderr
endef

DISTFILES += COPYING

PACKAGES = CSWpmtstbldrtester
CATALOGNAME = pm_tstbldrtester

ARCHALL = 1

# Seems that tests might assume a newer version of Test-Simple than is
# provided with Perl 5.8.8.
TEST_SCRIPTS =

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\.3perl$$$$/ { next } \
                         { print }'

include gar/category.mk

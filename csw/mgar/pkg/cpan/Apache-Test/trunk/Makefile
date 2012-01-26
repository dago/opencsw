NAME = Apache-Test
VERSION = 1.30
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PHRED

DESCRIPTION = Test.pm wrapper with helpers for testing Apache
define BLURB
  Apache::Test is a wrapper around the standard Test.pm with helpers for
  testing an Apache server.
endef

# depends
RUNTIME_DEP_PKGS     = CSWap2prefork
BUILD_DEP_PKGS = CSWap2prefork

PACKAGES = CSWpmapachetst
CATALOGNAME = pm_apachetst

ARCHALL = 1

APACHE_TEST_HTTPD = $(prefix)/apache2/sbin/httpd
export APACHE_TEST_HTTPD

include gar/category.mk

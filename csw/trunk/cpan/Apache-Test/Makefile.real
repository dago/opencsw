GARNAME = Apache-Test
GARVERSION = 1.22
CATEGORIES = cpan
AUTHOR = GEOFF
GARCH = all

DESCRIPTION = Test.pm wrapper with helpers for testing Apache
define BLURB
  Apache::Test is a wrapper around the standard Test.pm with helpers for
  testing an Apache server.
endef

DISTFILES += CSWpmapachetst.gspec

APACHE_TEST_HTTPD = $(prefix)/apache2/sbin/httpd
export APACHE_TEST_HTTPD

include ../category.mk

GARNAME = Apache-Test
GARVERSION = 1.29
CATEGORIES = cpan
AUTHOR = PGOLLUCCI

DESCRIPTION = Test.pm wrapper with helpers for testing Apache
define BLURB
  Apache::Test is a wrapper around the standard Test.pm with helpers for
  testing an Apache server.
endef

DISTFILES = $(call admfiles,CSWpmapachetst,depend prototype)

APACHE_TEST_HTTPD = $(prefix)/apache2/sbin/httpd
export APACHE_TEST_HTTPD

include ../category.mk

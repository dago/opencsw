GARNAME = libapreq2
GARVERSION = 2.06-dev
CATEGORIES = cpan
AUTHOR = JOESUF

DESCRIPTION = methods for dealing with Apache request data
define BLURB
  Apache::Request is a subclass of the Apache class, which adds methods for
  parsing GET requests and POST requests where Content-type is one of
  application/x-www-form-urlencoded or multipart/form-data. See the libapreq(3)
  manpage for more details.
endef

DISTFILES = $(call admfiles,CSWpmapreq2,depend prototype)

DEPENDS += cpan/Apache-Test cpan/ExtUtils-XSBuilder
DEPENDS += cpan/mod_perl2

CONFIGURE_ARGS  = --enable-perl-glue
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-apache2-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-apr-config=$(bindir)/apr-config
CONFIGURE_ARGS += --with-apu-config=$(bindir)/apu-config
CONFIGURE_ARGS += --with-expat=$(prefix)

# Must be installed to test
ENABLE_TEST = 0

include ../category.mk

pre-package: test

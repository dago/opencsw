GARNAME = libapreq2
GARVERSION = 2.06-dev
CATEGORIES = cpan
AUTHOR = JOESUF

DESCRIPTION = methods for dealing with client request data
define BLURB
  Apache::Request is a subclass of the Apache class, which adds methods for
  parsing GET requests and POST requests where Content-type is one of
  application/x-www-form-urlencoded or multipart/form-data. See the libapreq(3)
  manpage for more details.
endef

DISTFILES += CSWpmapreq2.gspec

BUILDDEPS += cpan/Apache-Test cpan/ExtUtils-XSBuilder

CONFIGURE_ARGS  = --enable-perl-glue
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-apache2-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-apr-config=$(prefix)/apache2/bin/apr-config
CONFIGURE_ARGS += --with-apu-config=$(prefix)/apache2/bin/apu-config
CONFIGURE_ARGS += --with-expat=$(prefix)

include ../category.mk

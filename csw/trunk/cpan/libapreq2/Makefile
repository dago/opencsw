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

include ../category.mk

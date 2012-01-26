NAME = libapreq
VERSION = 1.34
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ISAAC

DESCRIPTION = Apache Request C Library
define BLURB
  Apache::Request is a subclass of the Apache class, which adds methods for
  parsing GET requests and POST requests where Content-type is one of
  application/x-www-form-urlencoded or multipart/form-data. See the libapreq(3)
  manpage for more details.
endef

PACKAGES = CSWpmapachereq
CATALOGNAME = 	pm_apachereq 

RUNTIME_DEP_PKGS = CSWpmapachetst CSWmodperl
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

CONFIGURE_ARGS  = -httpd /opt/csw/apache/bin/httpd
CONFIGURE_ARGS += -apxs /opt/csw/apache/bin/apxs

include gar/category.mk

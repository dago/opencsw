GARNAME = SOAP-Lite
GARVERSION = 0.710.10
CATEGORIES = cpan
AUTHOR = MKUTTER

DESCRIPTION = Client and server side SOAP implementation
define BLURB
  SOAP::Lite is a collection of Perl modules which provides a simple and
  lightweight interface to the Simple Object Access Protocol (SOAP) both on
  client and server side.
endef

REQUIRED_PKGS = CSWpmiocompress CSWpmlibwww CSWpmmimelite CSWpmmimetools CSWpmuri CSWpmxmlparser
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

PACKAGES = CSWpmsoaplite
CATALOGNAME = pm_soaplite

CONFIGURE_ARGS = --noprompt

ARCHALL = 1

include gar/category.mk


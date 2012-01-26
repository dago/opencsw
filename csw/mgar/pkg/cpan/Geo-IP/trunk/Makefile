NAME = Geo-IP
VERSION = 1.38
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BORISZ

DESCRIPTION = Look up location and network information by IP Address
define BLURB
  This Perl module enables the user to find geographical and network
  information of an IP address.
endef

DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWpmgeoip
CATALOGNAME = pm_geoip

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWgeolitedb

include gar/category.mk

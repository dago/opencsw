NAME = IP-Country
VERSION = 2.27
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NWETTERS

DESCRIPTION = Fast lookup of country codes from IP addresses
define BLURB
  Finding the home country of a client using only the IP address can be
  difficult. Looking up the domain name associated with that address can
  provide some help, but many IP address are not reverse mapped to any useful
  domain, and the most common domain (.com) offers no help when looking for
  country.
endef

DISTFILES += COPYING

PACKAGES = CSWpmipcountry
CATALOGNAME = pm_ipcountry
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmgeocountries

include gar/category.mk

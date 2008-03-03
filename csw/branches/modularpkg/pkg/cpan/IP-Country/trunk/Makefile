GARNAME = IP-Country
GARVERSION = 2.23
CATEGORIES = cpan
AUTHOR = NWETTERS

DESCRIPTION = fast lookup of country codes from IP addresses
define BLURB
  Finding the home country of a client using only the IP address can be
  difficult. Looking up the domain name associated with that address can
  provide some help, but many IP address are not reverse mapped to any useful
  domain, and the most common domain (.com) offers no help when looking for
  country.
endef

DISTFILES += CSWpmipcountry.gspec CSWpmipcountry.depend

DEPENDS += cpan/Geography-Countries

include gar/category.mk

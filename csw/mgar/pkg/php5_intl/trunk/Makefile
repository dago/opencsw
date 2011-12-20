# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = php5_intl
DISTNAME = intl-$(VERSION)
VERSION = 1.1.2
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = PHP5 Internationalization extension
define BLURB
The Internationalization extension exposes functionality of the ICU library to PHP.
endef

MASTER_SITES = http://pecl.php.net/get/
DISTFILES  = $(DISTNAME).tgz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


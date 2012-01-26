NAME = opennms
VERSION = 1.6.10
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = enterprise grade network management platform
define BLURB
  OpenNMS is an enterprise grade network management system, written in Java.
  Demo is at http://demo.opennms.org/opennms, username/pwd: demo/demo.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-source-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

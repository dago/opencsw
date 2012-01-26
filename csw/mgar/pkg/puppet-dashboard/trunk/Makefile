# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = puppet-dashboard
VERSION = 1.0.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Web interface and reporting tool for Puppet 
define BLURB
  Long description
endef

VENDOR_URL   = http://www.puppetlabs.com/puppet/related-projects/dashboard/
MASTER_SITES = http://puppetlabs.com/downloads/dashboard/
DISTFILES    = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

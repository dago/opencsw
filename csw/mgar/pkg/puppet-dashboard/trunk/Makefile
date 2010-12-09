# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
GARNAME = puppet-dashboard
GARVERSION = 1.0.0
CATEGORIES = apps

DESCRIPTION = Web interface and reporting tool for Puppet 
define BLURB
  Long description
endef

VENDOR_URL   = http://www.puppetlabs.com/puppet/related-projects/dashboard/
MASTER_SITES = http://puppetlabs.com/downloads/dashboard/
DISTFILES    = $(GARNAME)-$(GARVERSION).tgz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

GARNAME = di
GARVERSION = 4.16
CATEGORIES = utils

DESCRIPTION = Disk information utility
define BLURB
  'di' is a disk information utility, displaying everything (and more)
  that your 'df' command does. It features the ability to display your
  disk usage in whatever format you desire/prefer/are used to. It is
  designed to be portable across many platforms.
endef

MASTER_SITES = http://www.gentoo.com/di/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = 

include gar/category.mk


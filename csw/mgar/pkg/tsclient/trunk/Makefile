GARNAME = tsclient
GARVERSION = 0.140
CATEGORIES = apps

DESCRIPTION = a frontend for rdesktop and other remote desktop tool
define BLURB
endef

MASTER_SITES = http://www.gnomepro.com/tsclient/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWtsclient,)
PATCHFILES = support.c.diff
CONFIGURE_ARGS = --prefix=$(prefix) LD_OPTIONS='-lsocket -lnsl'

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =

include gar/category.mk

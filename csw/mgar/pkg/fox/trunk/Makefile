GARNAME = fox
GARVERSION = 1.4.33
CATEGORIES = lib

DESCRIPTION = Fox Toolkit runtime
define BLURB
  Fox Toolkit a C++ based Toolkit for developing Graphical User Interfaces easily and effectively
endef

MASTER_SITES = http://www.fox-toolkit.org/ftp/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWfoxrt, depend prototype )
DISTFILES += $(call admfiles,CSWfox, depend prototype )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LD=CC

CONFIGURE_ARGS = $(DIRPATHS) --enable-release --with-shape=no --with-xshm=no --disable-threadsafe

TEST_SCRIPTS =

include gar/category.mk

# change bad binary name
post-install:
	( mv $(DESTDIR)/opt/csw/bin/calculator $(DESTDIR)/opt/csw/bin/foxcalculator ) 
	@$(MAKECOOKIE)

#NOTES
# LD=CC is needed during configure
# after configer need to manually cd into source dist and run make
# then go back to GAR fox dir and gmake package to complete
# this is needed to get v8 instead of v8+ bins/libs
# need to figure out and fix but not today!

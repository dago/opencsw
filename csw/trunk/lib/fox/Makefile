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

CONFIGURE_ARGS = $(DIRPATHS) --enable-release --with-shape=no --with-xshm=no --disable-threadsafe

ENABLE_TEST = 0

include ../category.mk

# change bad binary name
post-install:
	( mv $(DESTDIR)/opt/csw/bin/calculator $(DESTDIR)/opt/csw/bin/foxcalculator ) 
	@$(MAKECOOKIE)

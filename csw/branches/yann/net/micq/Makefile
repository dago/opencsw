GARNAME = micq
GARVERSION = 0.5.1
CATEGORIES = net

DESCRIPTION = terminal-based ICQ client
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = 
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWmicq,depend)

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS += --enable-tcl --enable-ssl --enable-autopackage
CONFIGURE_ARGS += --enable-binreloc --enable-binreloc-threads

# micq doesn't have a test target
TEST_TARGET =

include ../category.mk

post-install:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/micq
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/micq

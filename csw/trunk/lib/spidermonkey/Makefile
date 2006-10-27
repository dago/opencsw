GARNAME = spidermonkey
GARVERSION = 1.5
CATEGORIES = lib

DESCRIPTION = SpiderMonkey JS library
define BLURB
  SpiderMonkey JS library
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/js/
DISTFILES  = js-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWspidermonkey,)

DISTNAME = js

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

include ../category.mk

build-custom:
	cd $(WORKSRC)/src && $(MAKE) -f Makefile.ref

install-custom:
	ginstall -d $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/*.h $(DESTDIR)$(includedir)

	ginstall -d $(DESTDIR)$(libdir)
	ginstall -D $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_DBG.OBJ/libjs.so $(DESTDIR)$(libdir)/libjs.so
	ginstall -D $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_DBG.OBJ/libjs.a $(DESTDIR)$(libdir)/libjs.a


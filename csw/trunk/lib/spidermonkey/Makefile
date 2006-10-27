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

post-patch:
	# the makefile use whoami which doesn't exist under solaris
	# it seems to be used to define special debug functions,
	# for developper only I suppose.
	# we just change it by echo to avoid error messages
	perl -pi -e 's/whoami/echo/g' $(WORKSRC)/src/config.mk

build-custom:
	cd $(WORKSRC)/src && BUILD_OPT=1 $(MAKE) -f Makefile.ref

install-custom:
	ginstall -d $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/*.h $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_OPT.OBJ/*.h $(DESTDIR)$(includedir)
	# 
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -D $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_OPT.OBJ/libjs.so $(DESTDIR)$(libdir)/libjs.so
	ginstall -D $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_OPT.OBJ/libjs.a $(DESTDIR)$(libdir)/libjs.a
	#
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -D $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_OPT.OBJ/js $(DESTDIR)$(bindir)/js
	ginstall -D $(WORKSRC)/src/$(shell uname -s)$(shell uname -r)_OPT.OBJ/jscpucfg $(DESTDIR)$(bindir)/jscpucfg


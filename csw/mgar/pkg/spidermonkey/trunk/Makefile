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
# the sun5.8 x86 config file is missing so
# we are using our own
DISTFILES += SunOS5.8_i86pc.mk

DISTNAME = js

# we find the os string used by the makefile by using
# the same code (from config.mk)
OS_ARCH := $(subst /,_,$(shell uname -s | sed /\ /s//_/))
# Attempt to differentiate between SunOS 5.4 and x86 5.4
OS_CPUARCH := $(shell uname -m)
ifeq ($(OS_CPUARCH),i86pc)
OS_RELEASE := $(shell uname -r)_$(OS_CPUARCH)
else
OS_RELEASE := $(shell uname -r)
endif
OS_CONFIG := $(OS_ARCH)$(OS_OBJTYPE)$(OS_RELEASE)

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom



include gar/category.mk

post-patch:
	# the makefile use whoami which doesn't exist under solaris
	# it seems to be used to define special debug functions,
	# for developper only I suppose.
	# we just change it by echo to avoid error messages
	perl -pi -e 's/whoami/echo/g' $(WORKSRC)/src/config.mk

pre-build:
	# if we are on x86, we install our own config file
	# and remove the lock_SunOS.s cause the makefile
	# always tries to compile it (why so ?)
	( if [ "$(OS_CPUARCH)" = "i86pc" ]; then \
		cp $(WORKDIR)/SunOS5.8_i86pc.mk $(WORKSRC)/src/config; \
		rm -f $(WORKSRC)/src/lock_SunOS.s; \
	fi )

build-custom:
	cd $(WORKSRC)/src && BUILD_OPT=1 $(MAKE) -f Makefile.ref

install-custom:
	ginstall -d $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/*.h $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/*.h $(DESTDIR)$(includedir)
	# 
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/libjs.so $(DESTDIR)$(libdir)/libjs.so
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/libjs.a $(DESTDIR)$(libdir)/libjs.a
	#
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/js $(DESTDIR)$(bindir)/js
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/jscpucfg $(DESTDIR)$(bindir)/jscpucfg


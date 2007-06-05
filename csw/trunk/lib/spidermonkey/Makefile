GARNAME = spidermonkey
#GARVERSION = 1.5
GARVERSION = 1.8.0.4
CATEGORIES = lib

DESCRIPTION = SpiderMonkey JS library
define BLURB
  SpiderMonkey JS library
endef

#MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/js/
#DISTFILES  = js-$(GARVERSION).tar.gz
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/xulrunner/releases/$(GARVERSION)/source/
DISTFILES  = xulrunner-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWspidermonkey,)
# the sun5.8 x86 config file is missing so
# we are using our own
DISTFILES += SunOS5.8_i86pc.mk SunOS5.8.mk
# editline is not provided in firefox, mozilla
# or xulrunner source so we took the one from
# http://ftp.mozilla.org/pub/mozilla.org/js/js-1.5.tar.gz
DISTFILES += editline.tar.gz

#DISTNAME = js
DISTNAME = mozilla/js

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



include ../category.mk

CFLAGS += -I$(CURDIR)/$(WORKSRC)/../nsprpub/pr/include/ -I$(CURDIR)/$(WORKSRC)/../nsprpub/pr/include/obsolete -I$(CURDIR)/$(WORKSRC)/../nsprpub/pr/src/md/mac/

post-extract:
	cp -r $(WORKDIR)/editline/ $(WORKSRC)/src

post-patch:
	# the makefile use whoami which doesn't exist under solaris
	# it seems to be used to define special debug functions,
	# for developper only I suppose.
	# we just change it by the USER variable
	perl -pi -e 's/shell whoami/USER/g' $(WORKSRC)/src/config.mk

pre-build:
	# we us our own config file
	ginstall -D $(WORKDIR)/$(OS_CONFIG).mk $(WORKSRC)/src/config/$(OS_CONFIG).mk
	# We remove the lock_SunOS.s on x86 cause the makefile
	# always tries to compile it (why so ?)
	( if [ "$(OS_CPUARCH)" = "i86pc" ]; then \
		rm -f $(WORKSRC)/src/lock_SunOS.s; \
	fi )

build-custom:
	# JS_THREADSAFE=1 
	cd $(WORKSRC)/src && BUILD_$(GARFLAVOR)=1 CFLAGS="$(CFLAGS)" $(MAKE) -f Makefile.ref

install-custom:
	ginstall -d $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/*.h $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/$(OS_CONFIG)_$(GARFLAVOR).OBJ/*.h $(DESTDIR)$(includedir)
	# 
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_$(GARFLAVOR).OBJ/libjs.so $(DESTDIR)$(libdir)/libjs.so
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_$(GARFLAVOR).OBJ/libjs.a $(DESTDIR)$(libdir)/libjs.a
	#
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_$(GARFLAVOR).OBJ/js $(DESTDIR)$(bindir)/js
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_$(GARFLAVOR).OBJ/jscpucfg $(DESTDIR)$(bindir)/jscpucfg


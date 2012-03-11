# $Id$

NAME = spidermonkey
VERSION = 1.7.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = The Mozilla SpiderMonkey JavaScript interpreter and library
define BLURB
  SpiderMonkey JS library
endef

VENDOR_URL   = http://www.mozilla.org/js/spidermonkey/
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/js/
DISTFILES    = js-$(VERSION).tar.gz

# the sun5.8 x86 config file is missing so
# we are using our own
#DISTFILES += SunOS5.8_i86pc.mk

PATCHFILES += 0001-Set-the-SONAME-of-the-shared-library.patch

prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

DISTNAME = js

LICENSE = src/README.html

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

EXTRA_CFLAGS="-DJS_C_STRINGS_ARE_UTF8"
EXTRA_CXXFLAGS="-DJS_C_STRINGS_ARE_UTF8"

PACKAGES += CSWlibjs-gxx-dev
SPKG_DESC_CSWlibjs-gxx-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibjs-gxx-dev += $(libdir)/libjs.so
PKGFILES_CSWlibjs-gxx-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibjs-gxx-dev += CSWlibjs1-7-0-gxx

PACKAGES += CSWlibjs1-7-0-gxx
PKGFILES_CSWlibjs1-7-0-gxx += $(call baseisadirs,$(libdir),libjs\.so\.1\.7\.0)
SPKG_DESC_CSWlibjs1-7-0-gxx += $(DESCRIPTION), libjs.so.1.7.0
RUNTIME_DEP_PKGS_CSWspidermonkey += CSWlibjs1-7-0-gxx

CHECKPKG_OVERRIDES_CSWlibjs1-7-0-gxx += binary-architecture-does-not-match-placement|file=opt/csw/gxx/lib/libjs.so.1.7.0|arch_id=18|arch_name=sparcv8+

include gar/category.mk

post-patch:
	# the makefile use whoami which doesn't exist under solaris
	# it seems to be used to define special debug functions,
	# for developper only I suppose.
	# we just change it by echo to avoid error messages
	perl -pi -e 's/whoami/echo/g' $(WORKSRC)/src/config.mk
	@$(MAKECOOKIE)

pre-build-modulated:
	# if we are on x86, we install our own config file
	# and remove the lock_SunOS.s cause the makefile
	# always tries to compile it (why so ?)
	( if [ "$(OS_CPUARCH)" = "i86pc" ]; then \
		cp $(WORKDIR)/SunOS5.8_i86pc.mk $(WORKSRC)/src/config; \
		rm -f $(WORKSRC)/src/lock_SunOS.s; \
	fi )
	@$(MAKECOOKIE)

build-custom:
	# Looks like it doesn't work with parallel builds.
	# $(PARALLELMFLAGS)
	cd $(WORKSRC)/src && BUILD_OPT=1 $(MAKE) -f Makefile.ref
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/*.h $(DESTDIR)$(includedir)
	cp $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/*.h $(DESTDIR)$(includedir)
	# 
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/libjs.so $(DESTDIR)$(libdir)/libjs.so
	# ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/libjs.a $(DESTDIR)$(libdir)/libjs.a
	(cd $(DESTDIR)/$(libdir); mv libjs.so libjs.so.1.7.0; ln -s libjs.so.1.7.0 libjs.so)
	#
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/js $(DESTDIR)$(bindir)/js
	ginstall -D $(WORKSRC)/src/$(OS_CONFIG)_OPT.OBJ/jscpucfg $(DESTDIR)$(bindir)/jscpucfg
	@$(MAKECOOKIE)

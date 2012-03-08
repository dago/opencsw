# $Id$

NAME = spidermonkey
VERSION = 1.0.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = The Mozilla SpiderMonkey JavaScript interpreter and library
define BLURB
  SpiderMonkey JS library
endef

VENDOR_URL   = http://www.mozilla.org/js/spidermonkey/
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/js/
DISTFILES    = js185-$(VERSION).tar.gz

# the sun5.8 x86 config file is missing so
# we are using our own
#DISTFILES += SunOS5.8_i86pc.mk

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
prefix = $(BUILD_PREFIX)/gxx

DISTNAME = js-1.8.5

# # we find the os string used by the makefile by using
# # the same code (from config.mk)
# OS_ARCH := $(subst /,_,$(shell uname -s | sed /\ /s//_/))
# # Attempt to differentiate between SunOS 5.4 and x86 5.4
# OS_CPUARCH := $(shell uname -m)
# ifeq ($(OS_CPUARCH),i86pc)
# OS_RELEASE := $(shell uname -r)_$(OS_CPUARCH)
# else
# OS_RELEASE := $(shell uname -r)
# endif
# OS_CONFIG := $(OS_ARCH)$(OS_OBJTYPE)$(OS_RELEASE)

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

GARCOMPILER = GNU

BUILD_DEP_PKGS = CSWautoconf2-13
BUILD_DEP_PKGS += CSWnspr-dev
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWgcc4g++

include gar/category.mk

post-patch:
	# the makefile use whoami which doesn't exist under solaris
	# it seems to be used to define special debug functions,
	# for developper only I suppose.
	# we just change it by echo to avoid error messages
	# perl -pi -e 's/whoami/echo/g' $(WORKSRC)/src/config.mk

pre-configure-modulated:
	(cd $(WORKSRC)/js/src && autoconf-2.13)
	@$(MAKECOOKIE)

configure-custom:
	(cd $(WORKSRC)/js && mkdir -p objdir && cd objdir && \
	CFLAGS="-DJS_C_STRINGS_ARE_UTF8" \
	       CXXFLAGS="-fshort-enums -DJS_C_STRINGS_ARE_UTF8" \
	       CXX=/opt/csw/bin/g++ CC=/opt/csw/bin/gcc \
	       ../src/configure \
	       --disable-pedantic \
	       --with-nspr-prefix=/opt/csw \
	       --prefix=/opt/csw/gxx \
	       --with-system-nspr)
	@$(MAKECOOKIE)

disabled-pre-build:
	# if we are on x86, we install our own config file
	# and remove the lock_SunOS.s cause the makefile
	# always tries to compile it (why so ?)
	# ( if [ "$(OS_CPUARCH)" = "i86pc" ]; then \
	# 	cp $(WORKDIR)/SunOS5.8_i86pc.mk $(WORKSRC)/src/config; \
	# 	rm -f $(WORKSRC)/src/lock_SunOS.s; \
	# fi )

build-custom:
	# cd $(WORKSRC)/js/src && DISABLE_JIT=1 BUILD_OPT=1 $(MAKE) -f Makefile.ref
	cd $(WORKSRC)/js/objdir && $(MAKE)
	@$(MAKECOOKIE)

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


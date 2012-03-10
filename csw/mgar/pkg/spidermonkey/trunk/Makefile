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

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
prefix = $(BUILD_PREFIX)/gxx

DISTNAME = js-1.8.5

PATCHFILES += 0001-Do-not-use-fpclassify-on-Solaris.patch
PATCHFILES += 0002-Specify-the-right-SONAME-for-the-library.patch

LICENSE = js/src/README.html

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

GARCOMPILER = GNU

BUILD_DEP_PKGS = CSWautoconf2-13
BUILD_DEP_PKGS += CSWnspr-dev
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWgcc4g++

PACKAGES = CSWlibmozjs185-gxx-dev
SPKG_DESC_CSWlibmozjs185-gxx-dev += $(DESCRIPTION), header files
PKGFILES_CSWlibmozjs185-gxx-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibmozjs185-gxx-dev += $(libdir)/libmozjs185.so

PACKAGES += CSWlibmozjs185-gxx
PKGFILES_CSWlibmozjs185-gxx += $(call baseisadirs,$(libdir),libmozjs185\.so\.1\.0\.0)
SPKG_DESC_CSWlibmozjs185-gxx += $(DESCRIPTION), libmozjs185.so
RUNTIME_DEP_PKGS_CSWlibmozjs185-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmozjs185-gxx += CSWlibstdc++6

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
	       --with-system-nspr \
	       --enable-threadsasafe \
	       --with-ctypes)
	@$(MAKECOOKIE)

build-custom:
	# cd $(WORKSRC)/js/src && DISABLE_JIT=1 BUILD_OPT=1 $(MAKE) -f Makefile.ref
	cd $(WORKSRC)/js/objdir && $(MAKE) $(PARALLELMFLAGS)
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC)/js/objdir && $(MAKE) $(INSTALL_ENV) install
	# Symlinks after installation are broken: they use absolute paths.
	grm -v $(DESTDIR)/opt/csw/gxx/lib/libmozjs185.so
	grm -v $(DESTDIR)/opt/csw/gxx/lib/libmozjs185.so.1.0
	gln -vs libmozjs185.so.1.0 $(DESTDIR)/opt/csw/gxx/lib/libmozjs185.so
	gln -vs libmozjs185.so.1.0.0 $(DESTDIR)/opt/csw/gxx/lib/libmozjs185.so.1.0
	@$(MAKECOOKIE)

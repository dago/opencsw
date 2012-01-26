# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# Based on the following resources:
# - http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/nspr/nspr-4.8.ebuild?view=markup
# - https://developer.mozilla.org/En/NSPR_build_instructions

NAME = nspr
MAJOR_VERSION = 4
MIN_VERSION = 8.9
VERSION = $(MAJOR_VERSION).$(MIN_VERSION)
CATEGORIES = lib
GARTYPE = v2

define BLURB
  Netscape Portable Runtime (NSPR) provides a platform-neutral API for system
  level and libc like functions. The API is used in the Mozilla clients and
  many of Red Hat's, Sun's, and other software offerings.
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$(VERSION)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
PATCHFILES  = nspr-4.6.1-config.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES = CSWnspr-dev
CATALOGNAME_CSWnspr-dev = nspr_dev
SPKG_DESC_CSWnspr-dev = Netscape Portable Runtime, header files
# PKGFILES_CSWnspr-dev += $(prefix)/include.*
# PKGFILES_CSWnspr-dev += $(bindir).*nspr-config
# PKGFILES_CSWnspr-dev += .*/nspr\.pc
# PKGFILES_CSWnspr-dev += .*compile-et\.pl
RUNTIME_DEP_PKGS_CSWnspr-dev  = CSWlibnspr4
RUNTIME_DEP_PKGS_CSWnspr-dev += CSWperl
OBSOLETED_BY_CSWnspr-dev = CSWnspr-devel
OBSOLETED_BY_CSWnspr-dev += CSWmozilla
OBSOLETED_BY_CSWnspr-dev += CSWsunbird
INCOMPATIBLE_PKGS_CSWnspr-dev = CSWmozilla
INCOMPATIBLE_PKGS_CSWnspr-dev += CSWsunbird

# Library splits

PACKAGES += CSWlibnspr4
CATALOGNAME_CSWlibnspr4 = libnspr4
SPKG_DESC_CSWlibnspr4 = Netscape Portable Runtime, libnspr4.so
PKGFILES_CSWlibnspr4 += $(call baseisadirs,$(libdir),libnspr4.so)
OBSOLETED_BY_CSWlibnspr4 = CSWnspr
CHECKPKG_OVERRIDES_CSWlibnspr4 += soname-equals-filename

PACKAGES += CSWlibplc4
CATALOGNAME_CSWlibplc4 = libplc4
SPKG_DESC_CSWlibplc4 = Netscape Portable Runtime, libplc4.so
PKGFILES_CSWlibplc4 += $(call baseisadirs,$(libdir),libplc4.so)
RUNTIME_DEP_PKGS_CSWlibplc4 += CSWlibnspr4
CHECKPKG_OVERRIDES_CSWlibplc4 += soname-equals-filename

PACKAGES += CSWlibplds4
CATALOGNAME_CSWlibplds4 = libplds4
SPKG_DESC_CSWlibplds4 = Netscape Portable Runtime, libplds4.so
PKGFILES_CSWlibplds4 += $(call baseisadirs,$(libdir),libplds4.so)
RUNTIME_DEP_PKGS_CSWlibplds4 += CSWlibnspr4
CHECKPKG_OVERRIDES_CSWlibplds4 += soname-equals-filename

PACKAGES += CSWlibnspr-flt4
CATALOGNAME_CSWlibnspr-flt4 = libnspr_flt4
SPKG_DESC_CSWlibnspr-flt4 = Netscape Portable Runtime, libnspr-flt4.so
PKGFILES_CSWlibnspr-flt4 += $(libdir).*/libnspr_flt4\.so
CHECKPKG_OVERRIDES_CSWlibnspr-flt4 += soname-equals-filename

PERL = /opt/csw/bin/perl


CONFIGURE_SCRIPTS = nspr
BUILD_SCRIPTS = nspr
# TEST_SCRIPTS = nspr
# Some tests are failing
TEST_SCRIPTS =
INSTALL_SCRIPTS = nspr

export PERL

localstatedir = /var/opt/csw
sysconfdir = /etc/opt/csw
# Move the include files to include/nspr to prevent polluting the main
# header file namespace.
includedir = $(prefix)/include/nspr

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS_isa-sparcv9 = --enable-64bit
CONFIGURE_ARGS_isa-amd64 = --enable-64bit
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))
CONFIGURE_ARGS_OPT += --enable-optimize="-xO3"
CONFIGURE_ARGS_OPT += --disable-debug
CONFIGURE_ARGS_OPT += --enable-strip
CONFIGURE_ARGS_DBG += --enable-debug
CONFIGURE_ARGS_DBG += --disable-strip
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

BUILD64_LIBS_ONLY = 1

LICENSE = LICENSE

# # Checkpkg suggests CSWlibp (the longest common substring), but we want the
# # three libraries to be in one package.
# CHECKPKG_OVERRIDES_CSWlibnspr4 += shared-lib-pkgname-mismatch

CPPFLAGS = 

include gar/category.mk

configure-nspr:
	(cp $(FILEDIR)/LICENSE $(WORKSRC))
	(cd $(WORKSRC) && mkdir -p build inst)
	gsed -i -e 's/$$(mkshlib) $$(OBJS)/$$(MKSHLIB) $$(LDFLAGS) $$(OBJS)/g' \
		        $(WORKSRC)/mozilla/nsprpub/config/rules.mk
	cd $(WORKSRC)/build && $(CONFIGURE_ENV) ../mozilla/nsprpub/configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-nspr:
	(cd $(WORKSRC)/build && $(BUILD_ENV) gmake)
	(cd $(WORKSRC)/build/pr/tests && $(BUILD_ENV) gmake)
	@$(MAKECOOKIE)

test-nspr: test-accept test-runtests

test-accept:
	(cd $(WORKSRC)/build/pr/tests && DYLD_LIBRARY_PATH=../../dist/lib ./accept)
	@$(MAKECOOKIE)

test-runtests:
	(cd $(WORKSRC)/build/pr/tests && DYLD_LIBRARY_PATH=../../dist/lib ../../../mozilla/nsprpub/pr/tests/runtests.sh)
	@$(MAKECOOKIE)

install-nspr:
	(cd $(WORKSRC)/build && $(INSTALL_ENV) gmake install DESTDIR=$(DESTDIR))
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/build/config/nspr-config \
		$(DESTDIR)$(bindir)
	ginstall -m 755 -d $(DESTDIR)$(libdir)/pkgconfig
	ginstall -m 644 $(WORKSRC)/build/config/nspr.pc \ 
		$(DESTDIR)$(libdir)/pkgconfig
	if [ $(MEMORYMODEL) = 64 ]; then \
		gsed -i -e 's+/lib$$+lib/64+' $(DESTDIR)$(libdir)/pkgconfig/nspr.pc ; \
	fi
	rm -f $(DESTDIR)$(bindir)/prerr.properties
	rm -f $(DESTDIR)$(bindir)/nspr.pc
	@$(MAKECOOKIE)

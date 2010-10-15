# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# Based on the following resources:
# - http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/nspr/nspr-4.8.ebuild?view=markup
# - https://developer.mozilla.org/En/NSPR_build_instructions

GARNAME = nspr
MAJOR_VERSION = 4
MIN_VERSION = 8.6
GARVERSION = $(MAJOR_VERSION).$(MIN_VERSION)
CATEGORIES = lib

define BLURB
  Netscape Portable Runtime (NSPR) provides a platform-neutral API for system
  level and libc like functions. The API is used in the Mozilla clients and
  many of Red Hat's, Sun's, and other software offerings.
endef

MASTER_SITES = https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += LICENSE
PATCHFILES  = nspr-4.6.1-config.patch

PACKAGES += CSWnspr
PACKAGES += CSWnspr-devel
PACKAGES += CSWlibnspr4-devel
PACKAGES += CSWlibnspr4
PKGFILES_CSWlibnspr4-devel += $(PKGFILES_DEVEL)
PKGFILES_CSWlibnspr4-devel += $(bindir).*nspr-config
PKGFILES_CSWlibnspr4-devel += .*/nspr\.pc
PKGFILES_CSWlibnspr4-devel += .*compile-et\.pl
PKGFILES_CSWnspr         = Invisible-Pink-Unicorn
PKGFILES_CSWnspr-devel   = Flying-Spaghetti-Monster

SPKG_DESC_CSWnspr        = Empty, transitional package (CSWnspr)
SPKG_DESC_CSWnspr-devel  = Empty, transitional package (CSWnspr-devel)
SPKG_DESC_CSWlibnspr4       = Netscape Portable Runtime
SPKG_DESC_CSWlibnspr4-devel = Netscape Portable Runtime, header files
CATALOGNAME_CSWnspr-devel   = nspr_devel
CATALOGNAME_CSWlibnspr4-devel   = nspr4_devel
RUNTIME_DEP_PKGS_CSWnspr        = CSWlibnspr4
RUNTIME_DEP_PKGS_CSWnspr-devel  = CSWlibnspr4-devel
RUNTIME_DEP_PKGS_CSWlibnspr4-devel  = CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibnspr4-devel += CSWperl
ARCHALL_CSWnspr = 1

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

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

BUILD64 = 1

LICENSE = LICENSE

# Checkpkg suggests CSWlibp (the longest common substring), but we want the
# three libraries to be in one package.
CHECKPKG_OVERRIDES_CSWlibnspr4 += shared-lib-pkgname-mismatch

CHECKPKG_OVERRIDES_CSWlibnspr4-devel += surplus-dependency|CSWlibnspr4

# For transitional packages
CHECKPKG_OVERRIDES_CSWnspr += surplus-dependency|CSWlibnspr4
CHECKPKG_OVERRIDES_CSWnspr-devel += surplus-dependency|CSWlibnspr4-devel

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

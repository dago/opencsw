GARNAME = nspr
MIN_VERSION = 8
GARVERSION = 4.$(MIN_VERSION)
CATEGORIES = lib

define BLURB
  Netscape Portable Runtime (NSPR) provides a platform-neutral API for system
  level and libc like functions. The API is used in the Mozilla clients and
  many of Red Hat's, Sun's, and other software offerings.
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES  = nspr-4.6.1-config.patch

PACKAGES = CSWnspr CSWnspr-devel
PKGFILES_CSWnspr-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWnspr-devel += $(bindir).*nspr-config
PKGFILES_CSWnspr-devel += .*/nspr\.pc
PKGFILES_CSWnspr-devel += .*compile-et\.pl

SPKG_DESC_CSWnspr = Netscape Portable Runtime
SPKG_DESC_CSWnspr-devel = Netscape Portable Runtime development files
CATALOGNAME_CSWnspr-devel = nspr_devel
REQUIRED_PKGS_CSWnspr-devel = CSWnspr

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PERL = /opt/csw/bin/perl
EXTRA_CFLAGS = -xlibmil
EXTRA_CXXFLAGS = -xlibmil -xlibmopt -features=tmplife -norunpath
CONFIGURE_SCRIPTS = nspr
BUILD_SCRIPTS = nspr
TEST_SCRIPTS =
INSTALL_SCRIPTS = nspr

export PERL

libdir = $(prefix)/lib/nspr
localstatedir = /var/opt/csw
sysconfdir = /etc/opt/csw
# Move the include files to include/nspr to prevent polluting the main
# header file namespace.
includedir = $(prefix)/include/nspr

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-mozilla
CONFIGURE_ARGS += --with-native-threads
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-system-sqlite
CONFIGURE_ARGS_isa-sparcv9 = --enable-64bit
CONFIGURE_ARGS_isa-amd64 = --enable-64bit
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))
CONFIGURE_ARGS_OPT  = --enable-optimize="-xO3"
CONFIGURE_ARGS_OPT += --disable-debug
CONFIGURE_ARGS_OPT += --enable-strip
CONFIGURE_ARGS_OPT += --disable-tests
CONFIGURE_ARGS_DBG  = --enable-debug
CONFIGURE_ARGS_DBG += --disable-strip
CONFIGURE_ARGS_DBG += --enable-tests
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# These options I'm unsure about, are they really needed?
# EXTRA_LDFLAGS = -R'\$\$ORIGIN:\$\$ORIGIN/..' -R/opt/csw/lib
# prefix = /opt/csw/mozilla/nspr
# CONFIGURE_ARGS += --with-dist-prefix=$(DESTDIR)/opt/csw/mozilla/nspr
# CONFIGURE_ARGS += --with-dist-bindir=$(DESTDIR)/opt/csw/mozilla/nspr/lib

BUILD64 = 1

include gar/category.mk

configure-nspr:
	(cp $(FILEDIR)/LICENSE $(WORKSRC))
	(cd $(WORKSRC) && mkdir -p build inst)
	gsed -i -e 's/$$(mkshlib) $$(OBJS)/$$(MKSHLIB) $$(LDFLAGS) $$(OBJS)/g' \
		        $(WORKSRC)/mozilla/nsprpub/config/rules.mk
	cd $(WORKSRC)/build && $(CONFIGURE_ENV) ../mozilla/nsprpub/configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-nspr:
	(cd $(WORKSRC)/build && $(BUILD_ENV) gmake CC=$(CC) CXX=$(CXX))
	@$(MAKECOOKIE)

install-nspr:
	(cd $(WORKSRC)/build && $(INSTALL_ENV) gmake install DESTDIR=$(DESTDIR))
	(cd $(DESTDIR)/opt/csw/lib/nspr \
		&& for file in *.so; do \
			mv $${file} $${file}.$(MIN_VERSION); \
			ln -s $${file}.$(MIN_VERSION) $${file}; \
		done)
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/build/config/nspr-config \
		$(DESTDIR)$(bindir)
	ginstall -m 755 -d $(DESTDIR)$(libdir)/pkgconfig
	ginstall -m 644 $(WORKSRC)/build/config/nspr.pc \
		$(DESTDIR)$(libdir)/pkgconfig
	rm $(DESTDIR)$(bindir)/prerr.properties
	rm $(DESTDIR)$(bindir)/nspr.pc
	@$(MAKECOOKIE)

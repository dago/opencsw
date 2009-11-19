GARNAME = nspr
MIN_VERSION = 8
GARVERSION = 4.$(MIN_VERSION)
CATEGORIES = lib
# DISTNAME = $(GARNAME)

DESCRIPTION = NSPR Netscape Portable Runtime
define BLURB
  NSPR Netscape Portable Runtime
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES  = nspr-4.6.1-config.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PERL = /opt/csw/bin/perl
EXTRA_CFLAGS = -xlibmil
EXTRA_CXXFLAGS = -xlibmil -xlibmopt -features=tmplife -norunpath
EXTRA_LDFLAGS = -R'\$\$ORIGIN:\$\$ORIGIN/..' -L/opt/csw/lib -R/opt/csw/lib
CONFIGURE_SCRIPTS = nspr
BUILD_SCRIPTS = nspr
TEST_SCRIPTS =
INSTALL_SCRIPTS = nspr

# export PERL CFLAGS CXXFLAGS LDFLAGS
export PERL

# prefix = /opt/csw/mozilla/nspr
libdir = $(prefix)/lib/nspr
localstatedir = /var/opt/csw
sysconfdir = /etc/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-mozilla
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --enable-strip
CONFIGURE_ARGS += --with-native-threads
CONFIGURE_ARGS += --enable-ipv6
# CONFIGURE_ARGS += --enable-64bit
# CONFIGURE_ARGS += --with-dist-prefix=$(DESTDIR)/opt/csw/mozilla/nspr
# CONFIGURE_ARGS += --enable-optimize="-xO3"
CONFIGURE_ARGS += --disable-tests
CONFIGURE_ARGS += --enable-system-sqlite
# CONFIGURE_ARGS += --with-dist-bindir=$(DESTDIR)/opt/csw/mozilla/nspr/lib

# PATCHFILES = autoconf.mk.in.diff

include gar/category.mk

configure-nspr:
	(cp $(FILEDIR)/LICENSE $(WORKSRC))
	(cd $(WORKSRC) && mkdir build inst)
	gsed -i -e 's/$$(mkshlib) $$(OBJS)/$$(MKSHLIB) $$(LDFLAGS) $$(OBJS)/g' \
		        $(WORKSRC)/mozilla/nsprpub/config/rules.mk
	cd $(WORKSRC)/build && ../mozilla/nsprpub/configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-nspr:
	cd $(WORKSRC)/build && $(BUILD_ENV) gmake
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
	ginstall -m 755 -d $(DESTDIR)$(prefix)/pkgconfig
	ginstall -m 644 $(WORKSRC)/build/config/nspr.pc \
		$(DESTDIR)$(prefix)/pkgconfig
	rm $(DESTDIR)$(bindir)/prerr.properties
	rm $(DESTDIR)$(bindir)/nspr.pc
	@$(MAKECOOKIE)

post-install:
	# ( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | grep ELF | grep -e 'executable' -e 'dynamic lib' | grep 'not stripped' && strip {}"  \; )
	@$(MAKECOOKIE)

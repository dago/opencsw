GARNAME = nspr
GARVERSION = 4.6.6
CATEGORIES = libs
DISTNAME = $(GARNAME)

DESCRIPTION = NSPR Netscape Portable Runtime
define BLURB
NSPR Netscape Portable Runtime
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnspr, depend )
# DISTFILES += CSWnspr.depend CSWnspr.gspec CSWnspr.prototype

PERL="/opt/csw/bin/perl"
CFLAGS=-xlibmil
CXXFLAGS="-xlibmil -xlibmopt -features=tmplife -norunpath"
LDFLAGS="-R'\$\$ORIGIN:\$\$ORIGIN/..' -L/opt/csw/lib -R/opt/csw/lib"

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/nspr --mandir=/opt/csw/share/man --with-mozilla --disable-debug --enable-strip --with-native-threads --enable-ipv6 --with-dist-prefix=$(DESTDIR)/opt/csw/mozilla/nspr  --enable-optimize="-xO3" --disable-tests --with-dist-bindir=$(DESTDIR)/opt/csw/mozilla/nspr/lib

# PATCHFILES = autoconf.mk.in.diff

include gar/category.mk

post-extract:
	( mv $(WORKDIR)/$(DISTNAME)-$(GARVERSION)/mozilla/nsprpub $(WORKDIR)/$(DISTNAME) )
	( cp $(FILEDIR)/LICENSE $(WORKDIR)/$(DISTNAME) )
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | grep ELF | grep -e 'executable' -e 'dynamic lib' | grep 'not stripped' && strip {}"  \; )

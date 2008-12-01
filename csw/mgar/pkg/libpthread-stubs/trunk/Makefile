GARNAME = libpthread-stubs
GARVERSION = 0.1
CATEGORIES = lib

DESCRIPTION = pthread stubs not provided by native libc
define BLURB
This library provides weak aliases for pthread functions not provided in libc or otherwise available by default. Libraries like libxcb rely on pthread stubs to use pthreads optionally, becoming thread-safe when linked to libpthread, while avoiding any performance hit when running single-threaded. libpthread-stubs supports this behavior even on platforms which do not supply all the necessary pthread stubs. On platforms which already supply all the necessary pthread stubs, this package has no content. 
endef

MASTER_SITES =http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# DISTFILES    += CSWlibpthreadstubs.gspec CSWlibpthreadstubs.prototype CSWlibpthreadstubs.depend 
# DISTFILES    += CSWlibpthreadstubsdev.gspec CSWlibpthreadstubsdev.prototype CSWlibpthreadstubsdev.depend 
DISTFILES    += $(call admfiles,CSWlibpthreadstubs, depend)

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

TEST_SCRIPTS      = none

GREP = ggrep

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man 

test-none:
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

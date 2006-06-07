GARNAME = lyx
GARVERSION = 1.4.1
CATEGORIES = applications

DESCRIPTION = WYSIWYM document processor
define BLURB
   LyX is a document processor that encourages an approach to writing based
   on the structure of your documents, not their appearance. It is released
   under a Free Software / Open Source license.
endef

MASTER_SITES = ftp://ftp.lyx.org/pub/lyx/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlyx,depend prototype postinstall)

LD_OPTIONS = -R/opt/csw/kde-gcc/lib -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += LIBS=-laspell LDFLAGS=-laspell
CONFIGURE_ARGS += QTDIR=/opt/csw/kde-gcc
CONFIGURE_ARGS += CC=/opt/csw/gcc3/bin/gcc
CONFIGURE_ARGS += CXX=/opt/csw/gcc3/bin/g++
CONFIGURE_ARGS += CPPFLAGS='-I/opt/csw/include'
CONFIGURE_ARGS += CFLAGS=-O2
CONFIGURE_ARGS += CXXFLAGS=-O2
CONFIGURE_ARGS += --prefix=/opt/csw/kde-gcc --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib --with-pspell
CONFIGURE_ARGS += --with-frontend=qt --enable-compression-support
CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw
CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw

# lyx doesn't have a test target
TEST_TARGET =

include ../category.mk

BINFILES = $(DESTDIR)$(prefix)/kde-gcc/bin/lyx
BINFILES += $(DESTDIR)$(prefix)/kde-gcc/bin/lyxclient
BINFILES += $(DESTDIR)$(prefix)/kde-gcc/bin/tex2lyx

post-install:
	cp -p files/README.CSW $(DESTDIR)$(prefix)/kde-gcc/share/lyx/doc
	/usr/ccs/bin/strip $(BINFILES)
	/usr/ccs/bin/mcs -d $(BINFILES)

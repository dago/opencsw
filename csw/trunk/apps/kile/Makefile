GARNAME = kile
GARVERSION = 1.9.3
CATEGORIES = applications

DESCRIPTION = An integrated LaTeX environment
define BLURB
  Kile is a user friendly TeX/LaTeX editor for the KDE desktop environment. 
  KDE is available for many architectures such as PC, PowerPC (Mac for
  example) and SPARC.
endef

SF_PROJ = kile
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWkile,depend prototype)

# Compile with GCC
GARCOMPILER = GNU

LD_OPTIONS = -R/opt/csw/kde-gcc/lib -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib
PATH=/opt/csw/kde-gcc/bin:$PATH
export LD_OPTIONS PATH

CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += --with-qt-dir=/opt/csw/kde-gcc
CONFIGURE_ARGS += QTDIR=/opt/csw/kde-gcc
#CONFIGURE_ARGS += CC=/opt/csw/gcc3/bin/gcc
#CONFIGURE_ARGS += CXX=/opt/csw/gcc3/bin/g++
#CONFIGURE_ARGS += CPPFLAGS='-I/opt/csw/include'
#CONFIGURE_ARGS += CFLAGS=-O2
#CONFIGURE_ARGS += CXXFLAGS=-O2
CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/kde-gcc/lib -L/opt/csw/lib"
CONFIGURE_ARGS += --prefix=/opt/csw/kde-gcc --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib
#CONFIGURE_ARGS += --with-frontend=qt --enable-compression-support
#CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw
#CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw

CONFIGURE_ARGS += --with-extra-includes=/opt/csw/include
CONFIGURE_ARGS += --with-extra-libs=/opt/csw/lib

CONFIGURE_ARGS += --with-qt-includes=/opt/csw/kde-gcc/include
CONFIGURE_ARGS += --with-qt-libraries=/opt/csw/kde-gcc/lib


# kile doesn't have a test target
TEST_TARGET =

include ../category.mk

SPKG_SOURCEURL = http://kile.sourceforge.net/

BINFILES = $(DESTDIR)$(prefix)/kde-gcc/bin/kile

post-install:
	/usr/ccs/bin/strip $(BINFILES)
	/usr/ccs/bin/mcs -d $(BINFILES)

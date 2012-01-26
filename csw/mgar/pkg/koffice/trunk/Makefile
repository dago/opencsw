NAME = koffice
VERSION = 1.6.3
CATEGORIES = kde
GARTYPE = v2

DESCRIPTION = KDE Web Development Environment (gcc3)
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = $(KDE_ROOT)/$(KDE_DIST)/$(NAME)-$(VERSION)/src/
#DISTFILES   += Templates, addons, etc...
DISTFILES   += $(call admfiles,CSWkofficegcc,)
DISTFILES   += $(call admfiles,CSWkofficeaddons,)

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEPENDS +=

LIBS += -lCstd -lCrun

CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += QTDIR=/opt/csw/kde-gcc
CONFIGURE_ARGS += CC=/opt/csw/gcc3/bin/gcc
CONFIGURE_ARGS += CXX=/opt/csw/gcc3/bin/g++
CONFIGURE_ARGS += CPPFLAGS='-I/opt/csw/include'
CONFIGURE_ARGS += CFLAGS=-O2
CONFIGURE_ARGS += CXXFLAGS=-O2
CONFIGURE_ARGS += LIBS='-lCstd -lCrun'
CONFIGURE_ARGS += --with-qt-dir=/opt/csw/kde-gcc  
CONFIGURE_ARGS += --with-extra-includes=/opt/csw/include
CONFIGURE_ARGS += --with-extra-libs=/opt/csw/lib
CONFIGURE_ARGS += --prefix=/opt/csw/kde-gcc --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib --with-pspell
CONFIGURE_ARGS += --with-frontend=qt --enable-compression-support
CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw
CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw

include gar/category.mk

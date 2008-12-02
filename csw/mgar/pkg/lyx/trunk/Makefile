GARNAME = lyx
GARVERSION = 1.4.4
CATEGORIES = apps

DESCRIPTION = WYSIWYM document processor
define BLURB
   LyX is a document processor that encourages an approach to writing based
   on the structure of your documents, not their appearance. It is released
   under a Free Software / Open Source license.
endef

MASTER_SITES = ftp://ftp.lyx.org/pub/lyx/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlyx,depend prototype postinstall)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PATCHFILES = solaris.patch

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

include gar/category.mk

LD_OPTIONS = -R/opt/csw/kde-gcc/lib -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib
export LD_OPTIONS

BINFILES = $(DESTDIR)$(prefix)/kde-gcc/bin/lyx
BINFILES += $(DESTDIR)$(prefix)/kde-gcc/bin/lyxclient
BINFILES += $(DESTDIR)$(prefix)/kde-gcc/bin/tex2lyx

# Looks like lib/configure (which is a Python script as of 1.4.2) is no longer
# called during configure stage. That means we are missing LaTeXConfig.lyx and
# other files created by it. Run it now.
post-configure:
	(cd $(WORKSRC)/lib; \
	chmod 755 configure.py; \
	./configure.py)

post-install:
	(cd $(WORKSRC)/lib; \
	cp -p doc/LaTeXConfig.lyx $(DESTDIR)$(prefix)/kde-gcc/share/lyx/doc; \
	cp -p lyxrc.defaults packages.lst textclass.lst \
		$(DESTDIR)$(prefix)/kde-gcc/share/lyx)
	cp -p files/README.CSW $(DESTDIR)$(prefix)/kde-gcc/share/lyx/doc
	/usr/ccs/bin/strip $(BINFILES)
	/usr/ccs/bin/mcs -d $(BINFILES)

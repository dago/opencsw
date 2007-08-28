GARNAME = kdesvn
GARVERSION = 0.9.3
CATEGORIES = applications

DESCRIPTION = A Subversion client for KDE
define BLURB
  KDESvn is a frontend to the subversion vcs. In difference to most other
  tools it uses the subversion C-Api direct via a c++ wrapper made by Rapid
  SVN and doesn't parse the output of the subversion client. So it is a real
  client itself instead of a frontend to the command line tool.
endef

MASTER_SITES = http://www.alwins-world.de/programs/kdesvn/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWkdesvn,)
#DISTFILES += $(call admfiles,CSWkdesvn,depend prototype)

#CONFIGURE_ARGS = $(DIRPATHS)
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
CONFIGURE_ARGS += --with-extra-includes=/opt/csw/include
CONFIGURE_ARGS += --with-svn-include=/opt/csw/include
CONFIGURE_ARGS += --with-svn-lib=/opt/csw/lib/svn
CONFIGURE_ARGS += --with-apr-config=/opt/csw/apache2/bin/apr-config 
CONFIGURE_ARGS += --with-apu-config=/opt/csw/apache2/bin/apu-config

# kdesvn doesn't have a test target
TEST_TARGET =

include ../category.mk

pre-configure:
	(cd $(WORKSRC); test -r configure || make -f Makefile.cvs)

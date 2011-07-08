NAME = qt4
VERSION = 4.7.1
GARTYPE = v1
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  Qt is a comprehensive cross-platform C++ application framework. Qt 4
  introduces new features and many improvements over the 3.x series.
endef

MASTER_SITES = http://get.qt.nokia.com/qt/source/
DISTFILES    = qt-everywhere-opensource-src-$(VERSION).tar.gz
#DISTFILES   += $(call admfiles,CSWqt4,depend prototype-sparc prototype-i386)
#DISTFILES   += $(call admfiles,CSWqt4-devel,depend prototype-sparc prototype-i386)
#DISTFILES   += $(call admfiles,CSWqt4-docs,prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = qt-everywhere-opensource-src-(\d+(?:\.\d+)*).tar.gz

# The PACKAGES variable tell GAR which packages to build
#PACKAGES  = CSWqt4 CSWqt4-devel

WORKSRC = $(WORKDIR)/qt-everywhere-opensource-src-$(VERSION)
RUNTIME_DEP_PKGS_CSWqt4 = CSWfconfig CSWftype2 CSWggettext CSWglib2 CSWjpeg CSWlibxrender CSWpng CSWtiff CSWzlib 
#RUNTIME_DEP_PKGS_CSWqt4-devel = CSWqt4

#ifndef DO64
#PLATFORM=solaris-cc
#else
#PLATFORM=solaris-cc-64
#endif

#BUILD_DEP_PKGS = CSWpkgconfig CSWfconfig CSWlibdbusdev

CONFIGURE_ARGS = -prefix $(prefix) \
			-bindir $(bindir) \
			-libdir $(libdir) \
			-docdir $(docdir)/qt \
			-headerdir $(includedir) \
			-plugindir $(libdir)/qt4/plugins \
			-datadir $(sharedstatedir)/qt4 \
			-translationdir $(sharedstatedir)/qt4/translations \
			-sysconfdir $(etcdir)/qt4/settings \
			-examplesdir $(sharedstatedir)/qt4/examples \
			-demosdir $(sharedstatedir)/qt4/demos \
			-I$(includedir) \
			-L$(libdir) \
			-confirm-license \
			-opensource \
			-verbose

# SKIPTEST = 1

#INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

SRC_CLEAN_TARGET = confclean

include gar/category.mk

#ifdef DO64
#	# Do not use -xO3 as -xO2 is already set in the Makefile
#	SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
#	SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff
#
#	# Do not include -I/-L here. These flags must be defined after
#	# local QT4 includes and need to be defined during configure.
#	CFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))
#	CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS)
#	# -D_POSIX_PTHREAD_SEMANTICS needed, because getpwuid_r is used in the 4-arg-version
#	# (see getpwuid_r(3c) for details)
#	CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR)) -D_POSIX_PTHREAD_SEMANTICS
#	LDFLAGS = $($(GARCOMPILER)_LD_FLAGS) $($(GARCOMPILER)_LD_$(GARFLAVOR))
#else
#	# Do not use -xO3 as -xO2 is already set in the Makefile
#	SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
#	SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff
#
#	# Do not include -I/-L here. These flags must be defined after
#	# local QT4 includes and need to be defined during configure.
#	CFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))
#	CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS)
#	CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR))
#	LDFLAGS = $($(GARCOMPILER)_LD_FLAGS) $($(GARCOMPILER)_LD_$(GARFLAVOR))
#endif

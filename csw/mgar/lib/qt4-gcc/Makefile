GARNAME = qt
GARVERSION = 4.3.2
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  It contains a C++ class library as well as tools for cross-platform GUI
  development and internationalization.
endef

GARCOMPILER = GNU

MASTER_SITES = ftp://ftp.trolltech.com/qt/source/
DISTNAME = qt-x11-opensource-src-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz
#DISTFILES += $(call admfiles,CSWqt4gcc,depend prototype)
DISTFILES += $(call admfiles,CSWqt4gcc,)

#TMP_DIRPATHS = --prefix=$(prefix) --exec_prefix=$(exec_prefix) --bindir=$(bindir
#) --sbindir=$(sbindir) --libexecdir=$(libexecdir) --datadir=$(datadir) --sysconf
#dir=$(sysconfdir) --sharedstatedir=$(sharedstatedir) --localstatedir=$(localstat
#edir) --libdir=$(libdir) --infodir=$(infodir) --lispdir=$(lispdir) --includedir=
$(includedir) --mandir=$(mandir)

CONFIGURE_ARGS = -platform solaris-g++ -confirm-license -prefix $(prefix) #-bindir=$(bindir) -libdir=$(libdir) -docdir=

#CONFIGURE_ARGS = $(DIRPATHS)

# lyx doesn't have a test target
TEST_TARGET =

include ../category.mk

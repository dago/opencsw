# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = speex
GARVERSION = 1.2
REV = rc1
CATEGORIES = lib

DESCRIPTION = Speex audio codec support library
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/speex/
DISTFILES  = $(GARNAME)-$(GARVERSION)$(REV).tar.gz

# The important lines are these:
#
# diff -Naur speex-1.2rc1.orig/src/Makefile.am speex-1.2rc1.patched/src/Makefile.am
# --- speex-1.2rc1.orig/src/Makefile.am   2008-06-02 10:21:21.000000000 +0200
# +++ speex-1.2rc1.patched/src/Makefile.am        2009-08-10 16:44:45.255831787 +0200
# @@ -18,8 +18,8 @@
# 
#  speexenc_SOURCES = speexenc.c wav_io.c skeleton.c
#  speexenc_LDADD = $(top_builddir)/libspeex/libspeex.la $(top_builddir)/libspeex/libspeexdsp.la \
# -       $(OGG_LIBS)  @FFT_LIBS@
# +       $(OGG_LIBS)  @FFT_LIBS@ $(LIBOBJS)
# 
#  speexdec_SOURCES = speexdec.c wav_io.c
#  speexdec_LDADD = $(top_builddir)/libspeex/libspeex.la \
# -       $(OGG_LIBS)  @FFT_LIBS@
# +       $(OGG_LIBS)  @FFT_LIBS@ $(LIBOBJS)
#
# All the other stuff is generated (and the newlines on getopt*.c were stripped of ^M)
PATCHFILES = speex-getopt.patch.bz2

PACKAGES = CSWspeex
CATALOGNAME = libspeex
REQUIRED_PKGS = CSWlibogg
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

SPKG_SOURCEURL = http://www.speex.org/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)$(REV)

# 64-bit doesn't build on x86.
BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = PACKAGE
INSTALL_OVERRIDE_VAR_PACKAGE = libspeex

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)_rev=$(REV)


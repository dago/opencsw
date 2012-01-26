# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = speex
VERSION = 1.2rc1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Speex audio codec support library
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/speex/
DISTFILES  = $(DISTNAME).tar.gz

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

VENDOR_URL = http://www.speex.org/

BUILD_DEP_PKGS += CSWlibogg-dev

PACKAGES = CSWspeex
SPKG_DESC_CSWspeex = Speex audio codec tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWspeex += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWspeex += CSWlibspeexdsp1
RUNTIME_DEP_PKGS_CSWspeex += CSWlibogg0

PACKAGES += CSWlibspeex-dev
SPKG_DESC_CSWlibspeex-dev = Development files for libspeex.so.1
PKGFILES_CSWlibspeex-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibspeex-dev += $(docdir)/libspeex/manual.pdf
RUNTIME_DEP_PKGS_CSWlibspeex-dev += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibspeex-dev += CSWlibspeexdsp1

PACKAGES += CSWlibspeex1
SPKG_DESC_CSWlibspeex1 = Speex audio codec library, libspeex.so.1
PKGFILES_CSWlibspeex1 += $(call pkgfiles_lib,libspeex.so.1)

PACKAGES += CSWlibspeexdsp1
SPKG_DESC_CSWlibspeexdsp1 = Speex audio codec support library, libspeexdsp.so.1
PKGFILES_CSWlibspeexdsp1 += $(call pkgfiles_lib,libspeexdsp.so.1)

# 64-bit doesn't build on x86.
BUILD64_LIBS_ONLY = 1
# TEST_SCRIPTS =

CONFIGURE_ARGS += $(DIRPATHS)
# Otherwise we must unnecessarily link to CSW provided libgnugetopt
CONFIGURE_ARGS += ac_cv_func_getopt_long=no
CONFIGURE_ARGS += ac_cv_lib_gnugetopt_getopt_long=no

INSTALL_OVERRIDE_VARS = PACKAGE
INSTALL_OVERRIDE_VAR_PACKAGE = libspeex

include gar/category.mk


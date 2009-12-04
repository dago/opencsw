# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pinentry
GARVERSION = 0.7.6
CATEGORIES = utils
DESCRIPTION = Allows entering passwords into gpg-agent.
define BLURB
endef
SPKG_SOURCEURL = http://www.gnupg.org/
EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/pinentry/
# PATCHFILES  = 0001-remove-__extension__-from-util.c.patch
EXTRA_CFLAGS = -D__EXTENSIONS__
EXTRA_CXXFLAGS = -D__EXTENSIONS__
PATCHFILES += 0002-ncurses-include.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS = CSWglib CSWgtk CSWiconv CSWncurses
PREREQUISITE_PKGS = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWgtk2devel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

# Unfortunately, the compilation fails with SOS11. Because of that, pinentry
# can't be compiled on Solaris 8, and CSWgnupg2 needs to be compiled for
# Solaris 8 with no pinentry support.
#
# gmake[4]: Entering directory
# `(...)/pinentry-0.7.6/secmem'
# source='util.c' object='util.o' libtool=no \
#         DEPDIR=.deps depmode=none /bin/bash ../depcomp \
#         /opt/studio/SOS11/SUNWspro/bin/cc -DHAVE_CONFIG_H -I. -I.. \
#         -I/opt/csw/X11/include -I/opt/csw/include  -xO3 -xarch=v8 \
#         -D__EXTENSIONS__ -c util.c
# "util.c", line 57: warning: implicit function declaration: __extension__
# "util.c", line 57: syntax error before or at: {
# "util.c", line 57: undefined symbol: __result
# "util.c", line 57: undefined symbol: __result
# "util.c", line 57: undefined symbol: __result
# "util.c", line 57: syntax error before or at: )
# "util.c", line 58: warning: syntax error:  empty declaration
# "util.c", line 59: warning: old-style declaration or incorrect type for: written
# cc: acomp failed for util.c
# gmake[4]: *** [util.o] Error 2

GARCOMPILER = SOS12

PACKAGING_PLATFORMS ?= solaris9-sparc solaris9-i386


include gar/category.mk

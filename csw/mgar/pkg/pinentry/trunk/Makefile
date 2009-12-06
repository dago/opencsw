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
PATCHFILES += 0002-ncurses-include.patch
PATCHFILES += 0003-TEMP_FAILURE_RETRY-macro-expansion.patch
PATCHFILES += 0004-adding-prereq-2.59-to-configure.ac.patch
PATCHFILES += 0005-Importing-getopt-posix-gnulib-module.patch
PATCHFILES += 0006-enabling-gnulib-getopt-module.patch
EXTRA_CFLAGS = -D__EXTENSIONS__
EXTRA_CXXFLAGS = -D__EXTENSIONS__
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS  = CSWfconfig
REQUIRED_PKGS += CSWftype2
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWgtk
REQUIRED_PKGS += CSWgtk2
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWlibatk
REQUIRED_PKGS += CSWlibcairo
REQUIRED_PKGS += CSWlibxext
REQUIRED_PKGS += CSWncurses
REQUIRED_PKGS += CSWpango
PREREQUISITE_PKGS = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWgtk2devel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LINKER_FLAGS_isa-i386    = /usr/openwin/lib/libXext.so
EXTRA_LINKER_FLAGS_isa-sparcv8 = /usr/openwin/lib/libXext.so
EXTRA_LINKER_FLAGS_isa-amd64   = /usr/openwin/lib/amd64/libXext.so
EXTRA_LINKER_FLAGS_isa-sparcv9 = /usr/openwin/lib/sparcv9/libXext.so
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(MODULATION))
BUILD64 = 1

include gar/category.mk

# Switch this target on when working with gnulib.
# pre-configure-modulated:
# 	# To pick up the gnulib bits.
# 	( \
# 	  cd $(WORKSRC) \
# 	    && \
# 	  aclocal -I m4 \
# 	    && \
# 	  autoconf -I m4 \
# 	    && \
# 	  autoheader \
# 	    && \
# 	  automake --add-missing --foreign \
# 	)
# 	@$(MAKECOOKIE)

# It works with SOS11 now, thanks to
# 0003-TEMP_FAILURE_RETRY-macro-expansion.patch
# GARCOMPILER = SOS12

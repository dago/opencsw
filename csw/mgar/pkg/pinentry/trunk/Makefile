# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pinentry
VERSION = 0.7.6
CATEGORIES = utils
DESCRIPTION = Allows entering passwords into gpg-agent.
define BLURB
endef
SPKG_SOURCEURL = http://www.gnupg.org/
EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/pinentry/
PATCHFILES  = 0002-ncurses-include.patch
PATCHFILES += 0003-TEMP_FAILURE_RETRY-macro-expansion.patch
PATCHFILES += 0004-adding-prereq-2.59-to-configure.ac.patch
PATCHFILES += 0005-Importing-getopt-posix-gnulib-module.patch
PATCHFILES += 0006-enabling-gnulib-getopt-module.patch
EXTRA_CFLAGS = -D__EXTENSIONS__
EXTRA_CXXFLAGS = -D__EXTENSIONS__
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
RUNTIME_DEP_PKGS  = CSWfconfig
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWlibxext
RUNTIME_DEP_PKGS += CSWncurses
RUNTIME_DEP_PKGS += CSWpango
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWgtk2devel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LINKER_FLAGS_isa-i386    = /usr/openwin/lib/libXext.so
EXTRA_LINKER_FLAGS_isa-sparcv8 = /usr/openwin/lib/libXext.so
EXTRA_LINKER_FLAGS_isa-amd64   = /usr/openwin/lib/amd64/libXext.so
EXTRA_LINKER_FLAGS_isa-sparcv9 = /usr/openwin/lib/sparcv9/libXext.so
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(MODULATION))

# There's a problem with building on Solaris 10 as getopt.h is already present
# in /usr/include and conflicts with the one provided by gnulib.
# BUILD64 = 1

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

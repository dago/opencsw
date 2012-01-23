# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libsamplerate
VERSION = 0.1.7
CATEGORIES = lib

DESCRIPTION = Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for audio
define BLURB
  SRC is capable of arbitrary and time varying conversions ; from
  downsampling by a factor of 256 to upsampling by the same factor.
  Arbitrary in this case means that the ratio of input and output sample
  rates can be an irrational number. The conversion ratio can also vary
  with time for speeding up and slowing down effects.
endef

MASTER_SITES = http://www.mega-nerd.com/SRC/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Both changes have been reported upstream to Erik de Castro Lopo and
# he gave his placet that they are correct. They affect the testsuite only.
PATCHFILES += 0001-Fix-testcase.patch
PATCHFILES += 0002-Raise-failure-levels-slightly-for-Solaris-Sparc-and-.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibsamplerate0
CATALOGNAME_CSWlibsamplerate0 = libsamplerate0
SPKG_DESC_CSWlibsamplerate0 = Sample rate converter for audio, libsamplerate.so.0

PACKAGES += CSWlibsamplerate-dev
CATALOGNAME_CSWlibsamplerate-dev = libsamplerate_dev
SPKG_DESC_CSWlibsamplerate-dev = Development files for libsamplerate
PKGFILES_CSWlibsamplerate-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsamplerate-dev = CSWlibsamplerate0

PACKAGES += CSWlibsamplerate-utils
CATALOGNAME_CSWlibsamplerate-utils = libsamplerate_utils
SPKG_DESC_CSWlibsamplerate-utils = Sample rate conversion programs using libsamplerate
PKGFILES_CSWlibsamplerate-utils = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWlibsamplerate-utils += CSWlibsamplerate0
RUNTIME_DEP_PKGS_CSWlibsamplerate-utils += CSWlibsndfile

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

include gar/category.mk

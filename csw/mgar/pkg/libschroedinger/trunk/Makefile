GARNAME = libschroedinger
GARVERSION = 1.0.7
CATEGORIES = lib

DESCRIPTION = A cross-platform implementation of the Dirac video compression specification
define BLURB
  A new release of Schrödinger is available. Schrödinger (o"schro"
  for short) is a cross-platform implementation of the Dirac video
  compression specification as a C library. Many media frameworks
  such as GStreamer and ffmpeg use schro to encode and decode Dirac
  video.
endef

MASTER_SITES = http://diracvideo.org/download/schroedinger/
DISTNAME = schroedinger-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES = 0001-Avoid-using-FUNCTION-and-stdint.h.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://diracvideo.org/

PACKAGES = CSWlibschro CSWlibschrodevel

SPKG_DESC_CSWlibschro = $(DESCRIPTION)
SPKG_DESC_CSWlibschrodevel = libschroedinger developer files

REQUIRED_PKGS_CSWlibschro = CSWliboil
REQUIRED_PKGS_CSWlibschrodevel = CSWlibschro

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PKGFILES_CSWlibschrodevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibschrodevel += $(sharedstatedir)/gtk-doc/.*

include gar/category.mk

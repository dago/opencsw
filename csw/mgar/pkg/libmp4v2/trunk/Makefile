# TBD:
# - Collision with CSWfaad2:
#     /csw/lib/libmp4v2.so
#     /opt/csw/include/mp4.h
# - How does ths library relate to mpeg4ip, both released 1.5.0.1 and unreleased 1.6.1 ?

NAME = libmp4v2
VERSION = 1.5.0.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A free library to read and manipulate the mp4 container format
define BLURB
  The mpeg4ip package, available from http://mpeg4ip.net/ contains a very useful piece of software,
  the libmp4v2 package. Unfortunately the mpeg4ip package also contains software that are covered by
  patents in some juridistictions and therefore the policy of several different free software
  distributions stops it's inclusion.
  Therefore the author of this software has prepared this redistribution of the libmp4v2 package.
  It cotains only code to read and manipulate the mp4 container format, and is free from patent
  issues to the best of his knowledgECTe.
endef

SF_PROJ = easytag
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES  = use-inttypes.h.diff
PATCHFILES += mp4util.diff
PATCHFILES += include-limits.h.diff
PATCHFILES += linux-stdints.diff
PATCHFILES += 0001-Use-const-char-where-necessary.patch
PATCHFILES += 0002-Add-headers-and-libs-as-required-to-testsuite.patch
PATCHFILES += 0003-Keep-norunpath-for-C-linkage.patch
PATCHFILES += 0004-Add-libgnugetopt.so-to-executables.patch

PACKAGES += CSWlibmp4v2-0
SPKG_DESC_CSWlibmp4v2-0 = A free library to read and manipulate the mp4 container format, libmp4v2.so.0
PKGFILES_CSWlibmp4v2-0 += $(call pkgfiles_lib,libmp4v2.so.0)

PACKAGES += CSWlibmp4v2-dev
SPKG_DESC_CSWlibmp4v2-dev = Development files for libmp4v2.so.0
PKGFILES_CSWlibmp4v2-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibmp4v2-dev += CSWlibmp4v2-0

PACKAGES += CSWlibmp4v2-utils
SPKG_DESC_CSWlibmp4v2-utils = Utility programs for mp4 file manipulation
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmp4v2-utils += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibmp4v2-utils += CSWlibmp4v2-0

EXTRA_LINKER_FLAGS += -norunpath

include
# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = x264
VERSION = snapshot-20120306-2245
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = x264 is encoding video streams into the H.264/MPEG-4 AVC format
define BLURB
 x264 is a free software library and application for encoding video streams into the H.264/MPEG-4 AVC format, and is released under the terms of the GNU GPL. 
endef

VENDOR_URL = http://www.videolan.org/developers/x264.html
MASTER_SITES = ftp://ftp.videolan.org/pub/videolan/x264/snapshots/ 
DISTFILES  = $(DISTNAME).tar.bz2

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
GARCOMPILER = GCC4
SKIPTEST = 1
BUILD64_LIBS_ONLY = 1

BUILD_DEP_PKGS += CSWffmpeg-dev


#More info on mimpure-text: http://blogs.everycity.co.uk/alasdair/2009/05/text-relocation-remains-against-symbol-libx264/

CONFIGURE_ARGS-isa-pentium_pro = $(DIRPATHS) --enable-shared --extra-ldflags="-mimpure-text -lrt"
CONFIGURE_ARGS-isa-amd64 = $(DIRPATHS) --enable-shared --extra-ldflags="-mimpure-text -lrt" --host=amd64-pc-solaris2.10
CONFIGURE_ARGS-isa-sparcv8plus = $(DIRPATHS) --enable-shared --extra-ldflags="-mimpure-text -lrt" --disable-asm
CONFIGURE_ARGS-isa-sparcv9 = $(DIRPATHS) --enable-shared --enable-pic --disable-asm
CONFIGURE_ARGS += $(CONFIGURE_ARGS-isa-$(ISA))


PACKAGES += CSWx264
SPKG_DESC_CSWx264 = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWx264 += CSWlibavformat53
RUNTIME_DEP_PKGS_CSWx264 += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWx264 += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWx264 += CSWlibavutil51

PACKAGES += CSWlibx264-120
CATALOGNAME_CSWlibx264-120 = libx264_120
PKGFILES_CSWlibx264-120 += $(call baseisadirs,$(libdir),libx264\.so\.120)
PKGFILES_CSWlibx264-120 += $(call baseisadirs,$(libdir),libx264\.so\.120(\.\d+)*)
SPKG_DESC_CSWlibx264-120 += $(DESCRIPTION), libx264.so.120
RUNTIME_DEP_PKGS_CSWlibx264-120 += CSWlibgcc-s1

PACKAGES += CSWlibx264-dev
CATALOGNAME_CSWlibx264-dev = libx264_dev
SPKG_DESC_CSWlibx264-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibx264-dev += /opt/csw/lib/libx264.so
PKGFILES_CSWlibx264-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibx264-dev += CSWlibx264-120

#Some overrides
CHECKPKG_OVERRIDES += pkginfo-description-not-starting-with-uppercase
CHECKPKG_OVERRIDES_CSWlibx264-120 += pkginfo-description-not-starting-with-uppercase
# seems to be checkpkg bug:
CHECKPKG_OVERRIDES_CSWlibx264-120 += non-uniform-lib-versions-in-package|sonames=libx264.so.120




include gar/category.mk

# For 'grep -q'
PATH := /opt/csw/gnu:$(PATH)

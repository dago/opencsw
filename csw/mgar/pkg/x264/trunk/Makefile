# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# So it does not get lost. With gcc4.8 you now need -fno-aggressive-loop-optimizations: http://comments.gmane.org/gmane.comp.video.ffmpeg.devel/161226
NAME = x264
VERSION = b3065e6
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = x264 is encoding video streams into the H.264/MPEG-4 AVC format
define BLURB
 x264 is a free software library and application for encoding video streams into the H.264/MPEG-4 AVC format, and is released under the terms of the GNU GPL. 
endef

VENDOR_URL = http://www.videolan.org/developers/x264.html
#MASTER_SITES = http://repo.or.cz/w/x264.git/snapshot/  
#DISTFILES  = c522ad1fed167d0e985e4f9dcdee042473cf74db.tar.gz
GIT_REPOS = http://git.videolan.org/git/x264.git
GIT_b3065e660df391168067f13216d99825260939d429f5da9b0292387309

# This Patch file needs to be updated on every new version! 
PATCHFILES += 0001-replace-version.sh.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAMrc solaris10-i386
GARCOMPILER = GCC4
SKIPTEST = 1

BUILD64 = 1
ISAEXEC = 1

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
RUNTIME_DEP_PKGS_CSWx264 += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWx264 += CSWlibavformat54
RUNTIME_DEP_PKGS_CSWx264 += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWx262

PACKAGES += CSWlibx264-130
CATALOGNAME_CSWlibx264-130 = libx264_130
PKGFILES_CSWlibx264-130 += $(call baseisadirs,$(libdir),libx264\.so\.130)
PKGFILES_CSWlibx264-130 += $(call baseisadirs,$(libdir),libx264\.so\.130(\.\d+)*)
SPKG_DESC_CSWlibx264-130 += $(DESCRIPTION), libx264.so.130
RUNTIME_DEP_PKGS_CSWlibx264-130KGS_CSWlibx264-128 += CSWlibgcc-s1

PACKAGES += CSWlibx264-dev
CATALOGNAME_CSWlibx264-dev = libx264_dev
SPKG_DESC_CSWlibx264-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibx264-dev += /opt/csw/lib/libx264.so
PKGFILES_CSWlibx264-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibx264-d30 += CSWlibx264-128

#Some overrides
CHECKPKG_OVERRIDES += pkginfo-description-not-starting-with-uppercase
CHECKPKG_OVER30DES_CSWlibx264-128 += pkginfo-description-not-starting-with-uppercase




include gar/category.mk

# For 'grep -q'
PATH := /op
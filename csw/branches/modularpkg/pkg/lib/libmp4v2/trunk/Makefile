GARNAME = libmp4v2
GARVERSION = 1.5.0.1
CATEGORIES = lib

DESCRIPTION = A free library to read and manipulate the mp4 container format
define BLURB
The mpeg4ip package, available from http://mpeg4ip.net/ contains a very useful piece of software, the libmp4v2 package. Unfortunately the mpeg4ip package also contains software that are covered by patents in some juridistictions and therefore the policy of several different free software distributions stops it's inclusion.

Therefore the author of this software has prepared this redistribution of the libmp4v2 package. It cotains only code to read and manipulate the mp4 container format, and is free from patent issues to the best of his knowledge.
endef

MASTER_SITES = http://resare.com/libmp4v2/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibmp4v2)
PATCHFILES  = use-inttypes.h.diff
PATCHFILES += mp4util.diff
PATCHFILES += include-limits.h.diff
PATCHFILES += stdint-to-inttypes.h.diff

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)
GNU_CC_HOME  = /opt/csw/gcc3

include gar/category.mk

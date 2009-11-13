GARNAME = libfaac
GARVERSION = 1.28
CATEGORIES = lib

DESCRIPTION = AAC encoder library and tool
define BLURB
  FAAC is an open source MPEG-4 and MPEG-2 AAC encoder
endef

SF_PROJ = faac
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(SF_PROJ)-$(GARVERSION).tar.bz2
DISTNAME = $(SF_PROJ)-$(GARVERSION)

PACKAGES = CSWfaac
CATALOGNAME = $(GARNAME)

SPKG_SOURCEURL = http://www.audiocoding.com/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SF_PROJ)-(\d+(?:\.\d+)*).tar.bz2

#PATCHFILES += Makefile.am.diff Makefile.in.diff Makefile.in.frontend.diff 
PATCHFILES += Makefile.in.frontend.diff Makefile.in.common.mp4v2.diff
PATCHFILES += aacquant.c.diff aacquant.h.diff config.h.in.diff
#PATCHFILES += configure.in.diff faac.h.diff faaccfg.h.diff frame.h.diff
PATCHFILES += configure.diff faac.h.diff faaccfg.h.diff frame.h.diff
PATCHFILES += input.c.diff ltp.c.diff mp4property.h.diff mp4util.h.diff
PATCHFILES += mpeg4ip.h.diff psych.h.diff

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

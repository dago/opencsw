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
CATALOGNAME_CSWfaac = $(GARNAME)
SPKG_DESC_CSWfaac = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(SF_PROJ)-(\d+(?:\.\d+)*).tar.bz2

PATCHFILES += Makefile.am.diff Makefile.in.diff Makefile.in.frontend.diff 
PATCHFILES += aacquant.c.diff aacquant.h.diff config.h.in.diff
PATCHFILES += configure.in.diff faac.h.diff faaccfg.h.diff frame.h.diff
PATCHFILES += input.c.diff ltp.c.diff mp4property.h.diff mp4util.h.diff
PATCHFILES += mpeg4ip.h.diff psych.h.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

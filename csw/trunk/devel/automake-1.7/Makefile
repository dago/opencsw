GARNAME = automake
GARVERSION = 1.7.3
CATEGORIES = bootstrap

MASTER_SITES = http://ftp.gnu.org/gnu/automake/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWautomake17,)

DESCRIPTION = automake
define BLURB
endef

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
ENABLE_TEST = 0

include ../category.mk

GARNAME = automake
GARVERSION = 1.4-p6
CATEGORIES = bootstrap

MASTER_SITES = http://ftp.gnu.org/gnu/automake/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWautomake14,)

DESCRIPTION = GNU automake
define BLURB
endef

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
TEST_SCRIPTS =

include ../category.mk

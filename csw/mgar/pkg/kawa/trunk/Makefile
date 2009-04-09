GARNAME = kawa
GARVERSION = 1.9.1
CATEGORIES = utils
ARCHALL = 1

DESCRIPTION = Java implementation of Scheme and a framework for implementing high-level and dynamic languages

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/kawa/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWkawa,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = kawa-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk

PATH := /usr/jdk1.5.0_15/bin:$(PATH)

GARNAME = jicmp
GARVERSION = 1.0.4
CATEGORIES = lib

DESCRIPTION = JICMP is a Java interface to the ICMP protocol (ping)

MASTER_SITES = http://heanet.dl.sourceforge.net/sourceforge/opennms
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWjicmp,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = gar-base.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = 

include gar/category.mk

GARNAME = jrrd
GARVERSION = 1.0.1
CATEGORIES = lib

DESCRIPTION = JRRD is a Java interface to RRDTool

MASTER_SITES = http://heanet.dl.sourceforge.net/sourceforge/opennms
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWjrrd,)

CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --with-java=/usr/jdk/latest
CONFIGURE_ARGS += --disable-rpm-rules

TEST_TARGET = 

include ../category.mk

GARNAME = easytag
GARVERSION = 2.1
CATEGORIES = applications

DESCRIPTION = Tag editor for MP3, Ogg Vorbis files and more
define BLURB
endef

SF_PROJ = easytag
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWeasytag,depend)

# Compile with GCC
GARCOMPILER = GNU

#LD_OPTIONS = -R/opt/csw/kde-gcc/lib -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

include ../category.mk

#SPKG_SOURCEURL = http://kile.sourceforge.net/

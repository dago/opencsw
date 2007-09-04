#STATUS:
#2.1.0 dumps core, and the developer has suggested that I instead use 2.1.2
#2.1.2 won't compile (with mp3 support) due to code using strcasestr,
# which isn't defined on solaris.
#I'm emailing backwards and forth

GARNAME = easytag
GARVERSION = 2.1.2
CATEGORIES = applications

DESCRIPTION = Tag editor for MP3, Ogg Vorbis files and more
define BLURB
endef

SF_PROJ = easytag
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWeasytag)#,depend)
PATCHFILES = patch_easytag_212_213.diff

# Compile with GCC
GARCOMPILER = GNU


CONFIGURE_ARGS  = --prefix=$(prefix) #--disable-mp3
CONFIGURE_ARGS += --mandir=/opt/csw/share/man
CONFIGURE_ARGS += CPPFLAGS="-I/export/home/griffous/bw/build/opt/csw/include -I/opt/csw/include -I/usr/include"


#CONFIGURE_ARGS  = --prefix=$(prefix) CC=/opt/csw/gcc4/bin/gcc CXX=/opt/csw/gcc4/bin/g++

include ../category.mk



jw:
	@echo "CPPFLAGS=$(CPPFLAGS)

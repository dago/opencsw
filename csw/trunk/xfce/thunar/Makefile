GARNAME = Thunar
GARVERSION = 0.8.0
CATEGORIES = xfce

DESCRIPTION = Xfce Thunar File Manager
define BLURB
   Xfce Thunar File Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcethunar.depend CSWxfcethunar.gspec CSWxfcethunar.prototype
DISTFILES += CSWlibxfcethunar.depend CSWlibxfcethunar.gspec CSWlibxfcethunar.prototype
DISTFILES += CSWxfcethunardoc.depend CSWxfcethunardoc.gspec CSWxfcethunardoc.prototype
DISTFILES += CSWlibxfcethunardev.depend CSWlibxfcethunardev.gspec CSWlibxfcethunardev.prototype

# DISTFILES  += $(call admfiles,CSWxfcethunar, depend)

PATCHFILES  = thunar-vfs-path-private.h.diff 
PATCHFILES += thunar-vfs-thumb-jpeg.c.diff

include ../category.mk

CONFIGURE_ARGS += --with-x --enable-dbus

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )


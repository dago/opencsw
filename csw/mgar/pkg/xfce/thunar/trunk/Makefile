GARNAME = Thunar
GARVERSION = 0.9.0
CATEGORIES = xfce

DESCRIPTION = Xfce Thunar File Manager
define BLURB
   Xfce Thunar File Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfcethunar.depend CSWxfcethunar.gspec CSWxfcethunar.prototype
# DISTFILES += CSWlibxfcethunar.depend CSWlibxfcethunar.gspec CSWlibxfcethunar.prototype
# DISTFILES += CSWxfcethunardoc.depend CSWxfcethunardoc.gspec CSWxfcethunardoc.prototype
# DISTFILES += CSWlibxfcethunardev.depend CSWlibxfcethunardev.gspec CSWlibxfcethunardev.prototype

DISTFILES  += $(call admfiles,CSWxfcethunar, depend)

# PATCHFILES  = thunar-vfs-path-private.h.diff 
# PATCHFILES += thunar-vfs-thumb-jpeg.c.diff

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/exo-0.3/

CONFIGURE_ARGS += --with-x --enable-dbus --with-volume-manager=auto

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )


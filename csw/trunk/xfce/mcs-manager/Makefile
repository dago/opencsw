GARNAME = xfce-mcs-manager
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager 
define BLURB
   Xfce Settings Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcemcsmanagerdevel.depend CSWxfcemcsmanagerdevel.gspec CSWxfcemcsmanagerdevel.prototype
DISTFILES += CSWxfcemcsmanagerdoc.depend CSWxfcemcsmanagerdoc.gspec CSWxfcemcsmanagerdoc.prototype
DISTFILES += CSWxfcemcsmanager.depend CSWxfcemcsmanager.gspec CSWxfcemcsmanager.prototype

# DISTFILES += $(call admfiles,CSWxfce_mcs_manager, depend)

LIBDEPS = xfce/libxfce4util

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )


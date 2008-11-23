GARNAME = xfce-mcs-manager
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager 
define BLURB
   Xfce Settings Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfcemcsmanagerdev.depend CSWxfcemcsmanagerdev.gspec CSWxfcemcsmanagerdev.prototype
# DISTFILES += CSWxfcemcsmanagerdoc.depend CSWxfcemcsmanagerdoc.gspec CSWxfcemcsmanagerdoc.prototype
# DISTFILES += CSWxfcemcsmanager.depend CSWxfcemcsmanager.gspec CSWxfcemcsmanager.prototype

DISTFILES += $(call admfiles,CSWxfcemcsmanager, depend)

LIBDEPS = xfce/libxfce4util

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )


GARNAME = libxfcegui4
CATEGORIES = xfce

DESCRIPTION = Xfce Widget Library 
define BLURB
   Xfce Widget Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWlibxfcegui4.depend CSWlibxfcegui4.gspec CSWlibxfcegui4.prototype 
DISTFILES += CSWlibxfcegui4dep.depend CSWlibxfcegui4dep.gspec CSWlibxfcegui4dep.prototype CSWlibxfcegui4dep.preinstall
DISTFILES += CSWlibxfcegui4doc.depend CSWlibxfcegui4doc.gspec CSWlibxfcegui4doc.prototype
DISTFILES += CSWlibxfcegui4dev.depend CSWlibxfcegui4dev.gspec CSWlibxfcegui4dev.prototype
# DISTFILES += $(call admfiles,CSWlibxfcegui4, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS = xfce/libxfce4util

TEST_SCRIPTS = none

include gar/category.mk

# Configure common options
CONFIGURE_ARGS += --enable-xinerama

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

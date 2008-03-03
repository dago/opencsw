GARNAME = xfce-mcs-plugins
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager Plugins
define BLURB
   Xfce Settings Manager Plugins
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcemcsplugins.depend CSWxfcemcsplugins.gspec CSWxfcemcsplugins.prototype
DISTFILES += CSWxfcemcspluginsdoc.depend CSWxfcemcspluginsdoc.gspec CSWxfcemcspluginsdoc.prototype

# DISTFILES += $(call admfiles,CSWxfce_mcs_plugins, depend)

# PATCHFILES += configure.in.diff
# PATCHFILES += configure.diff

include gar/category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )


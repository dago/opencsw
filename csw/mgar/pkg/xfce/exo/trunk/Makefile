GARNAME = exo
CATEGORIES = xfce

DESCRIPTION = Xfce Extensions Library 
define BLURB
   Xfce Extensions Library 
endef

GARVERSION = 0.3.4
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfceexo.depend CSWxfceexo.gspec CSWxfceexo.prototype
# DISTFILES += CSWxfcelibexo.depend CSWxfcelibexo.gspec CSWxfcelibexo.prototype
# DISTFILES += CSWxfceexodoc.depend CSWxfceexodoc.gspec CSWxfceexodoc.prototype
# DISTFILES += CSWxfcelibexodev.depend CSWxfcelibexodev.gspec CSWxfcelibexodev.prototype
DISTFILES += $(call admfiles,CSWxfceexo, depend)

#  Patch for the exo-mount.c file
# PATCHFILES = exo.diff

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS += --enable-python --enable-hal

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

NAME = lzo
VERSION = 2.04
CATEGORIES = utils

DESCRIPTION = LZO compression library
define BLURB
  LZO is a portable lossless data compression library written in ANSI C.
endef

MASTER_SITES = http://www.oberhumer.com/opensource/lzo/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWliblzo-dev
CATALOGNAME_CSWliblzo-dev = liblzo_dev
SPKG_DESC_CSWliblzo-dev = Development files for liblzo2.so.2
RUNTIME_DEP_PKGS_CSWliblzo-dev = CSWliblzo2-2
# PKGFILES is catchall
OBSOLETED_BY_CSWliblzo-dev = CSWlzo

PACKAGES += CSWliblzo2-2
CATALOGNAME_CSWliblzo2-2 = liblzo2_2
SPKG_DESC_CSWliblzo2-2 = Library for LZO compression providing liblzo2.so.2
PKGFILES_CSWliblzo2-2 = $(call pkgfiles_lib,liblzo2.so.2)
OBSOLETED_BY_CSWliblzo2-2 = CSWlzo

VENDOR_URL = http://www.oberhumer.com/opensource/lzo/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static

CONFIGURE_ARGS_isa-amd64 = --disable-asm
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

include gar/category.mk

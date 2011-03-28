NAME = lzo
VERSION = 2.04
CATEGORIES = utils

DESCRIPTION = LZO compression library
define BLURB
  LZO is a portable lossless data compression library written in ANSI C.
endef

MASTER_SITES = http://www.oberhumer.com/opensource/lzo/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWliblzo-dev
CATALOGNAME_CSWliblzo-dev = liblzo_dev
SPKG_DESC_CSWliblzo-dev = Development files for liblzo2.so.2
RUNTIME_DEP_PKGS_CSWliblzo-dev = CSWliblzo2-2
# PKGFILES is catchall
OBSOLETED_BY_CSWliblzo-dev = CSWlzo

PACKAGES += CSWliblzo2-2
CATALOGNAME_CSWliblzo2-2 = liblzo2_2
SPKG_DESC_CSWliblzo2-2 = Library for LZO compression providing liblzo2.so.2
PKGFILES_CSWliblzo2-2 = $(call baseisadirs,$(libdir),liblzo2\.so\.2(\.\d+)*)
OBSOLETED_BY_CSWliblzo2-2 = CSWlzo

VENDOR_URL = http://www.oberhumer.com/opensource/lzo/

CONFIGURE_ARGS_isa-amd64 = --disable-asm

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

include gar/category.mk

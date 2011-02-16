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

PACKAGES += CSWlzo
CATALOGNAME_CSWlzo = lzo
SPKG_DESC_CSWlzo = Transitional package as contents moved to CSWliblzo2-2
CHECKPKG_OVERRIDES_CSWlzo += surplus-dependency|CSWliblzo2-2
PKGFILES_CSWlzo = NOFILES
ARCHALL_CSWlzo = 1

PACKAGES += CSWlzo-dev
CATALOGNAME_CSWlzo-dev = lzo_dev
SPKG_DESC_CSWlzo-dev = Development files for liblzo2.so.2
RUNTIME_DEP_PKGS_CSWlzo-dev = CSWliblzo2-2
# PKGFILES is catchall

PACKAGES += CSWliblzo2-2
CATALOGNAME_CSWliblzo2-2 = liblzo2_2
SPKG_DESC_CSWliblzo2-2 = Library for LZO compression providing liblzo2.so.2
PKGFILES_CSWliblzo2-2 = $(call baseisadirs,$(libdir),liblzo2\.so\.2(\.\d+)*)

VENDOR_URL = http://www.oberhumer.com/opensource/lzo/

CONFIGURE_ARGS_isa-amd64 = --disable-asm

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

include gar/category.mk

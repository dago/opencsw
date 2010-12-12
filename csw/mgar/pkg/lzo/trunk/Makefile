NAME = lzo
VERSION = 2.03
CATEGORIES = utils

DESCRIPTION = LZO compression library
define BLURB
  LZO is a portable lossless data compression library written in ANSI C.
endef

MASTER_SITES = http://www.oberhumer.com/opensource/lzo/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.oberhumer.com/opensource/lzo/

CONFIGURE_ARGS_isa-amd64 = --disable-asm

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

include gar/category.mk

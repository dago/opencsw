# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
GARNAME = nasm
GARVERSION = 2.08.01
CATEGORIES = utils

DESCRIPTION = The Netwide Assembler
define BLURB
endef

MASTER_SITES = http://www.nasm.us/pub/nasm/releasebuilds/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LICENSE = LICENSE

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_ARGS = INSTALLROOT=$(DESTDIR)

include gar/category.mk

GARNAME = enchant
GARVERSION = 1.5.0
CATEGORIES = apps

DESCRIPTION = A generic spell checking library
define BLURB
endef

MASTER_SITES =  http://www.abisource.com/downloads/$(GARNAME)/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTNAME  = $(GARNAME)-$(GARVERSION)

PACKAGES = CSWenchant CSWenchantrt CSWenchantdevel CSWenchantdoc
CATALOGNAME_CSWenchant = enchant
CATALOGNAME_CSWenchantrt = enchant_rt
CATALOGNAME_CSWenchantdevel = enchant_devel
CATALOGNAME_CSWenchantdoc = enchant_doc

SPKG_DESC_CSWenchant += $(DESCRIPTION)
SPKG_DESC_CSWenchantrt += $(DESCRIPTION) - runtime package
SPKG_DESC_CSWenchantdevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWenchantdoc += $(DESCRIPTION) - documentation

PKGFILES_CSWenchantrt = $(PKGFILES_RT)
PKGFILES_CSWenchantrt += $(libdir)/.*\.so.*
PKGFILES_CSWenchantdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWenchantdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWenchantdoc = 1

RUNTIME_DEP_PKGS_CSWenchant += CSWenchantrt
RUNTIME_DEP_PKGS_CSWenchant += CSWggettextrt
RUNTIME_DEP_PKGS_CSWenchant += CSWglib2
RUNTIME_DEP_PKGS_CSWenchantrt += CSWaspell
RUNTIME_DEP_PKGS_CSWenchantrt += CSWdbusglib
RUNTIME_DEP_PKGS_CSWenchantrt += CSWggettextrt
RUNTIME_DEP_PKGS_CSWenchantrt += CSWglib2
RUNTIME_DEP_PKGS_CSWenchantrt += CSWlibdbus
RUNTIME_DEP_PKGS_CSWenchantdevel += CSWenchant
RUNTIME_DEP_PKGS_CSWenchantdoc += 

BUILD_DEP_PKGS += CSWdbusglibdev

LICENSE = COPYING.LIB

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.abisource.com/projects/enchant/

CHECKPKG_OVERRIDES_CSWenchant += symbol-not-found|enchant-lsmod
CHECKPKG_OVERRIDES_CSWenchant += symbol-not-found|enchant
CHECKPKG_OVERRIDES_CSWenchantrt += symbol-not-found|libenchant_ispell.so
CHECKPKG_OVERRIDES_CSWenchantrt += symbol-not-found|libenchant_aspell.so
CHECKPKG_OVERRIDES_CSWenchantrt += symbol-not-found|libenchant_myspell.so

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

NOISAEXEC = 1
#NOISALIST = 1
# libdbus not 64-bit yet
#BUILD64 = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

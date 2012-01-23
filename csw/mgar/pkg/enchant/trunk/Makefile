NAME = enchant
VERSION = 1.6.0
CATEGORIES = apps

DESCRIPTION = A wrapper library for various spell checking engines
define BLURB
endef

MASTER_SITES =  http://www.abisource.com/downloads/$(NAME)/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTNAME  = $(NAME)-$(VERSION)
SPKG_SOURCEURL = http://www.abisource.com/projects/enchant/


# THe subpackages just arent worth it, sizewise
# Leaving the other stuff in for 
#PACKAGES = CSWenchant CSWenchantrt CSWenchantdevel CSWenchantdoc
#
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

#RUNTIME_DEP_PKGS_CSWenchant += CSWenchantrt
RUNTIME_DEP_PKGS_CSWenchant += CSWggettextrt
RUNTIME_DEP_PKGS_CSWenchant += CSWglib2
RUNTIME_DEP_PKGS_CSWenchant += CSWaspell

### I dont know why someting thinks it needs dbus.
### neither /opt/csw/bin/enchant, nor its libs, needs it.
RUNTIME_DEP_PKGS_CSWenchantrt += CSWdbusglib
RUNTIME_DEP_PKGS_CSWenchantrt += CSWlibdbus

RUNTIME_DEP_PKGS_CSWenchantrt += CSWggettextrt
RUNTIME_DEP_PKGS_CSWenchantrt += CSWglib2
#RUNTIME_DEP_PKGS_CSWenchantdevel += CSWenchantrt
#RUNTIME_DEP_PKGS_CSWenchantdoc += 

BUILD_DEP_PKGS += CSWdbusglibdev

LICENSE = COPYING.LIB

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2


#CHECKPKG_OVERRIDES_CSWenchant += symbol-not-found|enchant-lsmod
#CHECKPKG_OVERRIDES_CSWenchant += symbol-not-found|enchant

CHECKPKG_OVERRIDES_CSWenchant += soname-not-found|libenchant.so.1|is|needed|by|opt/csw/bin/enchant
CHECKPKG_OVERRIDES_CSWenchant += soname-not-found|libenchant.so.1|is|needed|by|opt/csw/bin/enchant-lsmod

#CHECKPKG_OVERRIDES_CSWenchantrt += symbol-not-found|libenchant_ispell.so
#CHECKPKG_OVERRIDES_CSWenchantrt += symbol-not-found|libenchant_aspell.so
#CHECKPKG_OVERRIDES_CSWenchantrt += symbol-not-found|libenchant_myspell.so


#NOISALIST = 1
# libdbus not 64-bit yet
#BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

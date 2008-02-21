GARNAME = tme
GARVERSION = 0.6
CATEGORIES = apps

DESCRIPTION = The Machine Emulator
define BLURB
  The Machine Emulator, or tme, provides a general-purpose
  framework for computer emulation. The goal is to create a
  large library of modules, each emulating a specific computer
  chip, or bus, or board, etc. These modules offer standard
  interfaces that allow you to connect them together to create
  a whole machine emulation with a minimum of effort.
endef

MASTER_SITES = http://people.csail.mit.edu/fredette/tme/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWtme,)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

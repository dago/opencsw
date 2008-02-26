GARNAME = zsh
GARVERSION = 4.3.5
CATEGORIES = devel

DESCRIPTION = Powerful UNIX shell
define BLURB
  Zsh is a shell designed for interactive use, although it is also a
  powerful scripting language. Many of the useful features of bash,
  ksh, and tcsh were incorporated into zsh; many original features were added.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWzsh,postinstall postremove)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk


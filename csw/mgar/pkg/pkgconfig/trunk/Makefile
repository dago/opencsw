GARNAME = pkg-config
GARVERSION = 0.23
CATEGORIES = devel

DESCRIPTION = Tool for determining the configuration of installed software
define BLURB
  pkg-config is a helper tool used when compiling applications and libraries.
  It helps you insert the correct compiler options on the command line so an
  application can use  gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
  for instance, rather than hard-coding values on where to find glib (or other
  libraries). It is language-agnostic, so it can be used for defining the
  location of documentation tools, for instance.
endef

MASTER_SITES = http://pkg-config.freedesktop.org/releases/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpkgconfig,depend)

PATCHFILES = gsed-check.patch

PREREQUISITE_PKGS = CSWggettext CSWglib2 CSWiconv CSWsunmath

CONFIGURE_ARGS = $(DIRPATHS) --with-installed-glib

TEST_TARGET = check

include gar/category.mk

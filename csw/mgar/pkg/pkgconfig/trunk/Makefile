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
DISTFILES += fixme.sh

PACKAGES = pkgconfig

SPKG_SOURCEURL = http://pkg-config.freedesktop.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = gsed-check.patch

REQUIRED_PKGS = CSWggettextrt CSWglib2

CONFIGURE_ARGS = $(DIRPATHS) --with-installed-glib

TEST_TARGET = check

include gar/category.mk

post-configure-modulated:
	@echo " ==> Fixing libtool .la-files"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	@$(MAKECOOKIE)

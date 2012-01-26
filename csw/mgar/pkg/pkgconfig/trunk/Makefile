NAME = pkg-config
VERSION = 0.25
CATEGORIES = devel
GARTYPE = v2

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
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWpkgconfig
CATALOGNAME = pkgconfig

SPKG_SOURCEURL = http://pkg-config.freedesktop.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES  = manpage-macro.patch
PATCHFILES += 0001-Ugly-shell-fixes-and-force-gnome-config-to-be-there.patch

DEP_PKGS = CSWggettextrt CSWglib2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(docdir)/$(CATALOGNAME)
CONFIGURE_ARGS += --with-installed-glib

include gar/category.mk

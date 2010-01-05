GARNAME = libproxy
GARVERSION = 0.3.0
CATEGORIES = lib

DESCRIPTION = A library that provides automatic proxy configuration management
define BLURB
  libproxy exists to answer the question: Given a network resource, how do I
  reach it? It handles all the details, enabling you to get back to programming.
  GNOME? KDE? Command line? WPAD? PAC? Network changed? It doesn't matter! Just
  ask libproxy what proxy to use: you get simple code and your users get correct,
  consistant behavior and broad infrastructure compatibility.
endef

MASTER_SITES = http://libproxy.googlecode.com/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES  = 0001-Use-xc99-for-Sun-Studio-compiler.patch
PATCHFILES += 0002-Dont-preset-CFLAGS.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

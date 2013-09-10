# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libreoffice
VERSION = 4.1.1.2
GARTYPE = v2

DESCRIPTION = Libre Office

MASTER_SITES = http://download.documentfoundation.org/libreoffice/src/4.1.1/
DISTFILES += libreoffice-$(VERSION).tar.xz
DISTFILES += libreoffice-dictionaries-$(VERSION).tar.xz
DISTFILES += libreoffice-help-$(VERSION).tar.xz
DISTFILES += libreoffice-translations-$(VERSION).tar.xz

EXTRA_INC += /usr/openwin/share/include
EXTRA_INC += /usr/X11/include
EXTRA_LIB += /usr/X11/lib
EXTRA_CPPFLAGS += -D_XFUNCPROTOBEGIN= -D_XFUNCPROTOEND=

CONFIGURE_ARGS = $(DIRPATHS)

# We probably have libxext headers on OpenCSW, but better skip them
CONFIGURE_ARGS += --without-system-xextensions-headers

include gar/category.mk


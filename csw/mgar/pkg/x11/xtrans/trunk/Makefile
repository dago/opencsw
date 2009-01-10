GARNAME = xtrans
GARVERSION = 1.2.2
CATEGORIES = x11

DESCRIPTION = X transport library
define BLURB
xtrans includes a number of routines to make X implementations transport-independent; at time of writing, it includes support for UNIX sockets, IPv4, IPv6, and DECnet.
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWxtrans = X transport library

DISTFILES    += $(call admfiles,CSWxtrans, )

include gar/category.mk


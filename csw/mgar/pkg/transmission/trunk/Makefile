GARNAME = transmission
GARVERSION = 1.76
CATEGORIES = net

DESCRIPTION = Fast, easy, and free multi-platform BitTorrent client
define BLURB
endef
MASTER_SITES = http://mirrors.m0k.org/transmission/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
PATCHFILES = icons-makefile.patch
PATCHFILES += linker-include.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

PACKAGES  = CSWtransmisson
PACKAGES += CSWtransmissongtk2
SPKG_DESC_CSWtransmisson = Fast, easy, and free multi-platform BitTorrent client
SPKG_DESC_CSWtransmissongtk2 = Fast, easy, and free multi-platform BitTorrent client ,  gtk2 Interface

REQUIRED_PKGS_CSWtransmissongtk2 = CSWcurlrt
REQUIRED_PKGS_CSWtransmissongtk2 += CSWdbusglib
REQUIRED_PKGS_CSWtransmissongtk2 += CSWfconfig
REQUIRED_PKGS_CSWtransmissongtk2 += CSWftype2
REQUIRED_PKGS_CSWtransmissongtk2 += CSWggettextrt
REQUIRED_PKGS_CSWtransmissongtk2 += CSWglib2
REQUIRED_PKGS_CSWtransmissongtk2 += CSWgtk2
REQUIRED_PKGS_CSWtransmissongtk2 += CSWlibatk
REQUIRED_PKGS_CSWtransmissongtk2 += CSWlibcairo
REQUIRED_PKGS_CSWtransmissongtk2 += CSWlibdbus
REQUIRED_PKGS_CSWtransmissongtk2 += CSWlibevent
REQUIRED_PKGS_CSWtransmissongtk2 += CSWlibxext
REQUIRED_PKGS_CSWtransmissongtk2 += CSWosslrt
REQUIRED_PKGS_CSWtransmissongtk2 += CSWpango
REQUIRED_PKGS_CSWtransmissongtk2 += CSWzlib
REQUIRED_PKGS_CSWtransmissongtk2 += CSWdbus

REQUIRED_PKGS_CSWtransmisson = CSWcurlrt
REQUIRED_PKGS_CSWtransmisson += CSWlibevent
REQUIRED_PKGS_CSWtransmisson += CSWggettextrt
REQUIRED_PKGS_CSWtransmisson += CSWosslrt
REQUIRED_PKGS_CSWtransmisson += CSWzlib



REQUIRED_PKGS_CSWtransmissongtk2 += CSWtransmisson

PKGFILES_CSWtransmisson  = /opt/csw/bin/transmissioncli
PKGFILES_CSWtransmisson  += /opt/csw/bin/transmission-.*
PKGFILES_CSWtransmisson  += /opt/csw/share/locale/.*
PKGFILES_CSWtransmisson  += /opt/csw/share/man/.*
PKGFILES_CSWtransmisson  += /opt/csw/share/transmission/.*

CATALOGNAME_CSWtransmisson = transmisson
CATALOGNAME_CSWtransmissongtk2 = transmisson_gtk2


EXTRA_CFLAGS = -DNO_SYS_QUEUE_H -lresolv -mt

EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS) --enable-gtk

TEST_TARGET = check

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)

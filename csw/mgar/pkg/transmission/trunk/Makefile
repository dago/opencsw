GARNAME = transmission
GARVERSION = 1.80
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

PACKAGES  = CSWtransmission
PACKAGES += CSWtransmissiongtk2
SPKG_DESC_CSWtransmission = Fast, easy, and free multi-platform BitTorrent client
SPKG_DESC_CSWtransmissiongtk2 = Fast, easy, and free multi-platform BitTorrent client ,  gtk2 Interface

REQUIRED_PKGS_CSWtransmissiongtk2 = CSWcurlrt
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWdbusglib
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWfconfig
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWftype2
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWggettextrt
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWglib2
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWgtk2
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWlibatk
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWlibcairo
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWlibdbus
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWlibevent
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWlibxext
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWosslrt
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWpango
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWzlib
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWdbus
REQUIRED_PKGS_CSWtransmissiongtk2 += CSWgconf2

REQUIRED_PKGS_CSWtransmission = CSWcurlrt
REQUIRED_PKGS_CSWtransmission += CSWlibevent
REQUIRED_PKGS_CSWtransmission += CSWggettextrt
REQUIRED_PKGS_CSWtransmission += CSWosslrt
REQUIRED_PKGS_CSWtransmission += CSWzlib



REQUIRED_PKGS_CSWtransmissiongtk2 += CSWtransmission

PKGFILES_CSWtransmission  = /opt/csw/bin/transmissioncli
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-.*
PKGFILES_CSWtransmission  += /opt/csw/share/locale/.*
PKGFILES_CSWtransmission  += /opt/csw/share/man/.*
PKGFILES_CSWtransmission  += /opt/csw/share/transmission/.*

CATALOGNAME_CSWtransmission = transmission
CATALOGNAME_CSWtransmissiongtk2 = transmission_gtk2


EXTRA_CFLAGS = -DNO_SYS_QUEUE_H -lresolv 

EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS) --enable-gtk 
STRIP_LIBTOOL = 1

TEST_TARGET = check

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)

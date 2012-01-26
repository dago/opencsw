NAME = transmission
VERSION = 2.20
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Fast, easy, and free multi-platform BitTorrent client
define BLURB
endef
MASTER_SITES = http://download.transmissionbt.com/files/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES = icons-makefile.patch
PATCHFILES += 0001-fix-include-and-test.patch
PATCHFILES += 0003-fix-usr-share.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

PACKAGES  = CSWtransmission
PACKAGES += CSWtransmissiongtk2
SPKG_DESC_CSWtransmission = Fast, easy, and free multi-platform BitTorrent client
SPKG_DESC_CSWtransmissiongtk2 = Transmission  BitTorrent client , gtk2 Interface

RUNTIME_DEP_PKGS_CSWtransmissiongtk2 = CSWcurlrt
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWdbusglib
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWftype2
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWgtk2
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWglib2
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWlibatk
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWlibcairo
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWlibdbus
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWosslrt
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWpango
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWzlib
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWdbus
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWgconf2
RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWiconv


RUNTIME_DEP_PKGS_CSWtransmission = CSWcurlrt
RUNTIME_DEP_PKGS_CSWtransmission += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWtransmission += CSWggettextrt
RUNTIME_DEP_PKGS_CSWtransmission += CSWosslrt
RUNTIME_DEP_PKGS_CSWtransmission += CSWzlib
RUNTIME_DEP_PKGS_CSWtransmission += CSWiconv




RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWtransmission

PKGFILES_CSWtransmission  = /opt/csw/bin/transmission-cli
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-create
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-daemon
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-edit
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-show
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-remote
PKGFILES_CSWtransmission  += /opt/csw/share/locale/.*
PKGFILES_CSWtransmission  += /opt/csw/share/man/.*
PKGFILES_CSWtransmission  += /opt/csw/share/transmission/.*

CATALOGNAME_CSWtransmission = transmission
CATALOGNAME_CSWtransmissiongtk2 = transmission_gtk2


#EXTRA_CFLAGS = -DNO_SYS_QUEUE_H -lresolv 
EXTRA_CFLAGS = -DNO_SYS_QUEUE_H -lintl
EXTRA_LD_OPTIONS = -L/opt/csw/lib -liconv -lrt

#EXTRA_INC = /opt/csw/X11/include
#EXTRA_LIB = /opt/csw/X11/lib 
#EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS) --enable-gtk --disable-silent-rules
STRIP_LIBTOOL = 1

CHECKPKG_OVERRIDES_CSWtransmissiongtk2 += surplus-dependency|CSWtransmission
CHECKPKG_OVERRIDES_CSWtransmissiongtk2 += surplus-dependency|CSWdbus



include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)

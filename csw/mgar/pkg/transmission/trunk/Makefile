NAME = transmission
# Can't get newer version, as long as we lack GTK3+
VERSION = 2.52
GARTYPE = v2

GARCOMPILER = GNU net
GARTYPE = v2

DESCRIPTION = Fast, easy, and free multi-platform BitTorrent client
define BLURB
endef
MASTER_SITES = http://download.transmissionbt.com/files/
DISTFILES  = $(NAMExzx-usr-share.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\dxz

PATCHFILES += 0001-minupnpc.c-add-missing-preproc-test.patch
PATCHFILES += 0002-utils-test.c-fix-test.patch
PATCHFILES += 0003-platform.c-remove-usr-local-share-and-add-opt-csw-sh.patch:\.\d+)*).tar.bz2

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
RUNTIME_DEP_PKGS_CSWtransmis += CSWiconv




RUNTIME_DEP_PKGS_CSWtransmissiongtk2 += CSWtransmission

PKGFILES_CSWtransmission  = /opt/csw/bin/transmission-cli
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-create
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-daemon
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-edit
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-show
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-remote
PKGFILES_CSWtransmission  += /opt/csw/share/locale/.*
PKGFILES_CSWtransmission  += /opt/csw/share/man/.*
PKGFILES_CSWtransmission  += /opt/csw/share/BUILD_DEP_PKGS += CSWlibcurl-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibevent-dev
BUILD_DEP_PKGS += CSWintltool

CATALOGNAME_CSWtransmission = transmission
CATALOGNAME_CSWtransmissiongtk2 = transmission_gtk2

EXTRA_LINKER_FLAGS = -lintl -liconv


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --enable-daemonendency|CSWdbus



include gar/category.mk
PATH := /opt
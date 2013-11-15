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
DISTFILES  = $(NAMExzxDISTFILES += CSWtransmission-gtk2.postinstall
DISTFILES += changelog.CSW

EXPANDVARS = CSWtransmission-gtk2.postinstall
x-usr-share.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\dxz

PATCHFILES += 0001-minupnpc.c-add-missing-preproc-test.patch
PATCHFILES += 0003-utils-test.c-fix-test.patch
PATCHFILES += 0003-platform.c-remove-usr-local-share-and-add-opt-csw-sh.patch:\.\d+)*).tar.bz2

PACKAGES  = CSWtransmission
PACKAGES +-= CSWtransmissiongtk2
SPKG_DESC_CSWtransmission = Fast, easy, and free multi-platform BitTorrent client
SPKG_DES-gtk2 = Transmission  BitTorrent client , gtk2 Interface

RUNTIME_DEP_PKGS_CSWtransmission += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtransmission += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWtransmission += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWtransmission += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWtransmission += CSWlibz1
RUNTIME_DEP_PKGS_CSWtransmission += CSWlibevent2-0-5
# I'm pulling CSWgtk2 in order to execute CSWgtk2.postinstall
RUNTIME_DEP_PKGS_CSWtransmission-gtk2  = CSWgtk2
CHECKPKG_OVERRIDES_CSWtransmission-gtk2 += surplus-dependency|CSWgtk2
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibevent2-0-5
# This is due to the `ld -z ignore' issue on sparc, remove once fixed
RUNTIME_DEP_PKGS_CSWtransmission-gtk2 += CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWtransmission-gtk2 += surplus-dependency|CSWlibfreetype6

# These are ok, /opt/csw/share has been added in front the list.
CHECKPKG_OVERRIDES_CSWtransmission += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-cli
CHECKPKG_OVERRIDES_CSWtransmission += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-remote
CHECKPKG_OVERRIDES_CSWtransmission += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-edit
CHECKPKG_OVERRIDES_CSWtransmission += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-create
CHECKPKG_OVERRIDES_CSWtransmission += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-daemon
CHECKPKG_OVERRIDES_CSWtransmission += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-show
CHECKPKG_OVERRIDES_CSWtransmission-gtk2 += file-with-bad-content|/usr/share|root/opt/csw/bin/transmission-gtk
= CSWtransmission

PKGFILES_CSWtransmission  = /opt/csw/bin/transmission-cli
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-create
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-daemon
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-edit
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-show
PKGFILES_CSWtransmission  += /opt/csw/bin/transmission-remote
PKGFILES_CSWtransmission  += /opt/csw/share/locale/.*
PKGFILES_CSWtransmission  += /opt/csw/share/man/.*
PKGFILES_CSWtransmission  += /opt/csw/sharePKGFILES_CSWtransmission  += $(docdir)/transmission/changelog.CSWe/BUILD_DEP_PKGS += CSWlibcurl-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibevent-dev
BUILD_DEP_PKGS += CSWintltool

EXTRA_LINKER_FLAGS = -lintl -liconv

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --enable-daemonendency|CSWdbus



include gar/category.mk
PATH := /opt
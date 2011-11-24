NAME = wireshark
VERSION = 1.6.4
CATEGORIES = apps

DESCRIPTION = Wireshark (was Ethereal) is a free network protocol analyzer
define BLURB
  Wireshark is the world's foremost network protocol analyzer, and is the
  de facto (and often de jure) standard across many industries and
  educational institutions.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Solaris-9-doesn-t-have-stdint.h.patch

# Use patch until this is fixed:
#   https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6615
PATCHFILES += 0002-Don-t-return-value-in-void-functions.patch

VENDOR_URL = http://www.wireshark.org/

BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWgtk2devel
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibcares-dev
BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWlibsmi-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWlibgnutls-dev
BUILD_DEP_PKGS += CSWlua
BUILD_DEP_PKGS += CSWgeoip-dev

PACKAGES += CSWwireshark
SPKG_DESC_CSWwireshark = Wireshark (was Ethereal) is a free network protocol analyzer
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWwireshark += CSWglib2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWwireshark += CSWgtk2
RUNTIME_DEP_PKGS_CSWwireshark += CSWpango
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibz1
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibintl8
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibcares2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibsmi2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWwireshark += CSWosslrt
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWwireshark += CSWlua
RUNTIME_DEP_PKGS_CSWwireshark += CSWftype2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibatk
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWwireshark += CSWgeoip
RUNTIME_DEP_PKGS_CSWwireshark += CSWfconfig

# No more library splitting unless absolutely necessary
CHECKPKG_OVERRIDES_CSWwireshark += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWwireshark += non-uniform-lib-versions-in-package

# example, \fI/usr/local/share/wireshark/preferences\fR) on UNIX-compatible
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/rawshark.1
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/wireshark/rawshark.html

# \&\fI/usr/local/lib/wireshark/plugins/$VERSION\fR), and then
# example, \fI/usr/local/share/wireshark/preferences\fR) on UNIX-compatible
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/wireshark.1
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/wireshark/wireshark.html

# example, \fI/usr/local/share/wireshark/preferences\fR) on UNIX-compatible
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/tshark.1
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/wireshark/tshark.html

REINPLACEMENTS += mibs
REINPLACE_MATCH_mibs = /usr/share/snmp/mibs
REINPLACE_WITH_mibs = /opt/csw/share/mibs
REINPLACE_FILES_mibs += epan/oids.c

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-usr-local=no
CONFIGURE_ARGS += --with-ssl=/opt/csw

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

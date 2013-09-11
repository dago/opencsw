NAME = wireshark
VERSION = 1.10.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Wireshark (was Ethereal) is a free network protocol analyzer
define BLURB
  Wireshark is the world's foremost network protocol analyzer, and is the
  de facto (and often de jure) standard across many industries and
  educational institutions.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

#new glib2 only on Solaris 10
PACKAGING_PLATFORMS = solaris10-spar solaris10-i386


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
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS +=BUILD_DEP_PKGS += CSWliblua5-2DEP_PKGS += CSWlua
BUILD_DEP_PKGS += CSWgeoip-dev

# Lua support disabled because luaL_register is checked during autoconf which
# is deprecated as described in http://lua-users.org/wiki/LuaFiveTwo
#  https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7409

PACKAGES += CSWwireshark
SPKG_DESC_CSWwireshark = Wireshark (was Ethereal) is a free network protocol analyzer
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWwireshark += CSWpango
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibz1
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibcares2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibsmi2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWwireshar8 reshark += CSWlua
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWwilib2-0-0
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgtk-x11-hark +RUNTIME_DEP_PKGS_CSWwireshark += CSWliblua5-2+= CSWlibglib2-0-0

# No more library splitting unless absolutely necessary
CHECKPKG_OVERRIDES_CSWwireshark += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWwireshark += shared-lib-pkgname-mismatch

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
REINPLACE_FILES_mibs This is now deprecated in Pango, use workaround until Pango is updated
EXTRA_CFLAGS += -DG_CONST_RETURN=const

# Hardcode ipv6 until this is fixed (taken from acinclude.m4):
#   https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8813
#EXTRA_CFLAGS += -DINET6 -DSOLARIS8_INET6PATH_LINKER_FLAGS)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-usr-local=no
CONFIGURE_ARGS += --with-ssl=/opt/csw

include gar/category.mk

PATH := /op
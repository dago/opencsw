# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = netatalk
VERSION = 3.0.3
GARTYPE = v2

DESCRIPTION = Open Source AFP fileserver
define BLURB
  Netatalk is a freely-available Open Source AFP fileserver. A *NIX/*BSD system
  running Netatalk is capable of serving many Macintosh clients simultaneously
  as an AppleShare file server (AFP).B
  Long description
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  =DISTFILES += CSWnetatalk.postinstall CSWnetatalk.preremove

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWbdb48devel
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWlibdbus-dev
BUILD_DEP_PKGS += CSWlibdbus-glib-dev

RUNTIME_DEP_PKGS += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS += CSWlibgcrypt11
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS += CSWlibkrb5-3
RUNTIME_DEP_PKGS += CSWlibglib2-0-0
RUNTIME_DEP_PKGS += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWlibldap2-4-2
RUNTIME_DEP_PKGS += CSWbdb48

# Patches are in upstream and will be in 3.0.4
PATCHFILES += 0000-Add-rpath-for-bdb.patch
PATCHFILES += 0001-Fix-use-of-unnamed-union-inside-struct.patch
PATCHFILES += 0003-Fix-misspelled-compiler-variable.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --libdir=$(prefix)/lib/netatalk
CONFIGURE_ARGS += --with-uams-path=$(prefix)/lib/netatalk
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --disable-tcp-wrappers
CONFIGURE_ARGS += --with-bdb=/opt/csw/bdb48
CONFIGURE_ARGS += --with-lockfile=/var/opt/csw/run/netatalk
CONFIGURE_ARGS += --with-init-style=solaris
CONFIGURE_ARGS += --with-init-dir=/var/opt/csw/svc/manifest/network/NK# Path to XML dtd
CHECKPKG_OVERRIDES_CSWnetatalk += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/netatalk.xml


include gar/category.mk


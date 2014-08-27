# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = netatalk
VERSION = 3.1.6
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
GARCOMPILER = GNU

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
# Solaris 11 for Zeroconf support
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386

BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWbdb48devel
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWlibdbus-dev
BUILD_DEP_PKGS += CSWlibdbus-glib-dev
BUILD_DEP_PKGS += CSWlibtracker-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWopenldap-dev
BUILD_DEP_PKGS += CSWlibpcre-dev

RUNTIME_DEP_PKGS += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS += CSWlibgcrypt20
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS += CSWlibkrb5-3
RUNTIME_DEP_PKGS += CSWlibglib2-0-0
RUNTIME_DEP_PKGS += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWbdb48
RUNTIME_DEP_PKGS += CSWlibtracker-sparql1-0-0
RUNTIME_DEP_PKGS += CSWlibgio2-0-0
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibldap2-4-2
RUNTIME_DEP_PKGS += CSWlibssl1-0-0

RUNTIME_DEP_PKGS_sparc_5.10 = CSWlibgmodule2-0-0 CSWlibintl8 CSWlibk5crypto3 CSWlibcom-err3 CSWlibgpg-error0
RUNTIME_DEP_PKGS += $(RUNTIME_DEP_PKGS_$(GARCH)_$(GAROSREL)) $(RUNTIME_DEP_PKGS_$(GARCH))

PATCHFILES += 0001-Disable-noinst-binary-fails-to-link-on-SPARC.patch
PATCHFILES += 0002-Ensure-gsettings-is-called-from-opt-csw-bin.patch
PATCHFILES += 0003-Disable-dbus-start-by-default.patch

PRESERVECONF += $(sysconfdir)/afp.conf
PRESERVECONF += $(sysconfdir)/extmap.conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --libdir=$(prefix)/lib/netatalk
CONFIGURE_ARGS += --with-uams-path=$(prefix)/lib/netatalk
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --disable-tcp-wrappers
CONFIGURE_ARGS += --with-bdb=/opt/csw/bdb48
CONFIGURE_ARGS += --with-lockfile=/var/opt/csw/run/netatalk
CONFIGURE_ARGS += --enable-krbV-uam
CONFIGURE_ARGS += --with-tracker-prefix=/opt/csw
CONFIGURE_ARGS += --with-tracker-pkgconfig-version=1.0
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw
CONFIGURE_ARGS += --with-ldap=/opt/csw
# compiling with MySQL on opencsw is a major pita atm :)
CONFIGURE_ARGS += --with-mysql-config=no
K# Path to XML dtd
CHECKPKG_OVERRIDES_CSWnetatalk += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswnetatalk.xml
CHECKPKG_OVERRIDES_CSWnetatalk += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/system/cswnetatalk-tracker-miner-fs.xml
CHECKPKG_OVERRIDES_CSWnetatalk += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/system/cswnetatalk-tracker-extract.xml
CHECKPKG_OVERRIDES_CSWnetatalk += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/system/cswnetatalk-dbus.xml
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/bin/afppasswd
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/lib/netatalk/uams_dhx_pam.so
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/lib/netatalk/uams_dhx_passwd.so
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/lib/netatalk/uams_randnum.so
CHECKPKG_OVERRIDES_CSWnetatalk_sparc_5.10 = surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWnetatalk += $(CHECKPKG_OVERRIDES_CSWnetatalk_$(GARCH)_$(GAROSREL))

include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)/var/opt/csw/svc/manifest/network
	ginstall -d -m 755 $(DESTDIR)/var/opt/csw/svc/manifest/system
	ginstall -m 444 $(FILEDIR)/cswnetatalk.xml $(DESTDIR)/var/opt/csw/svc/manifest/network/
	ginstall -m 444 $(FILEDIR)/cswnetatalk-dbus.xml $(DESTDIR)/var/opt/csw/svc/manifest/system/
	ginstall -m 444 $(FILEDIR)/cswnetatalk-tracker-extract.xml $(DESTDIR)/var/opt/csw/svc/manifest/system/
	ginstall -m 444 $(FILEDIR)/cswnetatalk-tracker-miner-fs.xml $(DESTDIR)/var/opt/csw/svc/manifest/system/
	@$(MAKECOOKIE)

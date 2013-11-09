# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = netatalk
VERSION = 3.1.0
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
RUNTIME_DEP_PKGS += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS += CSWlibtracker-sparql0-16-0
RUNTIME_DEP_PKGS += CSWlibtracker-miner0-16-0
RUNTIME_DEP_PKGS += CSWlibgio2-0-0
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibssl1-0-0
# needed because of 7051963 but fails checkpkg
# http://lists.opencsw.org/pipermail/maintainers/2013-November/018794.html
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWlibk5crypto3
RUNTIME_DEP_PKGS += CSWlibcom-err3
RUNTIME_DEP_PKGS += CSWlibgmodule2-0-0

PATCHFILES += 0003-Disable-noinst-binary-fails-to-link-on-SPARC.patch
# will be in 3.1.1
PATCHFILES += uam.patch

# Don't know yet why but this dependency is only picked under sparc
RUNTIME_DEP_PKGS_sparc = CSWlibgpg-error0
RUNTIME_DEP_PKGS += $(RUNTIME_DEP_PKGS_$(GARCH))

REINPLACEMENTS += manifest1
REINPLACE_MATCH_manifest1 = network/netatalk
REINPLACE_WITH_manifest1 = network/cswnetatalk
REINPLACE_FILES_manifest1 += distrib/initscripts/netatalk.xml.tmpl

REINPLACEMENTS += manifest2
REINPLACE_MATCH_manifest2 = name="netatalk"
REINPLACE_WITH_manifest2 =  name="cswnetatalk"
REINPLACE_FILES_manifest2 += distrib/initscripts/netatalk.xml.tmpl

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
CONFIGURE_ARGS += --with-tracker-pkgconfig-version=0.16
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw
# disable until asprintf() compat func is available in 3.1.1
CONFIGURE_ARGS += --with-mysql-config=no
K# Path to XML dtd
CHECKPKG_OVERRIDES_CSWnetatalk += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswnetatalk.xml
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/bin/afppasswd
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/lib/netatalk/uams_dhx_pam.so
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/lib/netatalk/uams_dhx_passwd.so
CHECKPKG_OVERRIDES_CSWnetatalk += bad-rpath-entry|/opt/csw|opt/csw/lib/netatalk/uams_randnum.so

include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)/var/opt/csw/svc/manifest/network
	ginstall -m 444 $(WORKSRC)/distrib/initscripts/netatalk.xml $(DESTDIR)/var/opt/csw/svc/manifest/network/
	mv $(DESTDIR)/var/opt/csw/svc/manifest/network/netatalk.xml $(DESTDIR)/var/opt/csw/svc/manifest/network/cswnetatalk.xml
	@$(MAKECOOKIE)

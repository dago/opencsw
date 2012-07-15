# $Id$
NAME = idzebra
VERSION = 2.0.52
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A high-performance, general-purpose structured text indexing and retrieval engine
define BLURB
endef

MASTER_SITES = http://ftp.indexdata.dk/pub/zebra/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.indexdata.com/zebra

LICENSE = LICENSE.zebra

# Many more missing
BUILD_DEP_PKGS += CSWlibyaz-dev

# DEP_PKGS = CSWyaz CSWgcrypt CSWexpat CSWlibxml2 CSWlibxslt CSWbzip2 CSWgpgerr CSWiconv CSWtcl CSWzlib

PACKAGES += CSWidzebra
SPKG_DESC_CSWidzebra = A high-performance, general-purpose structured text indexing and retrieval engine
# I have no idea how this is split, leave as one package for now
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibyaz-icu4
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibz1
RUNTIME_DEP_PKGS_CSWidzebra += CSWtcl
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibyaz-server4
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWidzebra += CSWlibgcrypt11

# Leave everything for now
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/share|root/opt/csw/share/idzebra-2.0-examples/oai-pmh/conf/zebra.cfg
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/share|root/opt/csw/share/doc/idzebra-2.0/installation-upgrade.html
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/share|root/opt/csw/share/doc/idzebra-2.0/tutorial.html
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/idzebra-config-2.0.1
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/local|root/opt/csw/share/doc/idzebra-2.0/zebra-cfg.html
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/local|root/opt/csw/share/doc/idzebra-2.0/idzebra-config.html
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/local|root/opt/csw/share/doc/idzebra-2.0/installation.html
CHECKPKG_OVERRIDES_CSWidzebra += file-with-bad-content|/usr/local|root/opt/csw/share/doc/idzebra-2.0/simple-indexing.html
CHECKPKG_OVERRIDES_CSWidzebra += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libidzebra-2.0.so
CHECKPKG_OVERRIDES_CSWidzebra += shared-lib-pkgname-mismatch|file=opt/csw/lib/libidzebra-2.0.so.0.0.1|soname=libidzebra-2.0.so.0|pkgname=CSWidzebra|expected=CSWlibidzebra2-0-0
CHECKPKG_OVERRIDES_CSWidzebra += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libidzebra-2.0.so

# Just wait a _little_ longer until Tcl is released in 64 bit
# BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

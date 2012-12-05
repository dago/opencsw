# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = courier-imap
VERSION = 4.11.0
GARTYPE = v2

DESCRIPTION = Courier IMAP
define BLURB
   Courier IMAP
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT = courier/imap
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWcourier-imap
SPKG_DESC_CSWcourier-imap = Courier IMAP
BUILD_DEP_PKGS_CSWcourier-imap += CSWmysql-dev
BUILD_DEP_PKGS_CSWcourier-imap += CSWpostgresql-dev
BUILD_DEP_PKGS_CSWcourier-imap += CSWopenldap-dev
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibpq5
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibldap2-4-2
OBSOLETED_BY_CSWcourier-imap += CSWcourierauth

MIGRATE_SOURCE_DIR_CSWcourier-imap = $(prefix)/etc/courier-imap
MIGRATE_DEST_DIR_CSWcourier-imap = $(sysconfdir)/courier-imap

PRESERVECONF += imapd
PRESERVECONF += pop3d
PRESERVECONF += imapd-ssl
PRESERVECONF += pop3d-ssl
PRESERVECONF += imapd.cnf
PRESERVECONF += pop3d.cnf

PACKAGES += CSWcourier-imap-dev
SPKG_DESC_CSWcourier-imap-dev = Courier IMAP development files
PKGFILES_CSWcourier-imap-dev = $(PKGFILES_DEVEL)

include gar/category.mk


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
DISTFILES += cswcourier-imap.xml
DISTFILES += cswcourier-imap

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

sysconfdir = /etc/opt/csw/courier-imap
localstatedir = /var/opt/csw/courier-imap
datadir = /opt/csw/share/courier-imap
libexecdir = /opt/csw/libexec/courier-imap

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-root-check
CONFIGURE_ARGS += --with-waitfunc=wait3
CONFIGURE_ARGS += --enable-unicode
CONFIGURE_ARGS += --with-db=gdbm
CONFIGURE_ARGS += --with-userdb=/etc/opt/csw/authlib/userdb
CONFIGURE_ARGS += --with-certsdir=$(sysconfdir)
CONFIGURE_ARGS += --with-certdb=/etc/opt/csw/ssl/certs/ca-certificates.crt

REINPLACE_USRLOCAL += $(mandir)/man1/maildirmake.1
REINPLACE_WHEN_USRLOCAL = postinstall

PACKAGES = CSWcourier-imap
SPKG_DESC_CSWcourier-imap = Courier IMAP
BUILD_DEP_PKGS_CSWcourier-imap += CSWcourier-authlib-dev
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibidn11
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibfam0
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWcourier-imap += CSWcourier-authlib
OBSOLETED_BY_CSWcourier-imap += CSWcourierimap
EXTRA_LIB = $(prefix)/lib/courier-authlib

INITSMF = /etc/opt/csw/init.d/cswcourier-imap

TEST_SCRIPTS =

MIGRATE_SOURCE_DIR_CSWcourier-imap = $(prefix)/etc/courier-imap
MIGRATE_DEST_DIR_CSWcourier-imap = $(sysconfdir)

PRESERVECONF += imapd
PRESERVECONF += pop3d
PRESERVECONF += imapd-ssl
PRESERVECONF += pop3d-ssl
PRESERVECONF += imapd.cnf
PRESERVECONF += pop3d.cnf

# SMF override
CHECKPKG_OVERRIDES_CSWcourier-imap += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswcourier-imap.xml

include gar/category.mk

post-install-modulated:
	 @/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/init.d
	 @/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/var/opt/csw/svc/manifest/network
	 @/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	 @/opt/csw/bin/ginstall -m 755 $(FILEDIR)/cswcourier-imap $(DESTDIR)/$(INITSMF)
	 @/opt/csw/bin/ginstall -m 644 $(FILEDIR)/cswcourier-imap.xml $(DESTDIR)/var/opt/csw/svc/manifest/network/cswcourier-imap.xml
	 @$(MAKECOOKIE)


# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pidentd
VERSION = 3.0.19
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Portable ident daemon
define BLURB
endef

MASTER_SITES = ftp://ftp.stack.nl/pub/users/johans/pidentd/
DISTFILES  = $(DISTNAME).tar.gz

PATCHDIRLEVEL = 0

# From ftp://ftp.stack.nl/pub/users/johans/pidentd/
PATCHFILES += pidentd-3.0.19-ipv6-20080101.diff.gz

# From http://www.vlakno.cz/~rdivacky/pidentd.diff
PATCHFILES += pidentd.diff

# We need a specific version for each release
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

VENDOR_URL = http://www.lysator.liu.se/~pen/pidentd/

LICENSE = README

PACKAGES += CSWpidentd
SPKG_DESC_CSWmypkg = Portable ident daemon
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpidentd += CSWlibssl0-9-8

# This is ok as it references the DTD
CHECKPKG_OVERRIDES_CSWpidentd += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswidentd.xml

REINPLACEMENTS += ignoreisa
REINPLACE_MATCH_ignoreisa = ISA="
REINPLACE_WITH_ignoreisa = ISA="IGNORE
REINPLACE_FILES_ignoreisa += configure

REINPLACE_USRLOCAL += etc/identd.init

REINPLACEMENTS += usrlocaletc
REINPLACE_MATCH_usrlocaletc = /usr/local/etc
REINPLACE_WITH_usrlocaletc = /etc/opt/csw
REINPLACE_FILES_usrlocaletc = etc/identd.conf

REINPLACEMENTS += pidfile
REINPLACE_MATCH_pidfile = /etc/identd.pid
REINPLACE_WITH_pidfile = /var/run/identd.pid
REINPLACE_FILES_pidfile +=  src/pidentd.h
REINPLACE_FILES_pidfile += etc/identd.init
REINPLACE_FILES_pidfile += etc/identd.conf
REINPLACE_FILES_pidfile += doc/identd.8

REINPLACEMENTS += localconf
REINPLACE_MATCH_localconf = /etc/identd.conf
REINPLACE_WITH_localconf = $(sysconfdir)/identd.conf
REINPLACE_FILES_localconf += etc/identd.conf

REINPLACEMENTS += daemon
REINPLACE_MATCH_daemon = /usr/sbin/in.identd
REINPLACE_WITH_daemon = $(sbindir)/identd -b
REINPLACE_FILES_daemon = etc/identd.xml

REINPLACEMENTS += customsmf
REINPLACE_MATCH_customsmf = \#  You.*
REINPLACE_WITH_customsmf = \# MANIFEST /var/opt/csw/svc/manifest/network/cswidentd.xml
REINPLACE_FILES_customsmf += etc/identd.init

BUILD64 = 1
ISAEXEC = 1

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += mandir
INSTALL_OVERRIDE_VAR_mandir = $(DESTDIR)$(mandir)
INSTALL_OVERRIDE_VARS += sbindir
INSTALL_OVERRIDE_VAR_sbindir = $(DESTDIR)$(sbindir)

INITSMF += $(sysconfdir)/init.d/cswidentd

PRESERVECONF += /etc/opt/csw/identd.conf
PRESERVECONF += /opt/csw/etc/identd.conf

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall $(WORKSRC)/etc/identd.conf $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)/opt/csw/etc
	ginstall $(WORKSRC)/etc/identd.conf $(DESTDIR)/opt/csw/etc
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall $(WORKSRC)/etc/identd.init $(DESTDIR)$(sysconfdir)/init.d/cswidentd
	ginstall -d $(DESTDIR)/var/opt/csw/svc/manifest/network
	ginstall $(WORKSRC)/etc/identd.xml $(DESTDIR)/var/opt/csw/svc/manifest/network/cswidentd.xml



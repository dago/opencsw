# TODO (release-critical prefixed with !, non release-critical with *)
#
# * postinstall mknod not possible within zone (mknod fails with "not owner")
#   Work around this or provide README.CSW with instructions for chroot
#   --> Why should /dev/zero be required at all? google suggests relation
#       to pthreads .. truss doesn't show /dev/zero usage on Solaris 10
#       Test on Solaris 8 / 9 for comparison
#
NAME = stunnel
VERSION = 5.18
BETA = b4
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Universal SSL Wrapper
define BLURB
  Stunnel is a program that allows you to encrypt arbitrary TCP connections
  inside SSL (Secure Sockets Layer) available on both Unix and Windows. Stunnel
  can allow you to secure non-SSL aware daemons and protocols (like POP, IMAP,
  LDAP, etc) by having Stunnel provide the encryption, requiring no changes to
  the daemon/www.stunnel.+= https://www.stunnel.org/downloads/unnel.cswstunnel

# Upstream moves versions to an obsolete/ subdir over time, consider it too
MAJOR_VER = $(firstword $(subst ., ,$(VERSION)))https://www.stunnel.org/downloads/archive/$(MAJOR_VER).x/

MASTER_SITES += https://www.stunnel.org/downloads/beta/
DISTFILES += $(DISTNAME)$(BETA).tar.gze/VENDOR_URL   = http://www.stunnel.org

BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibwrap-dev

PACKAGES += CSWstunnel
SPKG_DESC_CSWstunnel = Universal SSL Wrapper
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWstunnel += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWstunnel
RUNTIME_DEP_PKGPCONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --enable-ipv6

REINPLACEMENTS += capath
REINPLACE_MATCH_capath = /etc/ssl/certs
REINPLACE_WITH_capath = $(sysconfdir)/ssl/certs
REINPLACE_FILES_capath += tools/stunnel.conf-sample

PRESERVECONF += $(sysconfdir)/stunnel/stunnel.conf

# stunnel installs several random sample scripts, cgi scripts, and
# a .spec file with unadjusted paths. Leave them out for now and
# only include specific files
EXTRA_MERGE_EXCLUDE_FILES += $(docdir)/stunnel/.*

SSLCERT += $(sysconfdir)/stunnel/stunnel

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswcarbon-cache.xml
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

post-install:
	cd $(DESTDIR)$(sysconfdir)/stunnel && mv stunnel.conf-sample stunnel.conf
	echo "# create /etc/opt/csw/stunnel/stunnel.(key|crt)" > $(DESTDIR)$(sysconfdir)/stunnel/stunnel
	ginstall -D -m 0644 $(WORKDIR)/cswstunnel.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswstunnel.xml
	@$(MAKECOOKIE)

# TODO (release-critical prefixed with !, non release-critical with *)
#
# * postinstall mknod not possible within zone (mknod fails with "not owner")
#   Work around this or provide README.CSW with instructions for chroot
#   --> Why should /dev/zero be required at all? google suggests relation
#       to pthreads .. truss doesn't show /dev/zero usage on Solaris 10
#       Test on Solaris 8 / 9 for comparison
#
NAME = stunnel
VERSION = 4.44
CATEGORIES = net

DESCRIPTION = Universal SSL Wrapper
define BLURB
  Stunnel is a program that allows you to encrypt arbitrary TCP connections
  inside SSL (Secure Sockets Layer) available on both Unix and Windows. Stunnel
  can allow you to secure non-SSL aware daemons and protocols (like POP, IMAP,
  LDAP, etc) by having Stunnel provide the encryption, requiring no changes to
  the daemon's code. 
endef

VENDOR_URL   = http://www.stunnel.org
MASTER_SITES = ftp://ftp.stunnel.org/stunnel/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
DISTFILES   += CSWstunnel.cswstunnel

# Upstream moves versions to an obsolete/ subdir over time, consider it too
MAJOR_VER = $(firstword $(subst ., ,$(VERSION)))
MASTER_SITES += ftp://ftp.stunnel.org/stunnel/obsolete/$(MAJOR_VER).x/

RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWlibwrap1
RUNTIME_DEP_PKGS += CSWlibz1

# Make stunnel.conf-sample.in honor our $localstatedir. Issue description:
# cf. http://marc.info/?l=stunnel-users&m=128035848632004&w=2
# Not merged upstream as ./configure without arguments leads to expansions
# that the config file doesn't understand, e.g. sysconfdir='${prefix}/etc'
PATCHFILES = 0001-Make-stunnel.conf-sample.in-honor-sysconfdir-localst.patch

sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-dh
CONFIGURE_ARGS += --localstatedir=$(localstatedir)

# No test target available
TEST_SCRIPTS =

# tools/Makefile references ssldir, but configure only defines SSLDIR, thus
# we pass ssldir manually as a workaround (according to --with-ssl above).
# Should be reported and fixed upstream. Observed with 4.44.
INSTALL_ARGS = ssldir=$(prefix)

# Expand autoconf vars in our init script and mark it for SMF registration
EXPANDVARS = CSWstunnel.cswstunnel
INITSMF = $(sysconfdir)/init.d/cswstunnel

SAMPLECONF = $(sysconfdir)/stunnel.pem
MIGRATE_FILES = stunnel # migrate the /opt/csw/etc/stunnel sub directory

PROTOTYPE_MODIFIERS = restrict
PROTOTYPE_FILES_restrict = $(localstatedir)/lib/stunnel.*
PROTOTYPE_USER_restrict  = nobody
PROTOTYPE_GROUP_restrict = nobody

EXTRA_PAX_ARGS = -s ',ChangeLog$$,changelog,p'

# Contains a historic reference to the default install locations
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/doc/stunnel/changelog

include gar/category.mk

# 1) Suppress prompts for openssl sample cert generation (-batch)
# 2) Disable creation of /dev/zero (needs root privs, moved to postinstall)
pre-build-modulated:
	perl -pi -e '\
		s|\$$\(openssl\) req|\$$\(openssl\) req -batch|; \
		s|^|#| if (m|/dev/zero|);' \
		$(WORKSRC)/tools/Makefile
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: DOCS=AUTHORS BUGS CREDITS ChangeLog TODO
post-install-modulated: DOCS+= doc/stunnel.*html
post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/CSWstunnel.cswstunnel \
		$(DESTDIR)$(sysconfdir)/init.d/cswstunnel

	# create pidfile directory
	ginstall -d $(DESTDIR)$(localstatedir)/run/stunnel

	# stunnel installs several random sample scripts, cgi scripts, and
	# a .spec file with unadjusted paths. Leave them out for now and
	# only include specific files
	rm -rf $(DOCDEST)/*
	$(foreach D,$(DOCS),cp $(WORKSRC)/$(D) $(DOCDEST);)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)

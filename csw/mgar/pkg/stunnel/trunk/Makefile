# Todo:
# * postinstall mknod not possible within zone (mknod fails with "not owner")
#   Work around this or provide README.CSW with instructions for chroot
#   --> Why should /dev/zero be required at all? google suggests relation
#       to pthreads .. truss doesn't show /dev/zero usage on Solaris 10
#       Test on Solaris 8 / 9 for comparison
GARNAME = stunnel
GARVERSION = 4.33
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
MASTER_SITES = http://www.stunnel.org/download/stunnel/src/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWzlib CSWosslrt CSWtcpwrap

# Make stunnel.conf-sample.in honor $localstatedir adjustments
PATCHFILES = 0001-Make-stunnel.conf-sample.in-honor-sysconfdir-localst.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-dh
CONFIGURE_ARGS += --localstatedir=/var/opt/csw

# No test target available
TEST_SCRIPTS =

sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

INITSMF = $(sysconfdir)/init.d/cswstunnel
SAMPLECONF = $(sysconfdir)/stunnel.pem

PROTOTYPE_MODIFIERS = restrict
PROTOTYPE_FILES_restrict = $(localstatedir)/lib/stunnel.*
PROTOTYPE_USER_restrict  = nobody
PROTOTYPE_GROUP_restrict = nobody

EXTRA_PAX_ARGS = '-s,ChangeLog$$,changelog,p'

include gar/category.mk

# 1) Suppress prompts for openssl sample cert generation (-batch)
# 2) Disable creation of /dev/zero (needs root privs, moved to postinstall)
pre-build-modulated:
	perl -pi -e '\
		s|\$$\(openssl\) req|\$$\(openssl\) req -batch|; \
		s|^|#| if (m|/dev/zero|);' \
		$(WORKSRC)/tools/Makefile
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: DOCS=AUTHORS BUGS CREDITS ChangeLog TODO
post-install-modulated: DOCS+= doc/stunnel.*html
post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/CSWstunnel.cswstunnel \
		$(DESTDIR)$(sysconfdir)/init.d/cswstunnel

	# create pidfile directory
	ginstall -d $(DESTDIR)/var/opt/csw/run/stunnel

	# stunnel installs several random sample scripts, cgi scripts, and
	# a .spec file with unadjusted paths. Leave them out for now and
	# only include specific files
	rm -rf $(DOCDEST)/*
	$(foreach D,$(DOCS),cp $(WORKSRC)/$(D) $(DOCDEST);)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)

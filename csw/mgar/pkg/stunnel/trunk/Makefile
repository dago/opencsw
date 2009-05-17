GARNAME = stunnel
GARVERSION = 4.27
CATEGORIES = net

DESCRIPTION = Universal SSL Wrapper
define BLURB
  Stunnel is a program that allows you to encrypt arbitrary TCP connections
  inside SSL (Secure Sockets Layer) available on both Unix and Windows. Stunnel
  can allow you to secure non-SSL aware daemons and protocols (like POP, IMAP,
  LDAP, etc) by having Stunnel provide the encryption, requiring no changes to
  the daemon's code. 
endef

MASTER_SITES = http://www.stunnel.org/download/stunnel/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWstunnel.postinstall

SPKG_SOURCEURL = http://www.stunnel.org

REQUIRED_PKGS = CSWzlib CSWosslrt CSWtcpwrap

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Make stunnel.conf-sample.in honor $localstatedir adjustments
PATCHFILES = gar-base.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-dh
CONFIGURE_ARGS += --localstatedir=/var/opt/csw

# No test target available
TEST_SCRIPTS =

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
	# create pidfile directory
	@ginstall -d $(DESTDIR)/var/opt/csw/run/stunnel

	# stunnel installs several random sample scripts, cgi scripts, and
	# a .spec file with unadjusted paths. Leave them out for now and
	# only include specific files
	@rm -rf $(DOCDEST)/*
	@$(foreach D,$(DOCS),cp $(WORKSRC)/$(D) $(DOCDEST);)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)

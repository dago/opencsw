GARNAME = openssh
GARVERSION = 5.2
RELEASE = p1
GSSKEX_PATCH_VERSION = $(GARVERSION)$(RELEASE)
GSSKEX_PATCH_DATE = 20081003
CATEGORIES = server

DESCRIPTION = OpenSSH Secure Shell

define BLURB
  OpenSSH is a FREE version of the SSH connectivity tools that technical users 
  of the Internet rely on. Users of telnet, rlogin, and ftp may not realize that 
  their password is transmitted across the Internet unencrypted, but it is. 
  OpenSSH encrypts all traffic (including passwords) to effectively eliminate 
  eavesdropping, connection hijacking, and other attacks. Additionally, OpenSSH 
  provides secure tunneling capabilities and several authentication methods, 
  and supports all SSH protocol versions.
endef

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.uk/computing/patches/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*p\d+).tar.gz

DISTVERSION = $(GARVERSION)$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += i.conf r.conf
DISTFILES += changelog.CSW

DISTFILES += sshd_config
DISTFILES += cswopenssh svc-cswopenssh cswopenssh.xml
DISTFILES += openssh

ifndef LPK
DISTFILES += $(call admfiles,CSWossh,depend checkinstall preinstall postinstall prototype) 
DISTFILES += $(call admfiles,CSWosshclient,depend prototype) 
endif


# Script created to workaround a upgrade bug between 
# package = 4.6,REV=2007.07.30_rev=p1 and later package
DISTFILES += openssh_restart_workaround.sh

# The GSSAPI key exchange patch
PATCHFILES = openssh-$(GSSKEX_PATCH_VERSION)-gsskex-$(GSSKEX_PATCH_DATE).patch

# Prevent TIOCSCTTY from being used to avoid error:
# ioctl(TIOCSCTTY): Invalid argument
PATCHFILES += don_t_use_TIOCSCTTY.patch

# Fix a X11 forwarding bug on machine installed with ipv6 disabled
# see https://bugzilla.mindrot.org/show_bug.cgi?id=1457
PATCHFILES += no_x_forwarding_bug.patch

# documentation files to install (not a gar variable)
DOCFILES = CREDITS ChangeLog ChangeLog.gssapi INSTALL LICENCE OVERVIEW README README.dns 
DOCFILES += README.platform README.privsep README.smartcard README.tun TODO WARNING.RNG    

SPKG_CLASSES = none conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)

TEST_SCRIPTS	=

ifdef LPK
	DISTFILES += $(call admfiles,CSWosshlpk,depend checkinstall preinstall postinstall prototype) 
	DESCRIPTION = OpenSSH Secure Shell with Ldap Public Key support
	MASTER_SITES += http://openssh-lpk.googlecode.com/svn/trunk/patch/contrib/
	PATCHFILES += contrib-openssh-lpk-5.2p1-0.3.9.patch
	CONFIGURE_ARGS += --with-ldap
	DOCFILES += openssh-lpk_openldap.schema openssh-lpk_sun.schema lpk-user-example.txt README.lpk
endif

include gar/category.mk


# we re-run autoconf because of the GSSAPI key exchange patch
pre-configure:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

# adding documentation files
post-install: customize_ssh_config
	ginstall $(WORKDIR_FIRSTMOD)/*.conf $(WORKDIR)/
	ginstall -D $(WORKDIR_FIRSTMOD)/openssh $(PKGROOT)/etc/init.d/openssh
	ginstall -D $(WORKDIR_FIRSTMOD)/sshd_config $(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW
	ginstall -D $(WORKDIR_FIRSTMOD)/openssh_restart_workaround.sh $(PKGROOT)/$(sharedstatedir)/openssh/openssh_restart_workaround.sh

ifdef LPK
	mkdir -p $(PKGROOT)/$(docdir)/openssh_lpk/ 
	cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/openssh_lpk/
	ginstall $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/openssh_lpk/
else
	mkdir -p $(PKGROOT)/$(docdir)/openssh/ 
	cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/openssh/
	ginstall $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/openssh/
	mkdir -p $(PKGROOT)/$(docdir)/openssh_client/
	cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/openssh_client/
	cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/openssh_client/
	ginstall $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/openssh_client/
endif

customize_ssh_config:
	# Correction des chemins
	sed -e 's,/etc/ssh/,/opt/csw/etc/ssh/,g' -e 's,/usr/libexec/,/opt/csw/libexec/,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config"
	sed -e 's,^ *# *UsePAM *.*,UsePAM yes,g' -e 's,^ *# *X11Forwarding *.*,X11Forwarding yes,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config"


SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

#####################################################################
# OpenCSW build recipe for openssh
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

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


PACKAGES = CSWossh CSWosshclient

CATALOGNAME_CSWossh = openssh
SPKG_DESC_CSWossh = OpenSSH Secure Shell server 
REQUIRED_PKGS_CSWossh = CSWosslrt CSWtcpwrap CSWzlib CSWkrb5lib CSWosshclient

CATALOGNAME_CSWosshclient = openssh_client
SPKG_DESC_CSWosshclient = OpenSSH Secure Shell client 
REQUIRED_PKGS_CSWosshclient = CSWosslrt CSWzlib CSWkrb5lib 


###### Upstream and OpenCSW files information #######

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.uk/computing/patches/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*p\d+).tar.gz

DISTVERSION = $(GARVERSION)$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += changelog.CSW

DISTFILES += cswopenssh sshd.smf_wrapper cswopenssh.xml

LICENSE = LICENCE

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

# we're using conf handling class from the cswclassutils package
REQUIRED_PKGS += CSWcswclassutils
SPKG_CLASSES = none cswpreserveconf


##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)

TEST_SCRIPTS	=


## Optional addition to add Ldap Public Key support 
## see http://code.google.com/p/openssh-lpk/

# we always register the lpk related files so checksum 
# is the same with LPK enabled or not
DISTFILES += contrib-openssh-lpk-5.2p1-0.3.9.patch
ifdef LPK
	PACKAGES = CSWosshlpk
	CATALOGNAME_CSWosshlpk = openssh_lpk
	SPKG_DESC_CSWosshlpk = $(SPKG_DESC_CSWossh) with ldap public key support
	REQUIRED_PKGS_CSWosshlpk = $(REQUIRED_PKGS_CSWossh) CSWoldaprt
	MASTER_SITES += http://openssh-lpk.googlecode.com/svn/trunk/patch/contrib/
	PATCHFILES += contrib-openssh-lpk-5.2p1-0.3.9.patch
	CONFIGURE_ARGS += --with-ldap
	DOCFILES += openssh-lpk_openldap.schema openssh-lpk_sun.schema lpk-user-example.txt README.lpk
	
	# we must reset the CSWosshclient description to avoid a bug in the automatic dependancy generation
	SPKG_DESC_CSWosshclient = 
endif


include gar/category.mk


# we re-run autoconf because of the GSSAPI key exchange patch
pre-configure:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

# adding documentation files
post-merge: merge-config-files merge-doc-files

merge-doc-files:
	for DOCDIR in $(foreach _PKG,$(PACKAGES),$(call catalogname,$(_PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$DOCDIR; \
		(cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/$$DOCDIR/); \
		ginstall $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$$DOCDIR/; \
	done
	@$(MAKECOOKIE)

merge-config-files:
	ginstall $(PKGROOT)/$(sysconfdir)/ssh/ssh_config $(PKGROOT)/$(sysconfdir)/ssh/ssh_config.CSW 
	ginstall $(PKGROOT)/$(sysconfdir)/ssh/moduli $(PKGROOT)/$(sysconfdir)/ssh/moduli.CSW 
	# we change some default value in the server config file
	sed -e 's,/etc/ssh/,/opt/csw/etc/ssh/,g' \
		-e 's,/usr/libexec/,/opt/csw/libexec/,g' \
		-e 's,^ *# *UsePAM *.*,UsePAM yes,g' \
	       	-e 's,^ *# *X11Forwarding *.*,X11Forwarding yes,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config" > "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW
	@$(MAKECOOKIE)


SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

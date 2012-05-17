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

NAME = openssh
VERSION = 6.0p1
GSSKEX_PATCH_VERSION = 5.9p1
GSSKEX_PATCH_DATE = 20110920
CATEGORIES = server
GARTYPE = v2

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
RUNTIME_DEP_PKGS_CSWossh = CSWlibssl1-0-0 CSWlibwrap1 CSWlibz1 CSWlibkrb5-3 CSWlibk5crypto3 CSWlibgssapi-krb5-2 CSWlibcom-err3 CSWosshclient

CATALOGNAME_CSWosshclient = openssh_client
SPKG_DESC_CSWosshclient = OpenSSH Secure Shell client 
RUNTIME_DEP_PKGS_CSWosshclient = CSWlibssl1-0-0 CSWlibz1 CSWlibkrb5-3 CSWlibk5crypto3 CSWlibgssapi-krb5-2 CSWlibcom-err3


PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386

PKGFILES_CSWossh = $(sbindir)/.*
PKGFILES_CSWossh += $(docdir)/openssh/.*
PKGFILES_CSWossh += $(mandir)/man5/sshd_config.5
PKGFILES_CSWossh += $(mandir)/man8/sftp-server.8
PKGFILES_CSWossh += $(mandir)/man8/sshd.8
PKGFILES_CSWossh += $(libexecdir)/sftp-server
PKGFILES_CSWossh += $(sysconfdir)/ssh/sshd_config.CSW
PKGFILES_CSWossh += $(sysconfdir)/ssh/moduli.CSW
PKGFILES_CSWossh += $(localstatedir)/empty
PKGFILES_CSWossh += $(sysconfdir)/init.d/cswopenssh
PKGFILES_CSWossh += $(localstatedir)/svc/manifest/network/cswopenssh.xml
PKGFILES_CSWossh += $(prefix)/etc/pkg/CSWossh/cswusergroup

PKGFILES_CSWosshclient = $(bindir)/.*
PKGFILES_CSWosshclient += $(docdir)/openssh_client/.*
PKGFILES_CSWosshclient += $(mandir)/man1/.*
PKGFILES_CSWosshclient += $(mandir)/man5/ssh_config.5
PKGFILES_CSWosshclient += $(mandir)/man8/ssh-keysign.8
PKGFILES_CSWosshclient += $(libexecdir)/ssh-keysign
PKGFILES_CSWosshclient += $(sysconfdir)/ssh/ssh_config.CSW
PKGFILES_CSWosshclient += $(prefix)/etc/ssh/THIS_LOCATION_IS_DEPRECATED

PROTOTYPE_MODIFIERS = setuid
PROTOTYPE_FILES_setuid = $(libexecdir)/ssh-keysign
PROTOTYPE_PERMS_setuid = 4711

PRESERVECONF = $(sysconfdir)/ssh/sshd_config
PRESERVECONF += $(sysconfdir)/ssh/ssh_config
PRESERVECONF += $(sysconfdir)/ssh/moduli
INITSMF = $(sysconfdir)/init.d/cswopenssh
USERGROUP = $(prefix)/etc/pkg/CSWossh/cswusergroup

MIGRATE_FILES_CSWossh = moduli sshd_config
MIGRATE_FILES_CSWossh += ssh_host_dsa_key ssh_host_dsa_key.pub ssh_host_rsa_key ssh_host_rsa_key.pub ssh_host_key ssh_host_key.pub
MIGRATE_FILES_CSWossh += shosts.equiv
MIGRATE_FILES_CSWossh += sshrc
MIGRATE_FILES_CSWosshclient = ssh_config
MIGRATE_FILES_CSWosshclient += ssh_known_hosts ssh_known_hosts2
MIGRATE_FILES_CSWosshclient += ssh_prng_cmds
MIGRATE_SOURCE_DIR = $(prefix)/etc/ssh
MIGRATE_DEST_DIR = $(sysconfdir)/ssh

CHECKPKG_OVERRIDES_CSWosshclient += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssh_client/INSTALL
CHECKPKG_OVERRIDES_CSWossh += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssh/INSTALL
CHECKPKG_OVERRIDES_CSWossh += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswopenssh.xml

CHECKPKG_OVERRIDES_CSWossh += surplus-dependency|CSWosshclient

#  We will not fix this today
CHECKPKG_OVERRIDES_CSWossh += catalogname-does-not-match-pkgname|pkgname=CSWossh|catalogname=openssh|expected-catalogname=ossh
CHECKPKG_OVERRIDES_CSWosshclient += catalogname-does-not-match-pkgname|pkgname=CSWosshclient|catalogname=openssh_client|expected-catalogname=osshclient



###### Upstream and OpenCSW files information #######

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.uk/computing/patches/
UPSTREAM_MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*p\d+).tar.gz

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWossh.checkinstall
DISTFILES += CSWosshlpk.checkinstall
DISTFILES += changelog.CSW
DISTFILES += cswusergroup

DISTFILES += cswopenssh sshd.smf_wrapper cswopenssh.xml

DISTFILES += THIS_LOCATION_IS_DEPRECATED

LICENSE = LICENCE

# The GSSAPI key exchange patch
PATCHFILES = openssh-$(GSSKEX_PATCH_VERSION)-gsskex-all-$(GSSKEX_PATCH_DATE).patch

# Prevent TIOCSCTTY from being used to avoid error:
# ioctl(TIOCSCTTY): Invalid argument
PATCHFILES += don_t_use_TIOCSCTTY.patch

# Fix a X11 forwarding bug on machine installed with ipv6 disabled
# see https://bugzilla.mindrot.org/show_bug.cgi?id=1457
PATCHFILES += no_x_forwarding_bug.patch

# Force openssh to not use /var/adm/lastlog but still prints last log information
# Workaround to fix https://www.opencsw.org/mantis/view.php?id=4494
# Bug filled upstream: https://bugzilla.mindrot.org/show_bug.cgi?id=87
PATCHFILES += 0004-no-lastlog-file.patch

# Rename the pidfile to use cswsshd.pid instead of sshd.pid in order to
# avoid a clash with sun native ssh pid file
# see https://www.opencsw.org/mantis/view.php?id=4398
PATCHFILES += 0005-rename-pidfile.patch

# documentation files to install (not a gar variable)
DOCFILES = CREDITS ChangeLog ChangeLog.gssapi INSTALL LICENCE OVERVIEW README README.dns 
DOCFILES += README.platform README.privsep README.tun TODO WARNING.RNG    

# we're using conf handling class from the cswclassutils package
RUNTIME_DEP_PKGS += CSWcswclassutils



##### Build and installation information #####


# to support shared /opt/csw setup
# see http://wiki.opencsw.org/shared-opt-csw-setup
localstatedir 	= /var$(prefix)
sysconfdir 	= /etc$(prefix)


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-privsep-path=$(localstatedir)/empty

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
	RUNTIME_DEP_PKGS_CSWosshlpk = $(RUNTIME_DEP_PKGS_CSWossh) CSWoldaprt
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

# kr5config returns the -R/opt/csw/lib/ which is considered not valid by checkpkg
# manually fixing this until the bug is fixed (see https://www.opencsw.org/mantis/view.php?id=4384 )
post-configure-modulated:
	cd $(WORKSRC) && perl -pi -e 's,-R/opt/csw/lib/ ,-R/opt/csw/lib ,' Makefile
	@$(MAKECOOKIE)

# adding documentation files
pre-package: merge-config-files merge-doc-files merge-init-files merge-contrib-files merge-special-directories

merge-contrib-files:
	ginstall -D "$(WORKSRC_FIRSTMOD)/contrib/ssh-copy-id" "$(PKGROOT)/$(bindir)/ssh-copy-id"
	ginstall -D "$(WORKSRC_FIRSTMOD)/contrib/ssh-copy-id.1" "$(PKGROOT)/$(mandir)/man1/ssh-copy-id.1"
	chmod -x "$(PKGROOT)/$(mandir)/man1/ssh-copy-id.1"

merge-init-files:
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswopenssh" "$(PKGROOT)/etc/opt/csw/init.d/cswopenssh"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswopenssh.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswopenssh.xml"
	ginstall -D "$(WORKDIR_FIRSTMOD)/sshd.smf_wrapper" "$(PKGROOT)/opt/csw/sbin/sshd.smf_wrapper"

merge-doc-files:
	for DOCDIR in $(foreach _PKG,$(PACKAGES),$(call catalogname,$(_PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$DOCDIR; \
		(cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/$$DOCDIR/); \
		(cd $(PKGROOT)/$(docdir)/$$DOCDIR && chmod -x $(DOCFILES)); \
		ginstall $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$$DOCDIR/; \
	done
	@$(MAKECOOKIE)

merge-config-files:
	# we change some default value in the server config file
	perl -pi -e 's,/etc/ssh/,$(sysconfdir)/ssh/,g; s,/usr/libexec/,/opt/csw/libexec/,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW"
	perl -pi -e 's,^ *# *UsePAM *.*,UsePAM yes,g, s,^ *# *PrintMotd *.*,PrintMotd no,g; s,^ *# *X11Forwarding *.*,X11Forwarding yes,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW" 
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswusergroup" "$(PKGROOT)$(prefix)/etc/pkg/CSWossh/cswusergroup"
	ginstall -D "$(WORKDIR_FIRSTMOD)/THIS_LOCATION_IS_DEPRECATED" "$(PKGROOT)/$(prefix)/etc/ssh/THIS_LOCATION_IS_DEPRECATED"
	@$(MAKECOOKIE)

merge-special-directories:
	ginstall -d $(PKGROOT)$(localstatedir)/empty
	ginstall -d $(PKGROOT)$(sysconfdir)/pkg/CSWossh

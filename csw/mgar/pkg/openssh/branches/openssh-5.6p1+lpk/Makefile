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
VERSION = 5.6p1
GSSKEX_PATCH_VERSION = $(VERSION)
GSSKEX_PATCH_DATE = 20100902
CATEGORIES = server

EXTRA_MODULATORS = LPK
MODULATIONS_LPK = no yes

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

BUILD_DEP_PKGS = CSWkrb5libdev CSWoldapdevel

PACKAGES = CSWossh CSWosshlpk CSWosshclient

CATALOGNAME_CSWossh = openssh
SPKG_DESC_CSWossh = OpenSSH Secure Shell server 
RUNTIME_DEP_PKGS_CSWossh = CSWosslrt CSWtcpwrap CSWzlib CSWkrb5lib CSWosshclient

CATALOGNAME_CSWosshlpk = openssh_lpk
SPKG_DESC_CSWosshlpk = OpenSSH Secure Shell server with ldap public key support
RUNTIME_DEP_PKGS_CSWosshlpk = CSWosslrt CSWtcpwrap CSWzlib CSWkrb5lib CSWoldaprt CSWossh

CATALOGNAME_CSWosshclient = openssh_client
SPKG_DESC_CSWosshclient = OpenSSH Secure Shell client 
RUNTIME_DEP_PKGS_CSWosshclient = CSWosslrt CSWzlib CSWkrb5lib 

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386

PKGFILES_CSWossh = $(sbindir)/sshd-nolpk
PKGFILES_CSWossh += $(sbindir)/sshd.smf_wrapper
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

PKGFILES_CSWosshlpk = $(sbindir)/sshd-lpk
PKGFILES_CSWosshlpk += $(docdir)/openssh_lpk/.*
PKGFILES_CSWosshlpk += $(sysconfdir)/openldap.*

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

# The openssh package installs the server and the client
CHECKPKG_OVERRIDES_CSWossh = surplus-dependency|CSWosshclient

###### Upstream and OpenCSW files information #######

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.uk/computing/patches/

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

# LDAP Public Key Patch, forward port from
#   http://code.google.com/p/openssh-lpk/source/browse/#svn/trunk/patch/contrib
PATCHFILES = 0001-Forward-port-of-contrib-openssh-lpk-5.4p1-0.3.13.pat.patch
PATCHFILES += 0002-Do-not-require-posixAccount.patch

# The GSSAPI key exchange patch
PATCHFILES += openssh-$(GSSKEX_PATCH_VERSION)-gsskex-all-$(GSSKEX_PATCH_DATE).patch

# Prevent TIOCSCTTY from being used to avoid error:
# ioctl(TIOCSCTTY): Invalid argument
PATCHFILES += don_t_use_TIOCSCTTY.patch

# Fix a X11 forwarding bug on machine installed with ipv6 disabled
# see https://bugzilla.mindrot.org/show_bug.cgi?id=1457
PATCHFILES += no_x_forwarding_bug.patch

# documentation files to install (not a gar variable)
DOCFILES = CREDITS ChangeLog ChangeLog.gssapi INSTALL LICENCE OVERVIEW README README.dns 
DOCFILES += README.platform README.privsep README.tun TODO WARNING.RNG    
DOCFILES_LPK = openssh-lpk_openldap.schema openssh-lpk_sun.schema lpk-user-example.txt README.lpk

##### Build and installation information #####


# to support shared /opt/csw setup
# see http://wiki.opencsw.org/shared-opt-csw-setup
localstatedir 	= /var$(prefix)
sysconfdir 	= /etc$(prefix)

# libldap is not self-contained and needs explicit linking against liblber.so
EXTRA_LD_FLAGS-lpk-yes = -L/opt/csw/lib -llber
EXTRA_LD_FLAGS += $(EXTRA_LD_FLAGS-lpk-$(LPK))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-privsep-path=$(localstatedir)/empty

CONFIGURE_ARGS-lpk-yes = --with-ldap
CONFIGURE_ARGS += $(CONFIGURE_ARGS-lpk-$(LPK))

TEST_SCRIPTS	=

MERGE_SCRIPTS_isa-default-lpk-no = copy-all
MERGE_SCRIPTS_isa-default-lpk-yes = copy-only
MERGE_DIRS_isa-default-lpk-yes = $(sbindir)

EXTRA_PAX_ARGS_lpk-no = -s ",\.$(sbindir)/sshd$$,.$(sbindir)/sshd-nolpk,p"
EXTRA_PAX_ARGS_lpk-yes = -s ",\.$(sbindir)/sshd$$,.$(sbindir)/sshd-lpk,p" -s ",.*,,"
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_lpk-$(LPK))

ALTERNATIVES_CSWossh    = nolpk
ALTERNATIVES_CSWosshlpk = lpk
ALTERNATIVE_nolpk = $(sbindir)/sshd sshd $(sbindir)/sshd-nolpk 100
ALTERNATIVE_lpk   = $(sbindir)/sshd sshd $(sbindir)/sshd-lpk 200

CHECKPKG_OVERRIDES_CSWossh += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWosshlpk += surplus-dependency|CSWossh
CHECKPKG_OVERRIDES_CSWosshlpk += surplus-dependency|CSWalternatives

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

post-install-modulated: install-config-files install-doc-files-lpk-$(LPK) install-init-files install-contrib-files install-special-directories

install-contrib-files:
	ginstall -D "$(WORKSRC)/contrib/ssh-copy-id" "$(PKGROOT)/$(bindir)/ssh-copy-id"
	ginstall -D "$(WORKSRC)/contrib/ssh-copy-id.1" "$(PKGROOT)/$(mandir)/man1/ssh-copy-id.1"
	chmod -x "$(PKGROOT)/$(mandir)/man1/ssh-copy-id.1"

install-init-files:
	ginstall -D "$(WORKDIR)/cswopenssh" "$(PKGROOT)/etc/opt/csw/init.d/cswopenssh"
	ginstall -D "$(WORKDIR)/cswopenssh.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswopenssh.xml"
	ginstall -D "$(WORKDIR)/sshd.smf_wrapper" "$(PKGROOT)/opt/csw/sbin/sshd.smf_wrapper"

install-doc-files-lpk-no:
	ginstall -d $(PKGROOT)/$(docdir)/openssh
	(cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/openssh/)
	(cd $(PKGROOT)/$(docdir)/openssh && chmod -x $(DOCFILES))
	ginstall $(WORKDIR)/changelog.CSW $(PKGROOT)/$(docdir)/openssh/

install-doc-files-lpk-yes:
	ginstall -d $(PKGROOT)/$(docdir)/openssh_lpk
	cd $(WORKSRC) && ginstall $(DOCFILES_LPK) $(PKGROOT)/$(docdir)/openssh_lpk/
	ginstall -d $(PKGROOT)$(sysconfdir)/openldap/schema
	ginstall $(WORKSRC)/openssh-lpk_openldap.schema $(PKGROOT)$(sysconfdir)/openldap/schema/openssh-lpk.schema

install-config-files:
	# we change some default value in the server config file
	perl -pi -e 's,/etc/ssh/,$(sysconfdir)/ssh/,g; s,/usr/libexec/,/opt/csw/libexec/,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW"
	perl -pi -e 's,^ *# *UsePAM *.*,UsePAM yes,g, s,^ *# *PrintMotd *.*,PrintMotd no,g; s,^ *# *X11Forwarding *.*,X11Forwarding yes,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW" 
	ginstall -D "$(WORKDIR)/cswusergroup" "$(PKGROOT)$(prefix)/etc/pkg/CSWossh/cswusergroup"
	ginstall -D "$(WORKDIR)/THIS_LOCATION_IS_DEPRECATED" "$(PKGROOT)/$(prefix)/etc/ssh/THIS_LOCATION_IS_DEPRECATED"

install-special-directories:
	ginstall -d $(PKGROOT)$(localstatedir)/empty
	ginstall -d $(PKGROOT)$(sysconfdir)/pkg/CSWossh

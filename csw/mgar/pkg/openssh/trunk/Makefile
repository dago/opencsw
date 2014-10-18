#####################################################################
# OpenCSW build recipe for openssh
#
# Author: Yann Rouillard <yann@pleiades.fr.eu.org>
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = openssh
VERSION = 6.7p1
GSSKEX_PATCH_VERSION = 6.7p1
GSSKEX_PATCH_DATE = 20140907
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
endpenssh CSWopenssh-client

CATALOGNAME_CSWopenssh = openssh
SPKG_DESC_CSWopenssh = OpenSSH Secure Shell server 
BUILD_DEP_PKGS = CSWautoconf CSWlibssl-dev CSWlibz-dev
RUNTIME_DEP_PKGS_CSWopenssh += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWopenssh += CSWlibz1
RUNTIME_DEP_PKGS_CSWopenssh += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWopenssh += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWopenssh += CSWopenssh-client

# Linking on sparc gives an additional dependency
# probably because of the current bug with Solaris 10
# sparc linker (see http://lists.opencsw.org/pipermail/maintainers/2013-November/018780.html)
RUNTIME_DEP_PKGS_CSWopenssh += $(RUNTIME_DEP_PKGS_CSWopenssh_$(GARCH))
RUNTIME_DEP_PKGS_CSWopenssh_sparc += CSWlibintl8

OBSOLETED_BY_CSWopenssh = CSWossh

CATALOGNAME_CSWopenssh-client = openssh_client
SPKG_DESC_CSWopenssh-client = OpenSSH Secure Shell client 
RUNTIME_DEP_PKGS_CSWopenssh-client += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWopenssh-client += CSWlibz1
RUNTIME_DEP_PKGS_CSWopenssh-client += CSWlibkrb5-3

# Linking on sparc gives an additional dependency
# probably because of the current bug with Solaris 10
# sparc linker (see http://lists.opencsw.org/pipermail/maintainers/2013-November/018780.html)
RUNTIME_DEP_PKGS_CSWopenssh-client += $(RUNTIME_DEP_PKGS_CSWopenssh-client_$(GARCH))
RUNTIME_DEP_PKGS_CSWopenssh-client_sparc += CSWlibintl8

OBSOLETED_BY_CSWopenssh-client = CSWosshclient

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PKGFILES_CSWopenssh = $(sbindir)/.*
PKGFILES_CSWopenssh += $(docdir)/openssh/.*
PKGFILES_CSWopenssh += $(mandir)/man5/sshd_config.5
PKGFILES_CSWopenssh += $(mandir)/man8/sftp-server.8
PKGFILES_CSWopenssh += $(mandir)/man8/sshd.8
PKGFILES_CSWopenssh += $(libexecdir)/sftp-server
PKGFILES_CSWopenssh += $(sysconfdir)/ssh/sshd_config.CSW
PKGFILES_CSWopenssh += $(sysconfdir)/ssh/moduli.CSW
PKGFILES_CSWopenssh += $(localstatedir)/empty
PKGFILES_CSWopenssh += $(sysconfdir)/init.d/cswopenssh
PKGFILES_CSWopenssh += $(localstatedir)/svc/manifest/network/cswopenssh.xml
PKGFILES_CSWopenssh += $(prefix)/etc/pkg/CSWopenssh/cswusergroup

PKGFILES_CSWopenssh-client = $(bindir)/.*
PKGFILES_CSWopenssh-client += $(docdir)/openssh_client/.*
PKGFILES_CSWopenssh-client += $(mandir)/man1/.*
PKGFILES_CSWopenssh-client += $(mandir)/man5/ssh_config.5
PKGFILES_CSWopenssh-client += $(mandir)/man8/ssh-keysign.8
PKGFILES_CSWopenssh-client += $(libexecdir)/ssh-keysign
PKGFILES_CSWopenssh-client += $(sysconfdir)/ssh/ssh_config.CSW
PKGFILES_CSWopenssh-CSW
PKGFILES_CSWosshclient += $(prefix)/etc/ssh/THIS_LOCATION_IS_DEPRECATED

PROTOTYPE_MODIFIERS = setuid
PROTOTYPE_FILES_setuid = $(libexecdir)/ssh-keysign
PROTOTYPE_PERMS_setuid = 4711

PRESERVECONF = $(sysconfdir)/ssh/sshd_config
PRESERVECONF += $(sysconfdir)/ssh/ssh_config
PRESERVECONF += $(sysconfdir)/ssh/moduli
INITSMF = $(sysconfdir)/init.d/cswopenssh
USERGROUP = $(penssh/cswusergroup

MIGRATE_FILES_CSWopenssh = moduli sshd_config
MIGRATE_FILES_CSWopeng
MIGRATE_FILES_CSWossh += ssh_host_dsa_key ssh_host_dsa_key.pub ssh_host_rsa_key ssh_host_rsa_key.pub ssh_host_key ssh_host_key.pupenssh += shosts.equiv
MIGRATE_FILES_CSWopenssh += sshrc
MIGRATE_FILES_CSWopenssh-client = ssh_config
MIGRATE_FILES_CSWopenssh-client += ssh_known_hosts ssh_known_hosts2
MIGRATE_FILES_CSWopenssh-IGRATE_FILES_CSWosshclient += ssh_prng_cmds
MIGRATE_SOURCE_DIR = $(prefix)/etc/ssh
MIGRATE_DEST_DIR = $(sysconfdir)/ssh

CHEpenCKP-KG_OVERRIDES_CSWosshclient += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssh_client/INSTALL
CHEpenssh += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openssh/INSTALL
CHECKPKG_OVERRIDES_CSWopenCKPKG_OVERRIDES_CSWossh += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/netwlogname=osshclient



###### Upstream and OpenCSW files information #######

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.u http://www.mindrot.org/openssh_snap/
UPSTREAM_nformation #######

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTVERSION).CSWopenssh.cswreleasenotes
DISTFILES += CSWopenssh_client.cswreleasenotesLES += changelog.CSW
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
PATCHFILES += 0005-renaThe regress/Makefile uses "id -un" to retrieve the id of the current user
# but that command doesn't work on Solaris, this patch fixes that issue
PATCHFILES += fix-user-id-retrieval-for-solaris 0005-rena Disable unittest fuzz ed25519 sig as it doesn't work correctly under Solaris
#  see: https://bugzilla.mindrot.org/show_bug.cgi?id=2271
PATCHFILES += disable-unittest-fuzz-ed25519-sig 0005-r# Same thing for ed25519 key test, see: https://bugzilla.mindrot.org/show_bug.cgi?id=2297
PATCHFILES += remote-unittest-key-ed25519 0005-rename-pidfile.patch

# documentation files to install (not a gar variable)
DOCFILES = CREDITS ChangeLog ChangeLog.gssapi INSTALL LICENCE OVERVIEW README README.dns 
DOCFILES += README.platform README.privTODO WARNING.RNG    

# we're using conf handling class from the cswclassutils package
RUNTIME_DEP_PKGS += CSWcswclassutils



##### Build and installation 	= /etc$(prefix)


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-privsep-path=$(localstatedir)/empty

# We don't want to use lazy load because of
# the chroot usage by sshd
EXTRA_LD_OPTIONS = TARGET	= testsloshclient = 
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
pre-package: merge-config-files merge-doc-files merge-init-files merge-contrib-files merge-	@$(MAKECOOKIE)-special-directories

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
		(cd $(PKGROOT)/$(docdir)/$$DOCDIR && chmod cdir)one
	@$(MAKECOOKIE)

merge-config-files:
	# we change some default value in the server config file
	perl -pi -e 's,/etc/ssh/,$(sysconfdir)/ssh/,g; s,/usr/libexec/,/opt/csw/libexec/,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW"
	perl -pi -e 's,^ *# *UsePAM *.*,UsePAM yes,g, s,^ *# *PrintMotd *.*,PrintMotd no,g; s,^ *# *X11Forwarding *.*,X11Forwarding yes,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW" 
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswusergroup" "$(PKGROOT)$(penprefix)/etc/pkg/CSWossh/cswusergroup"
	ginstall -D "$(WORKDIR_FIRSTMOD)/THIS_LOCATION_IS_DEPRECATED" "$(PKGROOT)/$(prefix)/etc/ssh/THIS_LOCAED"
	@$(MAKECOOKIE)

merge-special-directories:
	ginstall -d $(PKGROOT)$(localstatedir)/empty
	ginstall -d $(PKGROOT)$(penssh

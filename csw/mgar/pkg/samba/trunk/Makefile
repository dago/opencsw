#Todo stuff
# There are lots of files and libs which are part of samba 3 package too. There should be removed from packinging
# See http://sources.debian.net/src/samba4/4.0.3%2Bdfsg1-0.1/debian/rules
# All remaining libs are need to be split off. See debian package too.

NAME = samba
VERSION = 4.0.6
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
endef

MASTER_SITES = http://samba.org/samba/ftp/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswsamba
DISTFILES += cswwinbind
EXPANDVARS += cswsamba
EXPANDVARS += cswwinbind
EXPANDVARS += smb.conf

# From http://www.reallylinux.com/docs/smb.conf
DISTFILES += smb.conf

# This is taken from the old Samba package
DISTFILESPATCHFILES += 0001-fix-xml.patchE#From https://bugzilla.samba.org/show_bug.cgi?id=7588
PATCHFILES += nss_winbind.patch
PATCHFILES += smbd_patch_for_setgroups.patch

BUILD_DEP_PKGS += CSWlibtalloc-dev
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWsamba4
SPKG_DESC_CSWsamba4 = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibfam0
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba4 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibwbclient0

# Just docs override for now
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/lmhosts.5
CHECKPKG_4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/smb.conf.5
CHECKPKG_4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/cnmbd.8
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csmbd.8
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/ctdbbackup.8
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/cidmap_tdb2.8
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/cnet.8
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share= samba_doc_stub

PA4-client
SPKG_DESC_CSWsamba4-client = Client binaries for samba4
SMB_CLIENT_TOOLS = cifsdd smbclient4 nmblookup4
PKGFILES_CSWsamba4-client += $(foreach T,$(SMB_CLIENT_TOOLS),$(call baseisadirs,$(bindir),$T) $(mandir)/man1/$T\.1)
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibtdb1


# Just docs, override for now
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-client += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/smbclient.1

#PACKAGES += CSWsambadoc
SPKG_DESC_CSWsambadoc = Samba documentation
ARCHALL_CSWsambadoc = 1

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call pkgfiles_lib,libnetapi.so.0)
SPKG_DESC_CSWlibnetapi0 += Samba client librarrary, libtdb.so.1

PACKAGES += CSWlibnss-winbind1
PKGFILES_CSWlibnss-winbind1 += $(call pkgfiles_lib,libnss_winbind.so.1)
SPKG_DESC_CSWlibnss-winbind1 += Winbind nss libary,libnss_winbind.so.1

PA4-dev
SPKG_DESC_CSWsamba4-dev = Development files for Samba, libsmbclient.so.0
PKGFILES_CSWsamba4-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsmbclient0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibnetapi0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsmbsharemodes0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWsamba


PACKAGES += CSWsamba4-swat
SPKG_DESC_CSWsamba4-swat = Web-based samba administration tools
PKGFILES_CSWsamba4-swat += $(call baseisadirs,$(sbindir),swat)
PKGFILES_CSWsamba4-swat += $(mandir)/.*/swat\.*
PKGFILES_CSWsamba4-swat += $(sharedstatedir)/samba/swat/.*
PKGFILES_CSWsamba4-swat += $(prefix)/swat/.*
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba4-swat += CSWlibtdb1

# Just docs, override for now
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/cswByExample/ix01.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/cswByExample/appendix.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/cswByExample/upgrades.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/cswByExample/secure.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/cswByExample/nw4migration.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/cswDevelopers-Guide/pwencrypt.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/classicalprinting.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/bugreport.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/VFS.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/compiling.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/NetworkBrowsing.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/domain-member.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/SWAT.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/locking.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/hx01.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/samba-pdc.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/install.html
CHECKPKG_4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/diagnosis.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/FastStart.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/pam.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/winbind.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/AccessControls.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/swat.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/lmhosts.5.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/nmbd.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/idmap_tdb2.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/smb.conf.5.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/winbindd.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/smbd.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/net.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/tdbbackup.8.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/manpages/smbclient.1.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/export/home|root/opt/csw/swat/help/Samba3-HOWTO/msdfs.html
CHECKPKG_4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/cswByExample/ix01.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/cswByExample/appendix.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/cswByExample/upgrades.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/cswByExample/happy.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/VFS.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/CUPS-printing.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/SWAT.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/ix01.html
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/FastStart.html
CHECKPKG_4OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/ch-ldap-tls.html

PACKAGES += CSWsamba4-winbind
SPKG_DESC_CSWsamba4-winbind = Tools to authenticate users from active directory using winbind
PKGFILES_CSWsamba4-winbind += $(call baseisadirs,$(libdir),security/pam_winbind\.so)
PKGFILES_CSWsamba4-winbind += $(sharedstatedir)/locale/.*/pam_winbind\.mo
PKGFILES_CSWsamba4-winbind += $(mandir)/man5/pam_winbind\.conf\.5
PKGFILES_CSWsamba4
PKGFILES_CSWsamba-winbind += $(mandir)/man7/winbind_krb5_locator\.74-winbind += $(mandir)/man8/pam_winbind\.8
PKGFILES_CSWsamba4
PKGFILES_CSWsamba-winbind += $(call baseisadirs,$(sbindir),winbindd)4-winbind += $(mandir)/man8/winbindd\.8
PKGFILES_CSWsamba4-winbind += /etc/opt/csw/init.d/cswwinbind
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibnss-winbind1

# Just docs, override for now
CHECKPKG_OVERRIDES_CSWsamba4-winbindOVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/cwinbindd.8
CHECKPKG_OVERRIDES_CSWsamba4OVERRIDES_CSWsamba-winbind += surplus-dependency|CSWlibnss-winbind1
rt -lintl -lsec
EXTRA_LDFLAGS = -lrt -lintl -lsec

# At the moment there are errors about python headers missing on 64 bit
#BUILD64 = 1
#ISAEXEC = 1

GARCOMPILER = GNU64 = 1
ISAEXEC = 1

SMBLOCKDIR = $(localstatedir)/samba/locks
SMBLOGDIR = $(localstatedir)/samba/log
SMBPRIVATEDIR = $(sysconfdir)/samba/private
SMBCONFIGDIR = $(SMBPRIVATELIB = $(libFIGDIR = $(sCONFIGURE_ARGS += $(DIRPATHS)
#Remove exec_prefix from DIRPATHS:
NODIRPATHS += --exec_prefix=/opt/csw 

#CONFIGURE_ARGS += --enable-shared=yes
#enable-shared=yes
CONFIGURE_ARGS += --enable-static=no
#CONFIGURE_ARGS += --enable-socket-wrapper
#CONFIGURE_ARGS += --enable-nss-wrapper
CONFIGURE_ARGS += --with-acl-support
CONFIGURE_ARGS += --with-aio-support
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS CONFIGURE_ARGS += --with-static-modules=vfs_solarisacl
es=vfs_solarisacl
CONFIGURE_ARGS += --with-shared-modules=vfs_zfsacl,vfs_prealloc,vfs_cacheprime,vfs_commit,idmap_ldap,idmap_tdb2,idmap_rid,idmap_ad,idma#p_hash,idmap_adex
CONFIGUshared-modules=odules=vfs_zfsacl,vfs_prealloc,vfs_cacheprime,vfs_commit,idmap_ldap,idmap_tdb2,idmap_rid,idmap_ad,idma#p_hash,idmap_adex
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-ads
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS +=#CONFIGURE_ARGS += --with-dnsupdate=noith-krb5=$(prefix)
CONFIGURE_ARGS += --with-privaLIBir=$(SMBPRIVATEDIR)
CONFIGURE_ARGS += --with-configdir=$(SMBCONFIGDIR)
CONFIGURE_ARGS += --with-lockdir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-statedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-cachedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-pid# to stay with the one build with samba 3 build this one private
CONFIGURE_ARGS += --private-libraries=smbclient
CONFIGURE_ARGS += --with-privatelibdir=$(SMBPRIVATELIBiddir=$(SMBLOCKDIR)

CONFIGURE_ARGS += --with-logfilebase=$(SMBLOGDI += --enable-cupsGS-$(MEMORYMODEL))

# Can't use fdatasync atm do t#CONFIGURE_ARGS += ac_cv_lib_rt_fdatasync=no
#CONFIGURE_ARGS += ac_cv_have_fdatasync_decl=no
#CONFIGURE_ARGS += ac_cv_lib_ext_rt_fdatasync=no




TEST_TARGET = test

# Tests need root
SKIPTEST ?= 1

# Some filenames contain a "=" which totally confuses the svr4 packaging system
# These are:
#   /opt/csw/share/setup/cn=replicator.ldif
#   /opt/csw/share/setup/cn=samba-admin.ldif
#   /opt/csw/share/setup/cn=samba.ldif

EXTRA_PAX_ARGS += -s "/=/-/g"

INITSMF += /etc/opt/csw/init.d/cswsamba
INITSMF += /etc/opt/csw/init.d/cswwinbind

PRESERVECONF += $(sysconfdir)/samba/smb.conf

include gar/category.mk/source3/configure

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswsamba $(DESTDIR)/etc/opt/csw/init.d/cswsamba
	ginstall $(WORKDIR)/cswwinbind $(DESTDIR)/etc/opt/csw/init.d/cswwinbind
	ginstall -d $(DESTDIR)/etc/opt/csw/samba
	ginstall $(WORKDIR)/smb.conf $(DESTDIR)/etc/opt/cs#w/samba/smb.conf
	ginstall $(WORKSRC)/nsswitch/libnss_winbind.so $(DESTDIR)/$(libdir)/li	@$(MAKECOOKIE)

# python buildtools/bin/waf -v build 

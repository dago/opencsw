NAME = samba
VERSION = 4.0.9
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
endef

MASTER_SITES = http://samba.org/samba/ftp/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswsamba
DISTFI# From http://www.reallylinux.com/docs/smb.conf
DISTFILES += smb.conf
# This is taken from the old Samba package
DISTFILES += cswkrb5.conf
EXPANDVARS += cswsamba
EXPANDVARS += cswwinbind
EXPANDVARS += smb.conf

GARCOMPILER = GNU
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
BUILD_DEP_PKGS += CSWlibtalloc-dev

PATCHFILES += 0001-fix-xml.patch
# From https://bugzilla.samba.org/show_bug.cgi?id=7588
PATCHFILES += nss_winbind.patch
PATCHFILES += smbd_patch_for_setgroups.patch
# From https://bugzilla.samba.org/show_bug.cgi?id=10112
PATCHFILES += 0003-Use-R-linker-flag-instead-of-rpath.patch

# Filesystem layout4 = 1
ISAEXEC = 1

SMBLOCKDIR = $(localstatedir)/samba/locks
SMBLOGDIR = $(localstatedir)/samba/log
SMBPRIVATEDIR = $(sysconfdir)/samba/private
SMBCONFIGDIR = $(SMBPRIVATELIB = $(libFIGDIR = $4

# List of modules and libraries
SMB_VFS_MODULES_A = vfs_audit,vfs_extd_audit,vfs_full_audit,vfs_fake_perms,vfs_fake_acls
SMB_VFS_MODULES_B = vfs_recycle,vfs_netatalk,vfs_readonly,vfs_cap,vfs_expand_msdfs,vfs_shadow_copy,vfs_shadow_copy2
SMB_VFS_MODULES_C = vfs_xattr_tdb,vfs_posix_eadb,vfs_solarisacl,vfs_zfsacl,vfs_catia
SMB_VFS_MODULES_D = vfs_streams_xattr,vfs_streams_depot,vfs_cacheprime,vfs_prealloc,vfs_commit,vfs_notify_fam
SMB_VFS_MODULES_E = vfs_readahead,vfs_aio_pthread,vfs_aio_posix,vfs_preopen,vfs_syncops
SMB_VFS_MODULES_F = vfs_acl_xattr,vfs_acl_tdb,vfs_smb_traffic_analyzer,vfs_dirsort,vfs_scannedonly,vfs_crossrename
SMB_VFS_MODULES_G = vfs_time_audit,vfs_media_harmony,vfs_dfs_samba4
SMB_VFS_MODULES = $(SMB_VFS_MODULES_A),$(SMB_VFS_MODULES_B),$(SMB_VFS_MODULES_C),$(SMB_VFS_MODULES_D),$(SMB_VFS_MODULES_E),$(SMB_VFS_MODULES_F),$(SMB_VFS_MODULES_G)
SMB_IDMAP_MODULES = idmap_ad,idmap_adex,idmap_autorid,idmap_hash,idmap_ldap,idmap_nss,idmap_rid,idmap_tdb,idmap_tdb2
SMB_PDB_MODULES =  pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
SMB_AUTH_MODULES = auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
SMB_MODULES = $(SMB_VFS_MODULES),$(SMB_IDMAP_MODULES),$(SMB_PDB_MODULES),$(SMB_AUTH_MODULES)

# Main package CSWsamba4
PACKAGES += CSWsamba4
SPKG_DESC_CSWsamba4 = $(DESCRIPTION)
# OBSOLETED_BY_CSWsamba4 += CSWsamba
SMB_BINS  = eventlogadm gentest locktest masktest ndrdump net ntlm_auth pdbedit pidl
SMB_BINS += profiles samba-tool smbcontrol smbstatus smbtorture testparm
SMB_SBINS = smbd nmbd samba samba_dnsupdate samba_kcc samba_spnupdate samba_upgradedns
SMB_MANPAGES  = findsmb\.1 log2pcap\.1 vfstest\.1
SMB_MANPAGES += lmhosts\.5 smb.conf\.5 smbpasswd\.5 smbgetrc\.5
SMB_MANPAGES += samba\.7
SMB_MANPAGES += net\.8 pdbedit\.8 eventlogadm\.8 smbd\.8 nmbd\.8 samba\.8 samba-tool\.8 smbpasswd\.8 smbspool\.8 smbta-util\.8
SMB_MANPAGES += tdbbackup\.8 tdbdump\.8 tdbrestore\.8 tdbtool\.8
PKGFILES_CSWsamba4 += $(call baseisadirs,$(sysconfdir),init\.d/cswsamba4)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(sysconfdir),openldap/schema/samba\.schema)
PKGFILES_CSWsamba4 += $(foreach B,$(SMB_BINS),$(call baseisadirs,$(bindir),$B))
PKGFILES_CSWsamba4 += $(foreach B,$(SMB_BINS),$(call baseisadirs,$(mandir),man1/$B\.1))
PKGFILES_CSWsamba4 += $(foreach B,$(SMB_SBINS),$(call baseisadirs,$(sbindir),$B))
PKGFILES_CSWsamba4 += $(call baseisadirs,$(sharedstatedir),codepages/.*)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(sharedstatedir),setup/.*)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(sharedstatedir),perl5/.*)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(SMBCONFIGDIR),smb.conf.CSW)
PKGFILES_CSWsamba4 += $(foreach M,$(SMB_MANPAGES),$(call baseisadirs,$(mandir),man./$M))
PKGFILES_CSWsamba4 += $(call baseisadirs,$(mandir),man8/vfs_.*)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(mandir),man8/idmap_.*)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(libdir),mit_samba\.so)
PKGFILES_CSWsamba4 += $(call baseisadirs,$(libdir),security/pam_smbpass\.so)
RUNTIME_DEP_PKGS_CSWsamba4 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWsamba4 += CSWperl
RUNTIME_DEP_PKGS_CSWsamba4 += CSWlibgcc-s1

# Package with clients, finished
PACKAGES += CSWsamba4-client
SPKG_DESC_CSWsamba4-client = Samba 4 clients
# OBSOLETED_BY_CSWsamba4-client += CSWsamba-client
SMB_CLIENT_BINS  = cifsdd dbwrap_tool nmblookup nmblookup4 oLschema2ldif regdiff regpatch regshell regtree rpcclient
SMB_CLIENT_BINS += samba-regedit sharesec smbcacls smbclient smbclient4 smbcquotas smbget smbpasswd smbprint
SMB_CLIENT_BINS += smbspool smbta-util smbtar smbtree tdbbackup tdbdump tdbrestore tdbtool
SMB_CLIENT_BINS += ldbadd ldbdel ldbedit ldbmodify ldbrename ldbsearch
PKGFILES_CSWsamba4-client += $(foreach C,$(SMB_CLIENT_BINS),$(call baseisadirs,$(bindir),$C))
PKGFILES_CSWsamba4-client += $(foreach C,$(SMB_CLIENT_BINS),$(call baseisadirs,$(mandir),man1/$C\.1))
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4-client += CSWlibreadline6

# Development packagebnss_winbind.so.1

PA4-dev
SPKG_DESC_CSWsamba4-dev = Development files for Samba 4
# OBSOLETED_BY_CSWsamba4-dev += CSWsamba-dev
PKGFILES_CSWsamba4-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWsamba4-dev += $(libdir)/lib.*\.so)
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWsamba4
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibdcerpc-server0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibdcerpc-atsvc0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibregistry0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibtorture0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibndr-nbt0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsamba-util0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsmbclient-raw0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsamba-policy0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsamdb0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWsamba4-winbind
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibndr-krb5pac0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibndr0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibpdb0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsmbconf0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibdcerpc-samr0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibnetapi0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsamba-credentials0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibdcerpc0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsmbldap0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibgensec0
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsamba4-dev += CSWlibdcerpc-binding0

# Package CSWsamba4 libraries
PACKAGES += CSWsamba4-libs
SPKG_DESC_CSWsamba4-libs = Samba 4 libraries
SMB_LIBS  = libdcerpc-atsvc.so.0 libdcerpc-binding.so.0 libdcerpc-samr.so.0 libdcerpc-server.so.0 libdcerpc.so.0 libgensec.so.0
SMB_LIBS += libndr-krb5pac.so.0 libndr-nbt.so.0 libndr-standard.so.0 libndr.so.0 libnetapi.so.0 libpdb.so.0
SMB_LIBS += libregistry.so.0 libsamba-credentials.so.0 libsamba-hostconfig.so.0 libsamba-policy.so.0
SMB_LIBS += libsamba-util.so.0 libsamdb.so.0 libsmbclient-raw.so.0 libsmbconf.so.0 libsmbldap.so.0 libtevent-util.so.0
SMB_LIBS += libtorture.so.0
# PKGFILES_CSWsamba4-libs += $(foreach L,$(SMB_LIBS),$(call pkgfiles_lib,$L))
PKGFILES_CSWsamba4-libs += $(SMBPRIVATELIB)/.*
PKGFILES_CSWsamba4-libs += $(mandir)/man7/libsmbclient.7
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibfam0
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba4-libs += CSWlibgcc-s1

PACKAGES += CSWlibdcerpc-atsvc0
PKGFILES_CSWlibdcerpc-atsvc0 += $(call baseisadirs,$(libdir),libdcerpc-atsvc\.so\.0\.0\.1)
PKGFILES_CSWlibdcerpc-atsvc0 += $(call baseisadirs,$(libdir),libdcerpc-atsvc\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibdcerpc-atsvc0 += $(DESCRIPTION), libdcerpc-atsvc.so.0
RUNTIME_DEP_PKGS_CSWlibdcerpc-atsvc0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibdcerpc-atsvc0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdcerpc-atsvc0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdcerpc-atsvc0 += CSWlibsamba-util0

PACKAGES += CSWlibdcerpc-binding0
PKGFILES_CSWlibdcerpc-binding0 += $(call baseisadirs,$(libdir),libdcerpc-binding\.so\.0\.0\.1)
PKGFILES_CSWlibdcerpc-binding0 += $(call baseisadirs,$(libdir),libdcerpc-binding\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibdcerpc-binding0 += $(DESCRIPTION), libdcerpc-binding.so.0
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdcerpc-binding0 += CSWlibsamba-util0

PACKAGES += CSWlibdcerpc-samr0
PKGFILES_CSWlibdcerpc-samr0 += $(call baseisadirs,$(libdir),libdcerpc-samr\.so\.0\.0\.1)
PKGFILES_CSWlibdcerpc-samr0 += $(call baseisadirs,$(libdir),libdcerpc-samr\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibdcerpc-samr0 += $(DESCRIPTION), libdcerpc-samr.so.0
RUNTIME_DEP_PKGS_CSWlibdcerpc-samr0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibdcerpc-samr0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdcerpc-samr0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdcerpc-samr0 += CSWlibsamba-util0

PACKAGES += CSWlibdcerpc-server0
PKGFILES_CSWlibdcerpc-server0 += $(call baseisadirs,$(libdir),libdcerpc-server\.so\.0\.0\.1)
PKGFILES_CSWlibdcerpc-server0 += $(call baseisadirs,$(libdir),libdcerpc-server\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibdcerpc-server0 += $(DESCRIPTION), libdcerpc-server.so.0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibsamba-credentials0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibdcerpc0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibregistry0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibsamdb0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibgensec0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibdcerpc-binding0
RUNTIME_DEP_PKGS_CSWlibdcerpc-server0 += CSWlibsamba-util0

PACKAGES += CSWlibdcerpc0
PKGFILES_CSWlibdcerpc0 += $(call baseisadirs,$(libdir),libdcerpc\.so\.0\.0\.1)
PKGFILES_CSWlibdcerpc0 += $(call baseisadirs,$(libdir),libdcerpc\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibdcerpc0 += $(DESCRIPTION), libdcerpc.so.0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibsamba-credentials0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibsmbclient-raw0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibgensec0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibdcerpc-binding0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibndr-nbt0
RUNTIME_DEP_PKGS_CSWlibdcerpc0 += CSWlibsamba-util0

PACKAGES += CSWlibgensec0
PKGFILES_CSWlibgensec0 += $(call baseisadirs,$(libdir),libgensec\.so\.0\.0\.1)
PKGFILES_CSWlibgensec0 += $(call baseisadirs,$(libdir),libgensec\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgensec0 += $(DESCRIPTION), libgensec.so.0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibsamba-credentials0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibsamdb0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgensec0 += CSWlibsamba-util0

PACKAGES += CSWlibndr-krb5pac0
PKGFILES_CSWlibndr-krb5pac0 += $(call baseisadirs,$(libdir),libndr-krb5pac\.so\.0\.0\.1)
PKGFILES_CSWlibndr-krb5pac0 += $(call baseisadirs,$(libdir),libndr-krb5pac\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibndr-krb5pac0 += $(DESCRIPTION), libndr-krb5pac.so.0
RUNTIME_DEP_PKGS_CSWlibndr-krb5pac0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibndr-krb5pac0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibndr-krb5pac0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibndr-krb5pac0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibndr-krb5pac0 += CSWlibsamba-util0

PACKAGES += CSWlibndr-nbt0
PKGFILES_CSWlibndr-nbt0 += $(call baseisadirs,$(libdir),libndr-nbt\.so\.0\.0\.1)
PKGFILES_CSWlibndr-nbt0 += $(call baseisadirs,$(libdir),libndr-nbt\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibndr-nbt0 += $(DESCRIPTION), libndr-nbt.so.0
RUNTIME_DEP_PKGS_CSWlibndr-nbt0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibndr-nbt0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibndr-nbt0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibndr-nbt0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibndr-nbt0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibndr-nbt0 += CSWlibsamba-util0

PACKAGES += CSWlibndr-standard0
PKGFILES_CSWlibndr-standard0 += $(call baseisadirs,$(libdir),libndr-standard\.so\.0\.0\.1)
PKGFILES_CSWlibndr-standard0 += $(call baseisadirs,$(libdir),libndr-standard\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibndr-standard0 += $(DESCRIPTION), libndr-standard.so.0

PACKAGES += CSWlibndr0
PKGFILES_CSWlibndr0 += $(call baseisadirs,$(libdir),libndr\.so\.0\.0\.1)
PKGFILES_CSWlibndr0 += $(call baseisadirs,$(libdir),libndr\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibndr0 += $(DESCRIPTION), libndr.so.0
RUNTIME_DEP_PKGS_CSWlibndr0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibndr0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibndr0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibndr0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibndr0 += CSWlibsamba-util0

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call baseisadirs,$(libdir),libnetapi\.so\.0)
PKGFILES_CSWlibnetapi0 += $(call baseisadirs,$(libdir),libnetapi\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibnetapi0 += $(DESCRIPTION), libnetapi.so.0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibpdb0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibsmbconf0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibsamba-util0

PACKAGES += CSWlibpdb0
PKGFILES_CSWlibpdb0 += $(call baseisadirs,$(libdir),libpdb\.so\.0)
PKGFILES_CSWlibpdb0 += $(call baseisadirs,$(libdir),libpdb\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpdb0 += $(DESCRIPTION), libpdb.so.0
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibsmbconf0
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibsamdb0
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWlibpdb0 += CSWlibsamba-util0

PACKAGES += CSWlibregistry0
PKGFILES_CSWlibregistry0 += $(call baseisadirs,$(libdir),libregistry\.so\.0\.0\.1)
PKGFILES_CSWlibregistry0 += $(call baseisadirs,$(libdir),libregistry\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibregistry0 += $(DESCRIPTION), libregistry.so.0
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibdcerpc0
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibregistry0 += CSWlibsamba-util0

PACKAGES += CSWlibsamba-credentials0
PKGFILES_CSWlibsamba-credentials0 += $(call baseisadirs,$(libdir),libsamba-credentials\.so\.0\.0\.1)
PKGFILES_CSWlibsamba-credentials0 += $(call baseisadirs,$(libdir),libsamba-credentials\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsamba-credentials0 += $(DESCRIPTION), libsamba-credentials.so.0
RUNTIME_DEP_PKGS_CSWlibsamba-credentials0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsamba-credentials0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibsamba-credentials0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsamba-credentials0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibsamba-credentials0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsamba-credentials0 += CSWlibsamba-util0

PACKAGES += CSWlibsamba-hostconfig0
PKGFILES_CSWlibsamba-hostconfig0 += $(call baseisadirs,$(libdir),libsamba-hostconfig\.so\.0\.0\.1)
PKGFILES_CSWlibsamba-hostconfig0 += $(call baseisadirs,$(libdir),libsamba-hostconfig\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsamba-hostconfig0 += $(DESCRIPTION), libsamba-hostconfig.so.0
RUNTIME_DEP_PKGS_CSWlibsamba-hostconfig0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsamba-hostconfig0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsamba-hostconfig0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsamba-hostconfig0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibsamba-hostconfig0 += CSWlibsamba-util0

PACKAGES += CSWlibsamba-policy0
PKGFILES_CSWlibsamba-policy0 += $(call baseisadirs,$(libdir),libsamba-policy\.so\.0\.0\.1)
PKGFILES_CSWlibsamba-policy0 += $(call baseisadirs,$(libdir),libsamba-policy\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsamba-policy0 += $(DESCRIPTION), libsamba-policy.so.0
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibdcerpc0
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibsmbclient-raw0
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsamba-policy0 += CSWlibsamba-util0

PACKAGES += CSWlibsamba-util0
PKGFILES_CSWlibsamba-util0 += $(call baseisadirs,$(libdir),libsamba-util\.so\.0\.0\.1)
PKGFILES_CSWlibsamba-util0 += $(call baseisadirs,$(libdir),libsamba-util\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsamba-util0 += $(DESCRIPTION), libsamba-util.so.0
RUNTIME_DEP_PKGS_CSWlibsamba-util0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsamba-util0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsamba-util0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsamba-util0 += CSWlibiconv2

PACKAGES += CSWlibsamdb0
PKGFILES_CSWlibsamdb0 += $(call baseisadirs,$(libdir),libsamdb\.so\.0\.0\.1)
PKGFILES_CSWlibsamdb0 += $(call baseisadirs,$(libdir),libsamdb\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsamdb0 += $(DESCRIPTION), libsamdb.so.0
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibsamba-credentials0
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsamdb0 += CSWlibsamba-util0

PACKAGES += CSWlibsmbclient-raw0
PKGFILES_CSWlibsmbclient-raw0 += $(call baseisadirs,$(libdir),libsmbclient-raw\.so\.0\.0\.1)
PKGFILES_CSWlibsmbclient-raw0 += $(call baseisadirs,$(libdir),libsmbclient-raw\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsmbclient-raw0 += $(DESCRIPTION), libsmbclient-raw.so.0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibsamba-credentials0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibgensec0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibndr-nbt0
RUNTIME_DEP_PKGS_CSWlibsmbclient-raw0 += CSWlibsamba-util0

PACKAGES += CSWlibsmbconf0
PKGFILES_CSWlibsmbconf0 += $(call baseisadirs,$(libdir),libsmbconf\.so\.0)
PKGFILES_CSWlibsmbconf0 += $(call baseisadirs,$(libdir),libsmbconf\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsmbconf0 += $(DESCRIPTION), libsmbconf.so.0
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibndr0
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibtevent-util0
RUNTIME_DEP_PKGS_CSWlibsmbconf0 += CSWlibsamba-util0


PACKAGES += CSWlibsmbldap0
PKGFILES_CSWlibsmbldap0 += $(call baseisadirs,$(libdir),libsmbldap\.so\.0)
PKGFILES_CSWlibsmbldap0 += $(call baseisadirs,$(libdir),libsmbldap\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsmbldap0 += $(DESCRIPTION), libsmbldap.so.0
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWlibsmbconf0
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsmbldap0 += CSWlibsamba-util0

PACKAGES += CSWlibtevent-util0
PKGFILES_CSWlibtevent-util0 += $(call baseisadirs,$(libdir),libtevent-util\.so\.0\.0\.1)
PKGFILES_CSWlibtevent-util0 += $(call baseisadirs,$(libdir),libtevent-util\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibtevent-util0 += $(DESCRIPTION), libtevent-util.so.0
RUNTIME_DEP_PKGS_CSWlibtevent-util0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibtevent-util0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibtevent-util0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtevent-util0 += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWlibtevent-util0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtevent-util0 += CSWlibsamba-util0

PACKAGES += CSWlibtorture0
PKGFILES_CSWlibtorture0 += $(call baseisadirs,$(libdir),libtorture\.so\.0\.0\.1)
PKGFILES_CSWlibtorture0 += $(call baseisadirs,$(libdir),libtorture\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibtorture0 += $(DESCRIPTION), libtorture.so.0
RUNTIME_DEP_PKGS_CSWlibtorture0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibtorture0 += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWlibtorture0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtorture0 += CSWlibsamba-hostconfig0
RUNTIME_DEP_PKGS_CSWlibtorture0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtorture0 += CSWlibsamba-util0

# Python package
PACKAGES += CSWsamba4-python
SPKG_DESC_CSWsamba4-python = Samba 4 python files
PKGFILES_CSWsamba4-python += $(call baseisadirs,$(libdir),python2.6/site-packages/.*)
RUNTIME_DEP_PKGS_CSWsamba4-python += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWsamba4-python += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4-python += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsamba4-python += CSWlibpython2-6-1-0

# winbind daemon, NSS and PAM modules
PACKAGES += CSWsamba4-winbind
SPKG_DESC_CSWsamba4-winbind = Tools to authenticate users from active directory using winbind
# OBSOLETED_BY_CSWsamba4-windbind += CSWsamba-winbind
# OBSOLETED_BY_CSWsamba4-windbind += CSWsamba-nss
# OBSOLETED_BY_CSWsamba4-windbind += CSWsamba-nss-system-links
# OBSOLETED_BY_CSWsamba4-windbind += CSWsamba-pam-system-links
PKGFILES_CSWsamba4-winbind += $(call baseisadirs,$(bindir),wbinfo)
PKGFILES_CSWsamba4-winbind += $(call baseisadirs,$(libdir),security/pam_winbind\.so)
PKGFILES_CSWsamba4-winbind += $(call pkgfiles_lib,nss_winbind.so.1)
PKGFILES_CSWsamba4-winbind += $(call pkgfiles_lib,libnss_wins.so.2)
PKGFILES_CSWsamba4-winbind += $(call pkgfiles_lib,winbind_krb5_locator.so)
PKGFILES_CSWsamba4-winbind += $(call baseisadirs,$(sbindir),winbindd)
PKGFILES_CSWsamba4-winbind += $(sharedstatedir)/locale/.*/pam_winbind\.mo
PKGFILES_CSWsamba4-winbind += $(mandir)/man5/pam_winbind\.conf\.5
PKGFILES_CSWsamba4
PKGFILES_CSWsamba-winbind += $(mandir)/man7/winbind_krb5_locator\.74-winbind += $(mandir)/man8/pam_winbind\.8
PKGFILES_CSWsamba4
PKGFILES_CSWsmandir)/man1/wbinfo\.1
PKGFILES_CSWsamba4-winbind += $(mandir)/man8/winbindd\.8
PKGFILES_CSWsamba4-winbind += $(sysconfdir)/init\.d/cswwinbind4
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWsamba4-libs
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba4-winbind += CSWliblber2-4-2

PACKAGES += CSWsamba4-nss-system-links
CATALOGNAME_CSWsamba4-nss-system-links = samba4_nss_system_links
PKGFILES_CSWsamba4-nss-system-links  = /usr/lib/nss_winbind_csw.so.1
PKGFILES_CSWsamba4-nss-system-links += /usr/lib/nss_wins_csw.so.1
PKGFILES_CSWsamba4-nss-system-links += /usr/lib/amd64/nss_winbind_csw.so.1
PKGFILES_CSWsamba4-nss-system-links += /usr/lib/amd64/nss_wins_csw.so.1
PKGFILES_CSWsamba4-nss-system-links += /usr/lib/sparcv9/nss_winbind_csw.so.1
PKGFILES_CSWsamba4-nss-system-links += /usr/lib/sparcv9/nss_wins_csw.so.1
SPKG_DESC_CSWsamba4-nss-system-links += Samba 4 nss modules links for the system
RUNTIME_DEP_PKGS_CSWsamba4-nss-system-links += CSWsamba4-winbind
CHECKPKG_OVERRIDES_CSWsamba4-nss-system-links += bad-location-of-file
ARCHALL_CSWsamba4-nss-system-links = 1

PACKAGES += CSWsamba4-pam-system-links
CATALOGNAME_CSWsamba4-pam-system-links = samba4_pam_system_links
PKGFILES_CSWsamba4-pam-system-links  = /usr/lib/security/pam_smbpass_csw.so
PKGFILES_CSWsamba4-pam-system-links += /usr/lib/security/pam_winbind_csw.so
PKGFILES_CSWsamba4-pam-system-links += /usr/lib/security/amd64/pam_smbpass_csw.so
PKGFILES_CSWsamba4-pam-system-links += /usr/lib/security/amd64/pam_winbind_csw.so
PKGFILES_CSWsamba4-pam-system-links += /usr/lib/security/sparcv9/pam_smbpass_csw.so
PKGFILES_CSWsamba4-pam-system-links += /usr/lib/security/sparcv9/pam_winbind_csw.so
SPKG_DESC_CSWsamba4-pam-system-links += Samba 4 pam modules links for the system
RUNTIME_DEP_PKGS_CSWsamba4-pam-system-links += CSW4samba-winbind
RUNTIME_DEP_PKGS_CSWsamba4-pam-system-links += CSW4samba

CHECKPKG_OVERRIDES_CSWsamba4-pam-system-links += surplus-dependency|CSWsamba4
CHECKPKG_OVERRIDES_CSWsamba4-pam-system-links += surplus-dependency|CSWsamba4-winbind
CHECKPKG_OVERRIDES_CSWsamba4-pam-system-links += bad-location-of-file
ARCHALL_CSWsamba4-pam-system-links = 1

# For checking whether we're missing anything, enable and check when updating.
# Should only catch SWAT stuff which is EOL upstream so we're not packaging it
PACKAGES += CSWsamba4-catchall
SPKG_DESC_CSWsamba4-catchall = Samba 4 catch all

# The build fails to add the right rpath to at least the public libs
EXTRA_LDFLAGS = -R$(SMBPRIVATELIB) -Wl,-zignore -Wl,-Bdirect
# EXTRA_LD_OPTIONS = -B direct -z ignore

# At the moment there are errors about python headers missing on 64 bit
#BUILD64 = 1
#ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
#Remove exec_prefix from DIRPATHS:
NODIRPATHS += --exec_prefix=/opt/csw 
enable-nss-wrapper
CONFIGURE_ARGS += --with-acl-support
CONFIGURE_ARGS += --with-aio-support
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS CONFIGURE_ARGS += --with-shared-modules=$(SMB_MODULES)
CONFIGURE_ARGS += --with-ads
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-automount
CONFIGURE_ARGS += --enable-cups
CONFIGURE_ARGS += --with-privatedir=$(SMBPRIVATEDIRir=$(SMBPRIVATEDIR)
CONFIGURE_ARGS += --with-configdir=$(SMBCONFIGDIR)
CONFIGURE_ARGS += --with-lockdir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-statedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-cachedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-pidCONFIGURE_ARGS += --with-privatelibdir=$(SMBPRIVATELIB)
CONFIGURE_ARGS += --with-modulesdir=$(SMBPRIVATELIB)
CONFIGURE_ARGS += --with-logfilebase=$(SMBLOGDIR)
# to stay with the one build with samba 3 build these are private
CONFIGURE_ARGS += --private-libraries=smbclient,smbsharemodes,wbclient
CONFIGURE_ARGS += --bundled-libraries=heimdal,!zlib,!popt,talloc,pytalloc,pytalloc-util,tevent,pytevent,tdb,pytdb,ldb,pyldb

TEST_TARGET = test

# Tests need root
SKIPTEST ?= 1

# Some filenames contain a "=" which totally confuses the svr4 packaging system
# These are:
#   /opt/csw/share/setup/cn=replicator.ldif
#   /opt/csw/share/setup/cn=samba-admin.ldif
#   /opt/csw/share/setup/cn=samba.ldif

EXTRA_PAX_ARGS += -s "/=/-/g"

INITSMF += /etc/opt/csw/init.d/cswsamba4
INITSMF += /etc/opt/csw/init.d/cswwinbind4

PRESERVECONF += $(sysconfdir)/samba/smb.conf

EXTRA_MERGE_DIRS_isa-extra += /usr/lib/64 /usr/lib/security/64
MERGEBASE_/usr/lib/64          = /usr/lib
MERGEBASE_/usr/lib/security/64 = /usr/lib/security
EXTRA_PKGFILES_EXCLUDED += /usr/lib/security

include gar/category.mk

# Set the target dir for modules with the proper arch
NSS_MODULE_DIR = /usr/lib
PAM_MODULE_DIR = /usr/lib/security

ifeq ($(MEMORYMODEL),64)
	NSS_MODULE_DIR = /usr/lib/64
	PAM_MODULE_DIR = /usr/lib/security/64
endif

# Define the targets for the links
NSS_WINBIND_32 = ../..$(libdir)/nss_winbind.so.1
NSS_WINS_32    = ../..$(libdir)/libnss_wins.so.2
NSS_WINBIND_64 = ../../..$(libdir)/nss_winbind.so.1
NSS_WINS_64    = ../../..$(libdir)/libnss_wins.so.2

PAM_WINBIND_32 = ../../..$(libdir)/security/pam_winbind.so
PAM_SMBPASS_32 = ../../..$(libdir)/security/pam_smbpass.so
PAM_WINBIND_64 = ../../../..$(libdir)/security/pam_winbind.so
PAM_SMBPASS_64 = ../../../..$(libdir)/security/pam_smbpass.so/source3/configure

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswsamba $(DESTDIR)/etc/opt/c4
	ginstall $(WORKDIR)/cswwinbind $(DESTDIR)/etc/opt/csw/init.d/cswwinbind4/init.d/cswwinbind
	ginstall -d $(DESTDIR)/etc/opt/csw/samba
	ginstall $(WORKDIR)/smb.conf $(DESTDIR)/etc/opt/csginstall -d $(DESTDIR)/etc/opt/csw/openldap/schema
	ginstall $(WORKSRC)/examples/LDAP/samba.schema $(DESTDIR)/etc/opt/csw/openldap/schema
#	ginstall $(WORKSRC)/nsswitch/nss_winbind.so $(DESTDIR)/$(libdir)/nss_winbind.so.1
#	ginstall $(WORKSRC)/nsswitch/nss_wins.so $(DESTDIR)/$(libdir)/nss_wins.so.1
	# This bit is to install the symlinks to use the NSS modules with the
	# system's nsswitch.conf
	ginstall -d  -m 0755 $(DESTDIR)$(NSS_MODULE_DIR)
	gln -s $(NSS_WINBIND_$(MEMORYMODEL)) $(DESTDIR)$(NSS_MODULE_DIR)/nss_winbind_csw.so.1
	gln -s $(NSS_WINS_$(MEMORYMODEL)) $(DESTDIR)$(NSS_MODULE_DIR)/nss_wins_csw.so.1
	# This bit is to install the symlinks to use the PAM modules with the
	# system's pam.conf
	ginstall -d  -m 0755 $(DESTDIR)$(PAM_MODULE_DIR)
	gln -s $(PAM_WINBIND_$(MEMORYMODEL)) $(DESTDIR)$(PAM_MODULE_DIR)/pam_winbind_csw.so
	gln -s $(PAM_SMBPASS_$(MEMORYMODEL)) $(DESTDIR)$(PAM_MODULE_DIR)/pam_smbpass_csw.soi	@$(MAKECOOKIE)

# python buildtools/bin/waf -v build 

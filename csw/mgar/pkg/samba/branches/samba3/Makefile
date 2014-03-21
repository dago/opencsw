# TBD:
# - Check http://src.opensolaris.org/source/xref/userland/src/components/samba/samba/ from time to time

NAME    = samba
VERSION = 3.6.23
GARTYPE = v2

DESCRIPTION =er)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SM# GARCOMPILER is set below the includeSMB (server)
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
DISTFILESPATCHFILES += 0001-nss_winbind.patch
PATCHFILES += 0002-smbd-patch-for-setgroups.c.patch
PATCHFILES += 0003-rename-nss-modules.patchElibs and packages

BUILD_DEP_PKGS +=BUILD_DEP_PKGS += CSWopenldap-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWcups-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
= CSWlibtalloc-dev
PA =  solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS +CKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACCATALOGNAME_CSWsamba= 6

PACKAGES += CSWsamba
SPKG_DESC_CSWsamba = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsamba += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_readline6
RUNTIME_DEP_PKGS_CSWsamba += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba += CSWlibtdb1+RUNTIME_DEP_PKGS_CSWsamba += CSWlibtevent0+= CDifferent dependency names on different repos
RUNTIME_DEP_PKGS_CSWsamba_5.9  += CSWgamin
RUNTIME_DEP_PKGS_CSWsamba_5.10 += CSWlibfam0
RUNTIME_DEP_PKGS_CSWsamba += $(RUNTIME_DEP_PKGS_CSWsamba_$(GAROSREL))+= Can/man8/swat.8

# Make one unified package for now
OBSOLETED_BY_CSWsamba += CSWsambacommon
CATALOGNAME_CSWsambacommon = samba_common_stub
OBSOLETED_BY_CSWsamba += CSWsambadoc
CATALOGNAME_CSWsambadoc = samba_doc_stub

PACKAGES +CATALOGNAME_CSWsambaclient = samba_client_stub+= CSWsamba-client
SPKG_DESC_CSWsamba-client = Client binaries for samba
SMB_CLIENT_TOOLS = rpcclient smbcacls smbclient smbcquotas smbget smbspool smbtar smbtree
PKGFILES_CSWsamba-client += $(foreach T,$(SMB_CLIENT_TOOLS),$(call baseisadirs,$(bindir),$T) $(mandir)/man1/$T\.1)
PKGFILES_CSWsamba-client += $(mandir)/man5/smbgetrc\.5
PKGFILES_CSWsamba-client += $(mandir)/man8/smbspool\.8
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsambreadline6+= CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-cliRUNTIME_DEP_PKGS_CSWsamba-client += CSWlibtevent0
OBSOLETED_BY_CSWsamba-client += CSWsambaclient saan1/smbclient.1

#PACKAGES += CSWsambadoc
SPKG_DESC_CSWsambadoc = Samba documentation
ARCHALL_CSWsambadoc = 1

PACKAGES +=CATALOGNAME_CSWlibsmbclient0 = 1

PACKAGES += CSWlibsmbclient0
SPKG_DESC_CSWlibsmbclient0 = Samba client library, libsmbclient.so.0
PKGFILES_CSWlibsmbclient0 += $(call pkgfiles_lib,libsmbclient.so.0)
PKGFILES_CSWlibsmbclient0 += $(mandir)/man7/libsmbclient\.7
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWlibsmbclieRUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibtevent0ent0 += CSWlibtdb1
OBSOLETED_BY_CSWlibsmbclient0 += CSWsambalib
CATALOGNAME_CSWsambalib = samba_lib_stub

PACKAGES +CATALOGNAME_CSWlibwbclient0 = b

PACKAGES += CSWlibwbclient0
PKGFILES_CSWlibwbclient0 += $(call pkgfiles_lib,libwbclient.so.0)
SPKG_DESC_CSWlibwbclient0 += Samba client library, libwbclient.so.0

PACKAGESCATALOGNAME_CSWlibnetapi0 = 0

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call pkgfiles_lib,libnetapi.so.0)
SPKG_DESC_CSWlibnetapi0 += Samba client library, libnetapi.so.0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibnetapi0 +RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibtdb1rRUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibtevent0

PACKAGES += CSWlibsmbsharemodes0
CATALOGNAME_CSWlibsmbsharemodes0 = 0

PACKAGES += CSWlibsmbsharemodes0
PKGFILES_CSWlibsmbsharemodes0 += $(call pkgfiles_lib,libsmbsharemodes.so.0)
SPKG_DESC_CSWlibsmbsharemodes0 += Samba client library, libsmbsharemodes.so.0
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibtdb1

PACKACATALOGNAME_CSWlibtdb1 = 1

PACKAGES += CSWlibtdb1
PKGFILES_CSWlibtdb1 += $(call pkgfiles_lib,libtdb.so.1)
SPKG_DESC_CSWlibtdb1 += Samba client library, libtdb.so.samba-nss
CATALOGNAME_CSWsamba-nss = samba_nss
PKGFILES_CSWsamba-nss += $(call baseisadirs,$(libdir),nss_winbind\.so\.1)
PKGFILES_CSWsamba-nss += $(call baseisadirs,$(libdir),nss_wins\.so\.1)
SPKG_DESC_CSWsamba-nss += Samba nss modules,nss_winbind.so.1,nss_wins.so.1
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWlibtevent0
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWlibldap2-4-2
OBSOLETED_BY_CSWsamba-nss += CSWlibnss-winbind1
CHECKPKG_OVERRIDES_CSWsamba-nss += shared-lib-pkgname-mismatch

PACKAGES += CSWsamba-nss-system-links
CATALOGNAME_CSWsamba-nss-system-links = samba_nss_system_links
PKGFILES_CSWsamba-nss-system-links  = /usr/lib/nss_winbind_csw.so.1
PKGFILES_CSWsamba-nss-system-links += /usr/lib/nss_wins_csw.so.1
PKGFILES_CSWsamba-nss-system-links += /usr/lib/amd64/nss_winbind_csw.so.1
PKGFILES_CSWsamba-nss-system-links += /usr/lib/amd64/nss_wins_csw.so.1
PKGFILES_CSWsamba-nss-system-links += /usr/lib/sparcv9/nss_winbind_csw.so.1
PKGFILES_CSWsamba-nss-system-links += /usr/lib/sparcv9/nss_wins_csw.so.1
SPKG_DESC_CSWsamba-nss-system-links += Samba nss modules links for the system
RUNTIME_DEP_PKGS_CSWsamba-nss-system-links += CSWsamba-nssiCHECKPKG_OVERRIDES_CSWsamba-nss-system-links += surplus-dependency|CSWsamba-nss
CHECKPKG_OVERRIDES_CSWsamba-nss-system-links += bad-location-of-fileiCHECKPKG_OVERRIDES_CSWsamba-nss-system-links += file-needed-but-no-package-satisfies-itibnss_winbind.so.samba-pam-system-links
CATALOGNAME_CSWsamba-pam-system-links = samba_pam_system_links
PKGFILES_CSWsamba-pam-system-links  = /usr/lib/security/pam_smbpass_csw.so
PKGFILES_CSWsamba-pam-system-links += /usr/lib/security/pam_winbind_csw.so
PKGFILES_CSWsamba-pam-system-links += /usr/lib/security/amd64/pam_smbpass_csw.so
PKGFILES_CSWsamba-pam-system-links += /usr/lib/security/amd64/pam_winbind_csw.so
PKGFILES_CSWsamba-pam-system-links += /usr/lib/security/sparcv9/pam_smbpass_csw.so
PKGFILES_CSWsamba-pam-system-links += /usr/lib/security/sparcv9/pam_winbind_csw.so
SPKG_DESC_CSWsamba-pam-system-links += Samba pam modules links for the system
RUNTIME_DEP_PKGS_CSWsamba-pam-system-links += CSWsamba-winbind
RUNTIME_DEP_PKGS_CSWsamba-pam-system-links += CSWsamba
CHECKPKG_OVERRIDES_CSWsamba-pam-system-links += surplus-dependency|CSWsamba
CHECKPKG_OVERRIDES_CSWsamba-pam-system-links += surplus-dependency|CSWsamba-winbind
CHECKPKG_OVERRIDES_CSWsamba-pam-system-links += bad-location-of-fileiCHECKPKG_OVERRIDES_CSWsamba-pam-system-links += file-needed-but-no-package-satisfies-itibnss_winbind.so.libtevent0
CATALOGNAME_CSWlibtevent0 = libtevent0
PKGFILES_CSWlibtevent0 += $(call baseisadirs,$(libdir),libtevent\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibtevent0 += $(DESCRIPTION), libtevent.so.0
RUNTIME_DEP_PKGS_CSWlibtevent0 += CSWlibtalloc2

PACKAGES += CSWsamba-dev
CATALOGNAME_CSWsambalibdev = samba_libdev_stubES += CSWsamba-dev
SPKG_DESC_CSWsamba-dev = Development files for Samba, libsmbclient.so.0
PKGFILES_CSWsamba-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibsmbclient0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibnetapi0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibsmbsharemodes0
RUNTIME_DEP_PKGS_CSWsambRUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibtevent0
OBSOLETED_BY_CSWsamba-dev += CSWsambalibdev

PACKAGES += CSWsamba-swat
CATALOGNAME_CSWsambaswat = samba_swat_stubS += CSWsamba-swat
SPKG_DESC_CSWsamba-swat = Web-based samba administration tools
PKGFILES_CSWsamba-swat += $(call baseisadirs,$(sbindir),swat)
PKGFILES_CSWsamba-swat += $(mir)/samba/swat/.*
PKGFILES_CSWsamba-swat += $(prefix)/swat/.*
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-sRUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibtevent0
OBSOLETED_BY_CSWsamba-swat = CSWsambaswat = samba_swat_stub

# Just docs, override for now
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-ByExample/ix01.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-ByExample/appendix.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-ByExample/upgrades.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-ByExample/secure.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-ByExample/nw4migration.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-Developers-Guide/pwencrypt.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/classicalprinting.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/bugreport.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/VFS.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/compiling.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/NetworkBrowsing.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/domain-member.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/SWAT.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/locking.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/ix01.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/samba-pdc.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/install.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/diagnosis.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/FastStart.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/pam.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/winbind.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/Samba3-HOWTO/AccessControls.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/swat.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/lmhosts.5.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/nmbd.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/idmap_tdb2.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/smb.conf.5.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/winbindd.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/smbd.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/net.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/tdbbackup.8.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/local|root/opt/csw/swat/help/manpages/smbclient.1.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/export/home|root/opt/csw/swat/help/Samba3-HOWTO/msdfs.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-ByExample/ix01.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-ByExample/appendix.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-ByExample/upgrades.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-ByExample/happy.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/VFS.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/CUPS-printing.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/SWAT.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/ix01.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/FastStart.html
CHECKPKG_OVERRIDES_CSWsamba-swat += file-with-bad-content|/usr/share|root/opt/csw/swat/help/Samba3-HOWTO/ch-ldap-tls.html

PACKAGES +=CATALOGNAME_CSWsambawb = samba_wb_stub= CSWsamba-winbind
SPKG_DESC_CSWsamba-winbind = Tools to authenticate users from active directory using winbind
PKGFILES_CSWsamba-winbind += $(call baseisadirs,$(libdir),security/pam_winbind\.so)
PKGFILES_CSWsamba-winbind += $(sharedstatedir)/locale/.*/pam_winbind\.mo
PKGFILES_CSWsamba-winbind += $(mandir)/man5/pam_winbind\.conf\.5
PKGFILES_CSWsamba-winbind += $(mandir)/man7/winbind_krb5_locator\.7
PKGFILES_CSWsamba-winbind += $(mandir)/man8/pam_winbind\.8
PKGFILES_CSWsamba-winbind += $(call baseisadirs,$(sbindir),winbindd)
PKGFILES_CSWsamba-winbind += $(mandir)/man8/winbindd\.8
PKGFILES_CSWsamba-winbind += /etc/opt/csw/init.d/cswwinbind
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsasamba-nssCRUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibtdb CRUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibtevent0
# Needed for smb.conf
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWsamba
OBSOLETED_BY_CSWsamba-winbind += CSWsambawawbn/man8/winbindd.8
CHECKPKG_OVERRIDES_CSWsamba-winbind += surpsamba-nssCS### The dependencies names in S10 are getting simpler
ifeq ($(shell /usr/bin/uname -r),5.9)
RUNTIME_DEP_PKGS_CSWsamba += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibgssapi-krb5-2
endif
###

### Needed to work around the ld Bug 
ifeq ($(shell /usr/bin/uname -rp),5.10 sparc)
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtdb1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwbclient0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibtevent0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-nss += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibintl8
endif
###CS# Needed as the configure script doesn't add it
EXTRA_LINKER_FLAGS += -lintl 
EXTRA_LINKER_FLAGS += -z ignore -z lazyloadA_# 32 bit only on Solaris 9 - just to save build time
BUILD64-5.9 =
BUILD64-5.10 = 1
BUILD64 = $(BUILD64-$(GAROSREL))lintl

BUILD64 = 1
ISAEXEC = 1

SMBLOCKDIR = $(localstatedir)/samba/locks
SMBLOGDIR = $(localstatedir)/samba/log
SMBPRIVATEDIR = $(sysconfdir)/samba/private
SMBCONFIGDIR = $(sysconfdir)/samba

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += -nable-nss-wrapper
CONFIGURE_ARGS += --with-acl-support
CONFIGURE_ARGS += --with-aio-support
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-winbind
COenable-nss-wrapper 
CONFIGURE_ARGS += --with-static-modules=vfs_solarisacl
# ZFS is only on S10+
CONFIGURE_ARGS_5.9 += --with-shared-modules=odules=vfs_zfsacl,vfs_prealloc,vfs_cacheprime,vfs_commit,idmap_ldap,idmap_tdb2,idmap_rid,idmap_ad,idmap_hash,idmap_a_5.10acl
CONFIGURE_ARGS += --with-shared-modules=vfs_zfsacl,vfs_prealloc,vfs_cacheprime,vfs_commit,idmap_ldap,idmap_tdb2,idmap_rid,idmap_ad,idmap_hash,idmap_adex
$(CONFIGURE_ARGS_$(GAROSREL))
ap_hash,idmap_adex
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-ads
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-automount
CONFIGURE_ARGS += --with-dnsupdate=no
# Do not setkrb5 this is handeled in gar. Otherwise 64bit will not build
#CONFIGURE_ARGS += --with-krb5=$(prefix)
CONFIGURE_ARGS += --with-privatedir=$(SMBPRIVATEDIR)
CONFIGURE_ARGS += --with-configdir=$(SMBCONFIGDIR)
CONFIGURE_ARGS += --with-lockdir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-statedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-cachedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-piddir=$(SMBLOCKDIR)

CONFIGURE_ARGS += --with-logfileb# Can't use fdatasync atm do to linker problems
# Symbols are not in the right libc:
#(symbol belongs to unavailable version /lib/libc.so (SUNW_1.22.7))to linker problems
CONFIGURE_ARGS += ac_cv_lib_rt_fdatasync=no
CONFIGURE_ARGS += ac_cv_have_fdatasync_decl=no
CONFIGURE_ARGS += ac_cv_lib_extt_fdatasync=no



BUILD_SCRIPTS = $(WORKSRC)/source3/Makefile

TEST_SCRIPTS = $(WORKSRC)/source3/Makefile
TEST_TARGET = test

# Tests need rot
SKIPTEST ?= 1


INSTALL_SCRIPTS = $(WORKSRC)/source3/Makefile

INITSMF += /etc/opt/csw/init.d/cswsamba
INITSMF += /etc/opt/csw/init.d/cswwinbind

MIGRATE_FILES_CSWsamba += samba
PRESERVECONF += $(sysconfdirEXTRA_MERGE_DIRS_isa-extra += /usr/lib/64 /usr/lib/security/64
MERGEBASE_/usr/lib/64          = /usr/lib
MERGEBASE_/usr/lib/security/64 = /usr/lib/security

EXTRA_PKGFILES_EXCLUDED += /usr/lib/security

include gar/category.mk

# Studio 12 is the last supported on Solaris 9
GARCOMPILER_5.9 = SOS12
GARCOMPILER_5.10 = SOS12U3
GARCOMPILER_5.11 = SOS12U3
GARCOMPILER = $(GARCOMPILER_$(GAROSREL))

# Set the target dir for modules with the proper arch
NSS_MODULE_DIR = /usr/lib
PAM_MODULE_DIR = /usr/lib/security

ifeq ($(MEMORYMODEL),64)
	NSS_MODULE_DIR = /usr/lib/64
	PAM_MODULE_DIR = /usr/lib/security/64
endif

# Define the targets for the links
NSS_WINBIND_32 = ../..$(libdir)/nss_winbind.so.1
NSS_WINS_32    = ../..$(libdir)/nss_wins.so.1
NSS_WINBIND_64 = ../../..$(libdir)/nss_winbind.so.1
NSS_WINS_64    = ../../..$(libdir)/nss_wins.so.1

PAM_WINBIND_32 = ../../..$(libdir)/security/pam_winbind.so
PAM_SMBPASS_32 = ../../..$(libdir)/security/pam_smbpass.so
PAM_WINBIND_64 = ../../../..$(libdir)/security/pam_winbind.so
PAM_SMBPASS_64 = ../../../..$(libdir)/security/pam_smbpass.sode gar/category.mk

# Use this hack until this bug has been fixed:
#   https://bugzilla.samba.org/show_bug.cgi?id=8571
post-extract-modulated:
	# Make sure to EXCLUDE the include path from 'krb5-config --cflags' as it is prepended to CFLAGS
	# leading to the inclusion of /opt/csw/include header files before the newly build ones.
	# The line looks like this:
	#   KRB5_CFLAGS="`$KRB5CONFIG --cflags | sed s/@INCLUDE_des@//`"
	# and after the transformation it looks like this:
	#   KRB5_CFLAGS="`$KRB5CONFIG --cflags | sed s,-I/opt/csw/include,,`"
	-perl -pi -e 's!/\@INCLUDE_des\@//!,-I$(includedir),,!' \
		$(WORKSRC)/	@$(MAKECOOKIE)/source3/configure

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswsamba $(DESTDIR)/etc/opt/csw/init.d/cswsamba
	ginstall $(WORKDIR)/cswwinbind $(DESTDIR)/etc/opt/csw/init.d/cswwinbind
	ginstall -d $(DESTDIR)/etc/opt/csw/samba
	ginstall $(WORKDIR)/smb.conf $(DESTDIR)/etc/opt/csw/samba/smb.conf
	ginstall $(nss_winbind.so $(DESTDIR)/$(libdir)/nss_winbind.so.1
	ginstall $(WORKSRC)/nsswitch/nss_wins.so $(DESTDIR)/$(libdir)/nss_wins.so.1
	# This bit is to install the symlinks to use the NSS modules with the
	# system's nsswitch.conf
	ginstall -d  -m 0755 $(DESTDIR)$(NSS_MODULE_DIR)
	gln -s $(NSS_WINBIND_$(MEMORYMODEL)) $(DESTDIR)$(NSS_MODULE_DIR)/nss_winbind_csw.so.1
	gln -s $(NSS_WINS_$(MEMORYMODEL)) $(DESTDIR)$(NSS_MODULE_DIR)/nss_wins_csw.so.1
	# This bit is to install the symlinks to use the PAM modules with the
	# system's pam.conf
	ginstall -d  -m 0755 $(DESTDIR)$(PAM_MODULE_DIR)
	gln -s $(PAM_WINBIND_$(MEMORYMODEL)) $(DESTDIR)$(PAM_MODULE_DIR)/pam_winbind_csw.so
	gln -s $(PAM_SMBPASS_$(MEMORYMODEL)) $(DESTDIR)$(PAM_MODULE_DIR)/pam_smbpass_csw.so
	@$(MAKECOOKIE)

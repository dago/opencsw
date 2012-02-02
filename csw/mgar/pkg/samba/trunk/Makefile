# TBD:
# - smb.conf is searched in /opt/csw/lib/64/smb.conf instead of /etc/opt/csw/samba/smb.conf
# - secrets.tdb is searched in /opt/csw/private/secrets.tdb instead of /etc/opt/csw/samba/private/secrets.tdb

NAME = samba
VERSION = 3.6.3
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
DISTFILES += cswkrb5.conf

#What needs to be fixed:
# Split libs and packages

BUILD_DEP_PKGS += CSWlibtalloc-dev
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWsamba
SPKG_DESC_CSWsamba = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsamba += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWsamba += CSWlibfam0
RUNTIME_DEP_PKGS_CSWsamba += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWsamba += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibwbclient0

# Just docs override for now
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/lmhosts.5
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/smb.conf.5
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/nmbd.8
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/smbd.8
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/tdbbackup.8
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/idmap_tdb2.8
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/net.8
CHECKPKG_OVERRIDES_CSWsamba += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/swat.8

# Make one unified package for now
OBSOLETED_BY_CSWsamba += CSWsambacommon
OBSOLETED_BY_CSWsamba += CSWsambadoc

PACKAGES += CSWsamba-client
SPKG_DESC_CSWsamba-client = Client binaries for samba
SMB_CLIENT_TOOLS = rpcclient smbcacls smbclient smbcquotas smbget smbspool smbtar smbtree
PKGFILES_CSWsamba-client += $(foreach T,$(SMB_CLIENT_TOOLS),$(call baseisadirs,$(bindir),$T) $(mandir)/man1/$T\.1)
PKGFILES_CSWsamba-client += $(mandir)/man5/smbgetrc\.5
PKGFILES_CSWsamba-client += $(mandir)/man8/smbspool\.8
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-client += CSWlibtdb1
OBSOLETED_BY_CSWsamba-client += CSWsambaclient
CATALOGNAME_CSWsambaclient = samba_client_stub

# Just docs, override for now
CHECKPKG_OVERRIDES_CSWsamba-client += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/smbclient.1

#PACKAGES += CSWsambacommon
SPKG_DESC_CSWsambacommon = Shared support files for samba
RUNTIME_DEP_PKGS_CSWsambacommon += CSWsasl
RUNTIME_DEP_PKGS_CSWsambacommon += CSWreadline
RUNTIME_DEP_PKGS_CSWsambacommon += CSWlibpopt
RUNTIME_DEP_PKGS_CSWsambacommon += CSWlibnet
RUNTIME_DEP_PKGS_CSWsambacommon += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWsambacommon += CSWiconv
RUNTIME_DEP_PKGS_CSWsambacommon += CSWggettext

#PACKAGES += CSWsambadoc
SPKG_DESC_CSWsambadoc = Samba documentation
ARCHALL_CSWsambadoc = 1

PACKAGES += CSWlibsmbclient0
SPKG_DESC_CSWlibsmbclient0 = Samba client library, libsmbclient.so.0
PKGFILES_CSWlibsmbclient0 += $(call pkgfiles_lib,libsmbclient.so.0)
PKGFILES_CSWlibsmbclient0 += $(mandir)/man7/libsmbclient\.7
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibtdb1
OBSOLETED_BY_CSWlibsmbclient0 += CSWsambalib
CATALOGNAME_CSWsambalib = samba_lib_stub

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call pkgfiles_lib,libnetapi.so.0)
SPKG_DESC_CSWlibnetapi0 += Samba client library, libnetapi.so.0

PACKAGES += CSWlibsmbsharemodes0
PKGFILES_CSWlibsmbsharemodes0 += $(call pkgfiles_lib,libsmbsharemodes.so.0)
SPKG_DESC_CSWlibsmbsharemodes0 += Samba client library, libsmbsharemodes.so.0

PACKAGES += CSWlibtdb1
PKGFILES_CSWlibtdb1 += $(call pkgfiles_lib,libtdb.so.1)
SPKG_DESC_CSWlibtdb1 += Samba client library, libtdb.so.1
RUNTIME_DEP_PKGS_CSWsamba += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWlibtdb1 += CSWlibintl8

PACKAGES += CSWlibwbclient0
PKGFILES_CSWlibwbclient0 += $(call pkgfiles_lib,libwbclient.so.0)
SPKG_DESC_CSWlibwbclient0 += Samba client library, libwbclient.so.0
RUNTIME_DEP_PKGS_CSWlibwbclient0 += CSWlibintl8

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call pkgfiles_lib,libnetapi.so.0)
SPKG_DESC_CSWlibnetapi0 += Samba client library, libnetapi.so.0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibnetapi0 += CSWlibldap2-4-2

PACKAGES += CSWlibsmbsharemodes0
PKGFILES_CSWlibsmbsharemodes0 += $(call pkgfiles_lib,libsmbsharemodes.so.0)
SPKG_DESC_CSWlibsmbsharemodes0 += Samba client library, libsmbsharemodes.so.0
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibsmbsharemodes0 += CSWlibtdb1

PACKAGES += CSWlibtdb1
PKGFILES_CSWlibtdb1 += $(call pkgfiles_lib,libtdb.so.1)
SPKG_DESC_CSWlibtdb1 += Samba client library, libtdb.so.1

PACKAGES += CSWsamba-dev
SPKG_DESC_CSWsamba-dev = Development files for Samba, libsmbclient.so.0
PKGFILES_CSWsamba-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibsmbclient0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibnetapi0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibsmbsharemodes0
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWsamba
OBSOLETED_BY_CSWsamba-dev += CSWsambalibdev
CATALOGNAME_CSWsambalibdev = samba_libdev_stub

PACKAGES += CSWsamba-swat
SPKG_DESC_CSWsamba-swat = Web-based samba administration tools
PKGFILES_CSWsamba-swat += $(call baseisadirs,$(sbindir),swat)
PKGFILES_CSWsamba-swat += $(mandir)/.*/swat\.*
#PKGFILES_CSWsamba-swat += $(sharedstatedir)/samba/swat/.*
PKGFILES_CSWsamba-swat += $(prefix)/swat/.*
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibz1
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWlibtdb1
OBSOLETED_BY_CSWsamba-swat = CSWsambaswat
CATALOGNAME_CSWsambaswat = samba_swat_stub

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

PACKAGES += CSWsamba-winbind
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
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibtdb1
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibwbclient0
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsamba-winbind += CSWlibldap2-4-2
OBSOLETED_BY_CSWsamba-winbind += CSWsambawb
CATALOGNAME_CSWsambawb = samba_wb_stub

# Just docs, override for now
CHECKPKG_OVERRIDES_CSWsamba-winbind += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/winbindd.8

EXTRA_CFLAGS = -lintl
EXTRA_LDFLAGS = -lintl

BUILD64 = 1
ISAEXEC = 1

SMBLOCKDIR = $(localstatedir)/samba/locks
SMBLOGDIR = $(localstatedir)/samba/log
SMBPRIVATEDIR = $(sysconfdir)/samba/private
SMBCONFIGDIR = $(sysconfdir)/samba

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-socket-wrapper
CONFIGURE_ARGS += --enable-nss-wrapper
CONFIGURE_ARGS += --with-acl-support
CONFIGURE_ARGS += --with-aio-support
CONFIGURE_ARGS += --with-pam
# CONFIGURE_ARGS += --with-krb5=$(prefix)
CONFIGURE_ARGS += --with-privatedir=$(SMBPRIVATEDIR)
CONFIGURE_ARGS += --with-configdir=$(SMBCONFIGDIR)
CONFIGURE_ARGS += --with-lockdir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-statedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-cachedir=$(SMBLOCKDIR)
CONFIGURE_ARGS += --with-piddir=$(SMBLOCKDIR)

CONFIGURE_ARGS += --with-logfilebase=$(SMBLOGDIR)

CONFIGURE_ARGS-64 +=  --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

BUILD_SCRIPTS = $(WORKSRC)/source3/Makefile

TEST_SCRIPTS = $(WORKSRC)/source3/Makefile
TEST_TARGET = test

# Tests need root
SKIPTEST ?= 1

INSTALL_SCRIPTS = $(WORKSRC)/source3/Makefile

INITSMF += /etc/opt/csw/init.d/cswsamba
INITSMF += /etc/opt/csw/init.d/cswwinbind

MIGRATE_FILES_CSWsamba += samba
PRESERVECONF += $(sysconfdir)/samba/smb.conf

include gar/category.mk

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
		$(WORKSRC)/source3/configure

post-merge:
	ginstall -d $(PKGROOT)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswsamba $(PKGROOT)/etc/opt/csw/init.d/cswsamba
	ginstall $(WORKDIR)/cswwinbind $(PKGROOT)/etc/opt/csw/init.d/cswwinbind
	ginstall -d $(PKGROOT)/etc/opt/csw/samba
	ginstall $(WORKDIR)/smb.conf $(PKGROOT)/etc/opt/csw/samba/smb.conf

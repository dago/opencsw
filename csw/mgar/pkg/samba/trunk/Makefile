# TBD:
# - smb.conf is searched in /opt/csw/lib/64/smb.conf instead of /etc/opt/csw/samba/smb.conf
# - secrets.tdb is searched in /opt/csw/private/secrets.tdb instead of /etc/opt/csw/samba/private/secrets.tdb

NAME = samba
VERSION = 3.6.1
CATEGORIES = apps

DESCRIPTION = Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
endef

MASTER_SITES = http://samba.org/samba/ftp/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswsamba
EXPANDVARS += cswsamba

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
RUNTIME_DEP_PKGS_CSWsamba += CSWgamin
RUNTIME_DEP_PKGS_CSWsamba += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsamba += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsamba += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWsamba += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWsamba += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsamba += CSWoldaprt

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
RUNTIME_DEP_PKGS_CSWsamba-client += CSWoldaprt
RUNTIME_DEP_PKGS_CSWsamba-client += CSWsamba
OBSOLETED_BY_CSWsamba-client += CSWsambaclient
CATALOGNAME_CSWsambaclient = samba_client_stub

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
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWoldaprt
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibsmbclient0 += CSWlibk5crypto3
OBSOLETED_BY_CSWlibsmclient0 += CSWsambalib
CATALOGNAME_CSWsambalib = samba_lib_stub

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call pkgfiles_lib,libnetapi.so.0)
SPKG_DESC_CSWlibnetapi0 += Samba client library, libnetapi.so.0
RUNTIME_DEP_PKGS_CSWsamba += CSWlibnetapi0

PACKAGES += CSWlibsmbsharemodes0
PKGFILES_CSWlibsmbsharemodes0 += $(call pkgfiles_lib,libsmbsharemodes.so.0)
SPKG_DESC_CSWlibsmbsharemodes0 += Samba client library, libsmbsharemodes.so.0
RUNTIME_DEP_PKGS_CSWsamba += CSWlibsmbsharemodes0

PACKAGES += CSWlibtdb1
PKGFILES_CSWlibtdb1 += $(call pkgfiles_lib,libtdb.so.1)
SPKG_DESC_CSWlibtdb1 += Samba client library, libtdb.so.1
RUNTIME_DEP_PKGS_CSWsamba += CSWlibtdb1

PACKAGES += CSWlibwbclient0
PKGFILES_CSWlibwbclient0 += $(call pkgfiles_lib,libwbclient.so.0)
SPKG_DESC_CSWlibwbclient0 += Samba client library, libwbclient.so.0

PACKAGES += CSWlibnetapi0
PKGFILES_CSWlibnetapi0 += $(call pkgfiles_lib,libnetapi.so.0)
SPKG_DESC_CSWlibnetapi0 += Samba client library, libnetapi.so.0

PACKAGES += CSWlibsmbsharemodes0
PKGFILES_CSWlibsmbsharemodes0 += $(call pkgfiles_lib,libsmbsharemodes.so.0)
SPKG_DESC_CSWlibsmbsharemodes0 += Samba client library, libsmbsharemodes.so.0

PACKAGES += CSWlibtdb1
PKGFILES_CSWlibtdb1 += $(call pkgfiles_lib,libtdb.so.1)
SPKG_DESC_CSWlibtdb1 += Samba client library, libtdb.so.1

PACKAGES += CSWsamba-dev
SPKG_DESC_CSWsamba-dev = Development files for Samba, libsmbclient.so.0
PKGFILES_CSWsamba-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsamba-dev += CSWlibsmbclient0
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
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWoldaprt
RUNTIME_DEP_PKGS_CSWsamba-swat += CSWsamba
OBSOLETED_BY_CSWsamba-swat = CSWsambaswat
CATALOGNAME_CSWsambaswat = samba_swat_stub

#PACKAGES += CSWsambawb
SPKG_DESC_CSWsambawb = Tools to authenticate users from active directory using winbind
RUNTIME_DEP_PKGS_CSWsambawb = CSWsamba

EXTRA_CFLAGS = -lintl
EXTRA_LDFLAGS = -lintl

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-socket-wrapper
CONFIGURE_ARGS += --with-privatedir=$(sysconfdir)/samba/private
CONFIGURE_ARGS += --with-configdir=$(sysconfdir)/samba

CONFIGURE_ARGS-64 +=  --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

BUILD_SCRIPTS = $(WORKSRC)/source3/Makefile

TEST_SCRIPTS = $(WORKSRC)/source3/Makefile
TEST_TARGET = test

# Tests need root
SKIPTEST ?= 1

INSTALL_SCRIPTS = $(WORKSRC)/source3/Makefile

INITSMF += /etc/opt/csw/init.d/cswsamba

MIGRATE_FILES += samba
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
	ginstall -d $(PKGROOT)/etc/opt/csw/samba
	ginstall $(WORKDIR)/smb.conf $(PKGROOT)/etc/opt/csw/samba/smb.conf

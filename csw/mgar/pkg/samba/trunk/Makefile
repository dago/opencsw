NAME = samba
VERSION = 3.6.1
CATEGORIES = apps

DESCRIPTION = Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
endef

MASTER_SITES = http://samba.org/samba/ftp/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

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
OBSOLETED_BY_CSWsamba += CSWsambaclient
OBSOLETED_BY_CSWsamba += CSWsambacommon
OBSOLETED_BY_CSWsamba += CSWsambadoc
OBSOLETED_BY_CSWsamba += CSWsambalib

#PACKAGES += CSWsambaclient
SPKG_DESC_CSWsambaclient = Client binaries for samba
RUNTIME_DEP_PKGS_CSWsambaclient += CSWsasl 
RUNTIME_DEP_PKGS_CSWsambaclient += CSWsambacommon
RUNTIME_DEP_PKGS_CSWsambaclient += CSWreadline
RUNTIME_DEP_PKGS_CSWsambaclient += CSWlibpopt
RUNTIME_DEP_PKGS_CSWsambaclient += CSWlibnet
RUNTIME_DEP_PKGS_CSWsambaclient += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWsambaclient += CSWiconv
RUNTIME_DEP_PKGS_CSWsambaclient += CSWggettext

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

#PACKAGES += CSWsambalib
SPKG_DESC_CSWsambalib = Samba shared libraries
RUNTIME_DEP_PKGS_CSWsambalib += CSWsasl
RUNTIME_DEP_PKGS_CSWsambalib += CSWlibnet
RUNTIME_DEP_PKGS_CSWsambalib += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWsambalib += CSWiconv

PACKAGES += CSWsamba-dev
SPKG_DESC_CSWsamba-dev = Development files for the samba libraries
PKGFILES_CSWsamba-dev += $(PKGFILES_DEVEL)
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

CONFIGURE_ARGS-64 +=  --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

BUILD_SCRIPTS = $(WORKSRC)/source3/Makefile

TEST_SCRIPTS = $(WORKSRC)/source3/Makefile
TEST_TARGET = test

# Tests need root
SKIPTEST ?= 1

INSTALL_SCRIPTS = $(WORKSRC)/source3/Makefile

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


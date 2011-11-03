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

#PACKAGES += CSWsambaclient
SPKG_DESC_CSWsambaclient = Client binaries for samba
RUNTIME_DEP_PKGS_CSWsambaclient = CSWsasl  CSWsambacommon CSWreadline CSWlibpopt CSWlibnet CSWkrb5lib CSWiconv CSWggettext

#PACKAGES += CSWsambacommon
SPKG_DESC_CSWsambacommon = Shared support files for samba
RUNTIME_DEP_PKGS_CSWsambacommon = CSWsasl CSWreadline CSWlibpopt CSWlibnet CSWkrb5lib CSWiconv CSWggettext

#PACKAGES += CSWsambadoc
SPKG_DESC_CSWsambadoc = Samba documentation
ARCHALL_CSWsambadoc = 1

#PACKAGES += CSWsambalib
SPKG_DESC_CSWsambalib = Samba shared libraries
RUNTIME_DEP_PKGS_CSWsambalib = CSWsasl CSWlibnet CSWkrb5lib CSWiconv

#PACKAGES += CSWsambalibdev
SPKG_DESC_CSWsambalibdev = Development files for the samba libraries
RUNTIME_DEP_PKGS_CSWsambalibdev = CSWsasl CSWlibnet CSWkrb5lib CSWiconv

#PACKAGES += CSWsambaswat
SPKG_DESC_CSWsambaswat = Web-based samba administration tools
RUNTIME_DEP_PKGS_CSWsambaswat = CSWsasl CSWlibpopt CSWlibnet CSWlibcups CSWkrb5lib CSWiconv CSWggettext

#PACKAGES += CSWsambawb
SPKG_DESC_CSWsambawb = not sure what this is
RUNTIME_DEP_PKGS_CSWsambawb = CSWsamba

EXTRA_CFLAGS = -lintl
EXTRA_LDFLAGS = -lintl

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-socket-wrapper

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


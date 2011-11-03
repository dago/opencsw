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
# old installed libsmbclient.h is included first at Compiling libsmb/libsmb_cache.c
# Split libs and packages

BUILD_DEP_PKGS += CSWlibtalloc-dev
#PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS = isa-pentium_pro

PACKAGES += CSWsamba
SPKG_DESC_CSWsamba = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWsamba = CSWsasl CSWsambacommon CSWoldaprt CSWlibpopt CSWlibnet CSWlibcups CSWkrb5lib CSWiconv CSWggettext CSWfam

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

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
CONFIGURE_ARGS = $(DIRPATHS) --enable-socket-wrapper
EXTRA_CFLAGS = -lintl
EXTRA_LDFLAGS = -lintl

#Tests need root
SKIPTEST = 1
TEST_TARGET = test
TEST_SCRIPTS = $(WORKSRC)/source3/Makefile

BUILD_SCRIPTS = $(WORKSRC)/source3/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/source3/Makefile


include gar/category.mk

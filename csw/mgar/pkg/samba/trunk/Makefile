GARNAME = samba
GARVERSION = 3.4.3
CATEGORIES = apps

DESCRIPTION = Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
endef

MASTER_SITES = http://samba.org/samba/ftp/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWsamba CSWsambaclient CSWsambacommon CSWsambadoc CSWsambalib CSWsambalibdev CSWsambaswat CSWsambawb

CATALOGNAME_CSWsamba = samba
SPKG_DESC_CSWsamba = $(DESCRIPTION)
CATALOGNAME_CSWsambaclient =  samba_client
SPKG_DESC_CSWsambaclient = Client binaries for samba
CATALOGNAME_CSWsambacommon = samba_common
SPKG_DESC_CSWsambacommon = Shared support files for samba
CATALOGNAME_CSWsambadoc = samba_doc
SPKG_DESC_CSWsambadoc = Samba documentation
CATALOGNAME_CSWsambalib = samba_lib
SPKG_DESC_CSWsambalib = Samba shared libraries
CATALOGNAME_CSWsambalibdev = samba_libdev
SPKG_DESC_CSWsambalibdev = Development files for the samba libraries
CATALOGNAME_CSWsambaswat = samba_swat
SPKG_DESC_CSWsambaswat = Web-based samba administration tools
CATALOGNAME_CSWsambawb = samba_wb
SPKG_DESC_CSWsambawb = not sure what this is

REQUIRED_PKGS_CSWsamba = CSWsasl CSWsambacommon CSWoldaprt CSWlibpopt CSWlibnet CSWlibcups CSWkrb5lib CSWiconv CSWggettext CSWfam
REQUIRED_PKGS_CSWsambaclient = CSWsasl  CSWsambacommon CSWreadline CSWlibpopt CSWlibnet CSWkrb5lib CSWiconv CSWggettext
REQUIRED_PKGS_CSWsambacommon = CSWsasl CSWreadline CSWlibpopt CSWlibnet CSWkrb5lib CSWiconv CSWggettext
REQUIRED_PKGS_CSWsambalib = CSWsasl CSWlibnet CSWkrb5lib CSWiconv
REQUIRED_PKGS_CSWsambalibdev = CSWsasl CSWlibnet CSWkrb5lib CSWiconv
REQUIRED_PKGS_CSWsambaswat = CSWsasl CSWlibpopt CSWlibnet CSWlibcups CSWkrb5lib CSWiconv CSWggettext
REQUIRED_PKGS_CSWsambawb = CSWsamba

ARCHALL_CSWsambadoc = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
CONFIGURE_ARGS = $(DIRPATHS)

BUILD_SCRIPTS = $(WORKSRC)/source3/Makefile

include gar/category.mk

GARNAME = samba
GARVERSION = 3.3.4
CATEGORIES = apps

DESCRIPTION = Tools to access a servers filespace and printers via SMB (server)
define BLURB
  Tools to access a servers filespace and printers via SMB (server)
endef

MASTER_SITES = http://samba.org/samba/ftp/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWsamba CSWsambaclient CSWsambacommon CSWsambadoc CSWsambalib CSWsambalibdev CSWsambaswat CSWsambawb

CATALOGNAME_CSWsamba = samba
CATALOGNAME_CSWsambaclient =  samba_client
CATALOGNAME_CSWsambacommon = samba_common
CATALOGNAME_CSWsambadoc = samba_doc
CATALOGNAME_CSWsambalib = samba_lib
CATALOGNAME_CSWsambalibdev = samba_libdev
CATALOGNAME_CSWsambaswat = samba_swat
CATALOGNAME_CSWsambawb = samba_wb

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

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

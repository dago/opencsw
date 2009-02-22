GARNAME = rdesktop
GARVERSION = 1.6.0
CATEGORIES = apps

DESCRIPTION = RDP client for Windows NT/2000/2003/XP Terminal Server
define BLURB
	rdesktop is an open source client for Windows Terminal Services, capable of natively speaking Remote Desktop Protocol (RDP) in order to present the user's Windows desktop. Supported servers include Windows 2000 Server, Windows Server 2003, Windows Server 2008, Windows XP, Windows Vista and Windows NT Server 4.0.
endef

PACKAGES = CSWrdesktop
CATALOGNAME_CSWrdesktop = rdesktop

MASTER_SITES = $(SF_MIRROR)
SPKG_SOURCEURL = http://www.rdesktop.org/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS_CSWrdesktop = CSWiconv CSWosslrt

#No test/check target provided by rdesktop
SKIPTEST=1

include gar/category.mk

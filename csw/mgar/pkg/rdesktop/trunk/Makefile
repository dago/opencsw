NAME = rdesktop
VERSION = 1.6.0
CATEGORIES = apps

DESCRIPTION = RDP client for Windows NT/2000/2003/XP Terminal Server
define BLURB
  rdesktop is an open source client for Windows Terminal Services, capable of natively
  speaking Remote Desktop Protocol (RDP) in order to present the user's Windows desktop.
  Supported servers include Windows 2000 Server, Windows Server 2003, Windows Server 2008,
  Windows XP, Windows Vista and Windows NT Server 4.0.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Apply patch from
#   https://sourceforge.net/tracker/?func=detail&aid=2812158&group_id=24366&atid=381349
# as referenced from
#   http://csiuo.com/drupal/content/rdesktop-160-and-windows-server-2008-sp2
PATCHFILES += fix-2022945.patch

PACKAGES = CSWrdesktop
CATALOGNAME_CSWrdesktop = rdesktop

VENDOR_URL = http://www.rdesktop.org/

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWrdesktop += CSWiconv
RUNTIME_DEP_PKGS_CSWrdesktop += CSWosslrt
RUNTIME_DEP_PKGS_CSWrdesktop += CSWlibao

# No test/check target provided by rdesktop
TEST_SCRIPTS =

include gar/category.mk

NAME = rdesktop
VERSION = 1.7.0
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

PACKAGES = CSWrdesktop
CATALOGNAME_CSWrdesktop = rdesktop

VENDOR_URL = http://www.rdesktop.org/

BUILD_DEP_PKGS += CSWlibao-dev
BUILD_DEP_PKGS += CSWlibsamplerate-dev
BUILD_DEP_PKGS += CSWossldevel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWrdesktop += CSWiconv
RUNTIME_DEP_PKGS_CSWrdesktop += CSWlibsamplerate0
RUNTIME_DEP_PKGS_CSWrdesktop += CSWosslrt

# No test/check target provided by rdesktop
TEST_SCRIPTS =

# The path is just an example and nobody will probably look into it
CHECKPKG_OVERRIDES_CSWrdesktop += file-with-bad-content|/usr/local|root/opt/csw/share/rdesktop/keymaps/is

include gar/category.mk

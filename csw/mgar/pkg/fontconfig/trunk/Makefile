# $Id$

NAME = fontconfig
VERSION = 2.11.0
GARTYPE = v2

DESCRIPTION = A library for configuring and customizing font accesszing font access.
define BLURB
  Fontconfig is a library for configuring and customizing font access. It
  contains two essential modules, the configuration module which builds an
  internal configuration from XML files and the matching module which accepts
  font patterns and returns the nearest matching font.
endef

MASTER_SITES = http://www.fontconfig.org/re+= $(DISTNAME).tar.gz
DISTFILES += CSWfontconfig.postinstall

VENDOR_URL = http://www.fontconfig.org

PACKAGES += CSWlibfontconfig1
PKGFILES_CSWlibfontconfig1 += $(call pkgfiles_lib,libfontconfig.so.1)
SPKG_DESC_CSWlibfontconfig1 += A library for configuring and customizing font access+= $(DESCRIPTION), libfontconfig.so.1
RUNTIME_DEP_PKGS_CSWlibfontconfig1 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibfontexpat1

PACKAGES += CSWfontconfig-dev
SPKG_DESC_CSWfontconfig-dev += Development files for libfontconfig.so.1
PKGFILES_CSWfontconfig-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWfontconfig-dev += CSWlibfontconfig1
OBSOLETED_BY_CSWfontconfig-dev += CSWfconfig-dev

PACKAGES += CSWfontconfig
SPKG_DESC_CSWfontconfig = A library for configuring and customizing font access
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWfontconfig += CSWlibfontconfig1
# This is for /usr/share/fonts which is ok
CHECKPKG_OVERRIDES_CSWfontconfig += file-with-bad-content|/usr/share|root/etc/opt/csw/fontconfig/fonts.conf

OBSOLETED_BY_CSWfontconfig += CSWfconfig
CATALOGNAME_CSWfconfig = fontconfig_stub

BUILD64_LIBS_ONLY = 1

MIGRATE_FILES_CSWfontconfigg/

MIGRATE_FILES = fontconfig

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-fonts=/usr/openwin/lib/X11/fonts
CONFIGURE_ARGS += --with-add-fonts=/usr/openwin/lib/locale,/usr/share/fonts,/opt/csw/share/fonts
CONFIGURE_ARGS += --with-cache-dir=/var/opt/csw/cache/fontconfig
CONFIGURbaseconfigdir=/etc/opt/csw/fontconfig

include gar/category.mk

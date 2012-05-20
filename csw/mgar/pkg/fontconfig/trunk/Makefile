# $Id$

NAME = fontconfig
VERSION = 2.8.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library for configuring and customizing font access.
define BLURB
  Fontconfig is a library for configuring and customizing font access. It
  contains two essential modules, the configuration module which builds an
  internal configuration from XML files and the matching module which accepts
  font patterns and returns the nearest matching font.
endef

MASTER_SITES = http://www.fontconfig.org/release/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWfconfig.postinstall

PATCHFILES = fix-zerowidth-struct.patch

BUILD64_LIBS_ONLY = 1

SPKG_SOURCEURL = http://www.fontconfig.org/

MIGRATE_FILES = fontconfig

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-fonts=/usr/openwin/lib/X11/fonts
CONFIGURE_ARGS += --with-add-fonts=/usr/openwin/lib/locale,/usr/share/fonts,/opt/csw/share/fonts
CONFIGURE_ARGS += --with-cache-dir=/var/opt/csw/cache/fontconfig
CONFIGURE_ARGS += --with-confdir=/etc/opt/csw/fontconfig

PACKAGES += CSWlibfontconfig1
PKGFILES_CSWlibfontconfig1 += $(call baseisadirs,$(libdir),libfontconfig\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibfontconfig1 += $(DESCRIPTION), libfontconfig.so.1
RUNTIME_DEP_PKGS_CSWlibfontconfig1 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibfontconfig1 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibfontconfig1 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibfontconfig1 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibfontconfig1 += CSWlibz1

PACKAGES += CSWfconfig-dev
SPKG_DESC_CSWfconfig-dev += $(DESCRIPTION), development files
PKGFILES_CSWfconfig-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWfconfig-dev += CSWlibfontconfig1

PACKAGES += CSWfconfig
CATALOGNAME_CSWfconfig = fontconfig
SPKG_DESC_CSWfconfig = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWfconfig += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWfconfig += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWfconfig += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWfconfig += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWfconfig += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWfconfig += CSWlibz1
# It's the documentation.
CHECKPKG_OVERRIDES_CSWfconfig += file-with-bad-content
# One of the classic: "historical reasons"
CHECKPKG_OVERRIDES_CSWfconfig += catalogname-does-not-match-pkgname|pkgname=CSWfconfig|catalogname=fontconfig|expected-catalogname=fconfig

include gar/category.mk

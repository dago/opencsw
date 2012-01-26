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

RUNTIME_DEP_PKGS = CSWexpat CSWftype2 CSWzlib CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
PACKAGES = CSWfconfig
CATALOGNAME = fontconfig

SPKG_SOURCEURL = http://www.fontconfig.org/

MIGRATE_FILES = fontconfig

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-fonts=/usr/openwin/lib/X11/fonts
CONFIGURE_ARGS += --with-add-fonts=/usr/openwin/lib/locale,/usr/share/fonts,/opt/csw/share/fonts
CONFIGURE_ARGS += --with-cache-dir=/var/opt/csw/cache/fontconfig
CONFIGURE_ARGS += --with-confdir=/etc/opt/csw/fontconfig

include gar/category.mk

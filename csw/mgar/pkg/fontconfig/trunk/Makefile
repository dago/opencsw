GARNAME = fontconfig
GARVERSION = 2.6.0
CATEGORIES = lib

DESCRIPTION = A library for configuring and customizing font access.
define BLURB
  Fontconfig is a library for configuring and customizing font access. It
  contains two essential modules, the configuration module which builds an
  internal configuration from XML files and the matching module which accepts
  font patterns and returns the nearest matching font.
endef

MASTER_SITES = http://www.fontconfig.org/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
#DISTFILES += $(call admfiles,postinstall)
DISTFILES += CSWfconfig.postinstall

REQUIRED_PKGS = CSWexpat CSWftype2 CSWzlib CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
PACKAGES = CSWfconfig
CATALOGNAME_CSWfconfig = fontconfig

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-default-fonts=/usr/openwin/lib/X11/fonts
CONFIGURE_ARGS += --with-add-fonts=/usr/openwin/lib/locale,/usr/share/fonts
CONFIGURE_ARGS += --with-cache-dir=/var/opt/csw/cache/fontconfig
CONFIGURE_ARGS += --with-confdir=/opt/csw/etc/fontconfig

pre-package:
	@rm -f $(DESTDIR)$(libdir)/libfontconfig.la*
	@rm -f $(DESTDIR)/opt/csw/etc/fonts/fonts.conf.bak
	@$(MAKECOOKIE)

include gar/category.mk

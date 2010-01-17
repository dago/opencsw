GARNAME = gtkwave
GARVERSION = 3.2.3
CATEGORIES = devel

DESCRIPTION = Brief description
define BLURB
  Long description
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_BASE_PKGS = CSWtofrodos

GARCOMPILER = GNU

REQUIRED_PKGS  = CSWfconfig
REQUIRED_PKGS += CSWftype2
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWgtk2
REQUIRED_PKGS += CSWlibatk
REQUIRED_PKGS += CSWlibcairo
REQUIRED_PKGS += CSWpango
REQUIRED_PKGS += CSWtcl
REQUIRED_PKGS += CSWzlib

PATCHFILES  = removing-stdint.h-include.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += LDFLAGS="-lintl /usr/openwin/lib/libXext.so"

CONFIGURE_ENV  = PKG_CONFIG_PATH=/opt/csw/X11/lib/pkgconfig

post-extract-modulated:
	@echo WORKSRC=$(WORKSRC)
	@echo post-extract-modulated
	find $(WORKSRC) -type f | xargs -I _ /opt/csw/bin/dos2unix _ _
	@$(MAKECOOKIE)

#post-extract:
#	@echo WORKSRC=$(WORKSRC)
#	@echo post-extract

TEST_SCRIPTS =

include gar/category.mk

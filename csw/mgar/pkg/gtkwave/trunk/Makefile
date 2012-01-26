NAME = gtkwave
VERSION = 3.2.3
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_BASE_PKGS = CSWtofrodos

GARCOMPILER = GNU

RUNTIME_DEP_PKGS  = CSWfconfig
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWtcl
RUNTIME_DEP_PKGS += CSWzlib

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

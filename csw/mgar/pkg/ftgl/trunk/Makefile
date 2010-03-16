GARNAME = ftgl
GARVERSION = 2.1.3-rc5
CATEGORIES = lib

DESCRIPTION = Library that uses Freetype2 to simplify rendering fonts in OpenGL applications
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

WORKSRC = $(WORKDIR)/$(GARNAME)-2.1.3~rc5

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

NOISAEXEC = 1
NOISALIST = 1
BUILD64 = 1

# Remove after rebuild of CSWmesa against OpenCSW X11
EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so.0

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --with-gl-inc=$(includedir)
CONFIGURE_ARGS += --with-gl-lib=$(libdir)

include gar/category.mk

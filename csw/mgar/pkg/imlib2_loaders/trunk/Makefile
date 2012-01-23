NAME = imlib2_loaders
VERSION = 1.4.3
CATEGORIES = lib

DESCRIPTION = Imlib 2 image loaders for XCF, EDB and EET

define BLURB
  The XCF loader cannot be packaged together with Imlib 2 because Imlib 2
  is distributed under the BSD license, whereas the XCF loader is using
  elements of the Gimp's (www.gimp.org) codebase, which is distributed
  under the GPL. The XCF loader therefore is GPL'd as well.
  2 other loaders are here too: EDB and EET
endef

SF_PROJ = enlightenment
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# TBD:
# - libeet missing
# - libedb missing

PACKAGES = CSWimlib2loaders
CATALOGNAME = imlib2_loaders

DEP_PKGS = CSWimlib2

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

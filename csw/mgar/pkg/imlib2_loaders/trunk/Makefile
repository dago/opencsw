NAME = imlib2_loaders
VERSION = 1.4.5 lib
GARTYPE = v2

DESCRIPTION = Imlib 2 image loaders for XCF, EDB and EET

define BLURB
  The XCF loader cannot be packaged together with Imlib 2 because Imlib 2
  is distributed under the BSD license, whereas the XCF loader is using
  elements of the Gimp's (www.gimp.org) codebase, which is distributed
  under the GPL. The XCF loader therefore is GPL'd as well.
  2 other loaders are here too: EDB and EECTET
endef

SF_PROJ = enlightenment
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VBUILD_DEP_PKGS += CSWlibimlib2-dev

PACKAGES = CSWlibimlib2-loaders
SPKG_DESC_CSWlibimlib2-loaders = Imlib2 loaders for ani, ico and scf
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibimlib2-loaders += CSWlibimlib2-1
OBSOLETED_BY_CSWlibimlib2-loaders += CSWimlib2loaders
CATALOGNAME_CSWimlib2loaders = imlib2_loaders_stub

EXTRA_LINKER_FLAGS += -lImlib2

# TBD:
# - libeet missing
# - libedb missing

BUILD64_LIBS_ONLY = 1

include gar/category.mk

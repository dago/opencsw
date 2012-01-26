NAME = liblbxutil
VERSION = 1.0.1
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = LBX utilities library from modular X.org.
define BLURB
  LBX (Low Bandwidth X) is an X server extension which performs compression and caching on the X protocol to improve the performance of X over low-bandwidth, high-latency links.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWliblbxutil CSWliblbxutildevel

CATALOGNAME_CSWliblbxutil = liblbxutil
CATALOGNAME_CSWliblbxutildevel = liblbxutil_devel

SPKG_DESC_CSWliblbxutil = $(DESCRIPTION)
SPKG_DESC_CSWliblbxutildevel = $(DESCRIPTION) development files

RUNTIME_DEP_PKGS_CSWliblbxutil      = CSWzlib
RUNTIME_DEP_PKGS_CSWliblbxutildevel = CSWliblbxutil

PKGFILES_CSWliblbxutildevel  = $(PKGFILES_DEVEL)

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include gar/category.mk

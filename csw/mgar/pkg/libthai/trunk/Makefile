NAME = libthai
VERSION = 0.1.12
CATEGORIES = lib

DESCRIPTION = Thai language support routines
define BLURB
  LibThai is a set of Thai language support routines aimed to ease
  developers tasks to incorporate Thai language support in their applications.
  It includes important Thai-specific functions e.g. word breaking, input
  and output methods as well as basic character and string supports.
  LibThai is an Open Source and collaborative effort initiated by
  Thai Linux Working Group and opened for all contributors.
endef

MASTER_SITES = http://linux.thai.net/pub/thailinux/software/libthai/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Remove-unknown-compiler-macro.patch

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=34448
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibthai CSWlibthaidevel

CATALOGNAME_CSWlibthai = libthai
CATALOGNAME_CSWlibthaidevel = libthai_devel

SPKG_DESC_CSWlibthai = Thai language support routines
SPKG_DESC_CSWlibthaidevel = Thai language support routines development files

SPKG_SOURCEURL = http://linux.thai.net/projects/libthai/

RUNTIME_DEP_PKGS_CSWlibthai = CSWlibdatrie
RUNTIME_DEP_PKGS_CSWlibthaidevel = CSWlibthai
PREREQUISUITE_PKGS = $(RUNTIME_DEP_PKGS_CSWlibthai)

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibthaidevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibthaidevel += $(docdir)/.*

include gar/category.mk

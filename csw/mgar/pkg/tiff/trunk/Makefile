NAME    = tiff
VERSION = 4.0.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Lib and tools for Tag Image File Format
define BLURB
endef

MASTER_SITES =  http://download.osgeo.org/libtiff/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Keep-norunpath-during-linkage.patch

VENDOR_URL = http://www.remotesensing.org/libtiff/

LICEGARCOMPILER = GCC4CENSE = COPYRIGHT

PACKAGES = CSWtiff
SPKG_DESC_CSWtiff += Tools for Tag Image File Format manipulation
PKGFILES_CSWtiff += $(bindir)/.*
PKGFILES_CSWtiff += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWt5
RUNTIME_DEP_PKGS_CSWtiff += CSWfreeglut
RUNTIME_DEP_PKGS_CSWtiff += CSWmesa

PACKAGES += CSWlibtiff5
SPKG_DESC_CSWlibtiff5 = Tag Image File Format library for C, libtiff.so.5
PKGFILES_CSWlibtiff5 += $(call pkgfiles_lib,libtiff.so.5)
RUNTIME_DEP_PKGS_CSWlibtiff5 += CSWlibjbig2
RUNTIME_DEP_PKGS_CSWlibtiff5 += CSWliblzma5
RUNTIME_DEP_PKGS_CSWlibtiff5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtiff5 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibtiff5 += CSWlibz1

PACKAGES += CSWlibtiffxx5
SPKG_DESC_CSWlibtiffxx5 = Tag Image File Format library for C++, libtiffcxx.so.5
PKGFILES_CSWlibtiffxx5 += $(call pkgfiles_lib,libtiffxx.so.5)
RUNTIME_DEP_PKGS_CSWlibtiffxx5 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibtiffxx5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtiffxx5 += CSWlibstdc++6x3 += CSWlibtiff3

PACKAGES += CSWlibtiff-dev
SPKG_DESC_CSWlibtiff-dev += Development file5 and libtiffxx.so.5
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtiff-dev += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibtiff-dev += CSWlibtiffxx5

# Ensure linking against the currently built lib and not the existing one
# (for libtiffxx)
EXTRA_LD_OPTIONS += -L$(abspath $(WORKSRC))/libtiff/.libsAGS += -norunpath

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(docdir)/tiff
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-cxx
CONenable-maintainer-mode

include gar/category.mk

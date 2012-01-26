NAME = tiff
VERSION = 3.9.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Lib and tools for Tag Image File Format
define BLURB
endef

MASTER_SITES =  http://download.osgeo.org/libtiff/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Keep-norunpath-during-linkage.patch

VENDOR_URL = http://www.remotesensing.org/libtiff/

LICENSE = COPYRIGHT

PACKAGES = CSWtiff
SPKG_DESC_CSWtiff += Tools for Tag Image File Format manipulation
PKGFILES_CSWtiff += $(bindir)/.*
PKGFILES_CSWtiff += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWtiff += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWtiff += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWtiff += CSWjbigkit
RUNTIME_DEP_PKGS_CSWtiff += CSWfreeglut
RUNTIME_DEP_PKGS_CSWtiff += CSWmesa
RUNTIME_DEP_PKGS_CSWtiff += CSWlibz1

# There are legacy packages dependencing on CSWtiff who have not a SONAME binding and
# require libtiff.so to be available
RUNTIME_DEP_PKGS_CSWtiff += CSWlibtiff-dev
CHECKPKG_OVERRIDES_CSWtiff += surplus-dependency|CSWlibtiff-dev

PACKAGES += CSWlibtiff3
SPKG_DESC_CSWlibtiff3 = Tag Image File Format library for C, libtiff.so.3
PKGFILES_CSWlibtiff3 += $(call pkgfiles_lib,libtiff.so.3)
RUNTIME_DEP_PKGS_CSWlibtiff3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibtiff3 += CSWjbigkit
RUNTIME_DEP_PKGS_CSWlibtiff3 += CSWlibz1

PACKAGES += CSWlibtiffxx3
SPKG_DESC_CSWlibtiffxx3 = Tag Image File Format library for C++, libtiffcxx.so.3
PKGFILES_CSWlibtiffxx3 += $(call pkgfiles_lib,libtiffxx.so.3)
RUNTIME_DEP_PKGS_CSWlibtiffxx3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibtiffxx3 += CSWjbigkit
RUNTIME_DEP_PKGS_CSWlibtiffxx3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibtiffxx3 += CSWlibtiff3

PACKAGES += CSWlibtiff-dev
SPKG_DESC_CSWlibtiff-dev += Development files for libtiff.so.3 and libtiffxx.so.3
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtiff-dev += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibtiff-dev += CSWlibtiffxx3

# There are docs only
CHECKPKG_OVERRIDES_CSWlibtiff-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/tiff/ChangeLog
CHECKPKG_OVERRIDES_CSWlibtiff-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/tiff/html/build.html

EXTRA_LINKER_FLAGS += -norunpath

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(docdir)/tiff
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --with-zlib-include-dir=$(includedir)
CONFIGURE_ARGS += --with-zlib-lib-dir=$(libdir)
CONFIGURE_ARGS += --with-jpeg-include-dir=$(includedir)
CONFIGURE_ARGS += --with-jpeg-lib-dir=$(libdir)
CONFIGURE_ARGS += --with-jbig-include-dir=$(includedir)
CONFIGURE_ARGS += --with-jbig-lib-dir=$(libdir)

include gar/category.mk

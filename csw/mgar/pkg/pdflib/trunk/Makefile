# $Id$
NAME = pdflib
VERSION = 7.0.5
CATEGORIES = lib

DESCRIPTION = Toolbox for generating and manipulating files in PDF
define BLURB
endef

MASTER_SITES = http://www.pdflib.com/binaries/PDFlib/705/
DISTNAME = PDFlib-Lite-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.pdflib.com/products/
LICENSE = doc/PDFlib-terms-and-conditions.pdf

PACKAGES += CSWlibpdf6
CATALOGNAME_CSWlibpdf6 = libpdf6
PKGFILES_CSWlibpdf6 += $(call baseisadirs,$(libdir),libpdf\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibpdf6 += Toolbox for generating and manipulating files in PDF, libpdf.so.6
RUNTIME_DEP_PKGS_CSWpdflib += CSWlibpdf6

PACKAGES += CSWlibpdf-java0
CATALOGNAME_CSWlibpdf-java0 = libpdf_java0
PKGFILES_CSWlibpdf-java0 += $(call baseisadirs,$(libdir),libpdf_java\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpdf-java0 += Toolbox for generating and manipulating files in PDF, libpdf_java.so.0
RUNTIME_DEP_PKGS_CSWpdflib += CSWlibpdf-java0

PACKAGES += CSWpdflib-devel
CATALOGNAME_CSWpdflib-devel = pdflib_devel
PKGFILES_CSWpdflib-devel = $(PKGFILES_DEVEL)
SPKG_DESC_CSWpdflib-devel = Development files for PDFlib
RUNTIME_DEP_PKGS_CSWpdflib-devel += CSWlibpdf6
RUNTIME_DEP_PKGS_CSWpdflib-devel += CSWlibpdf-java0

PACKAGES += CSWpdflib-utils
CATALOGNAME_CSWpdflib-utils = pdflib_utils
PKGFILES_CSWpdflib-utils += $(bindir)/pdfimage
PKGFILES_CSWpdflib-utils += $(bindir)/text2pdf
SPKG_DESC_CSWpdflib-utils = PDFlib utilities

# Do not force addition of /opt/csw/include before local includes or CSW libtiff
# includes will break compilation.
CPPFLAGS =
EXTRA_CFLAGS = -I/opt/csw/include

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-icu
CONFIGURE_ARGS += --enable-large_files
CONFIGURE_ARGS += --with-py=$(prefix)
CONFIGURE_ARGS += --with-pyincl=$(includedir)/python2.6
CONFIGURE_ARGS += --with-ruby=$(prefix)
CONFIGURE_ARGS += --with-rubyincl=$(libdir)/ruby/1.8/sparc-solaris2.9

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

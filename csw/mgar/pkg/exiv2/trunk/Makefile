NAME = exiv2
VERSION = 0.23
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Image metadata library and tools
define BLURB
  Exiv2 is a C++ library and a command line utility to manage image metadata.
  It provides fast and easy read and write access to the Exif, IPTC and XMP metadata
  of images in various formats. Exiv2 is available as free software and with a
  commercial license, and is used in many projects.
endef

MASTER_SITES = http://www.exiv2.org/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

BUILD_DEP_PKGS += CSWlibexpat-dev

PATCHFILES += 0002-fix-test-flag-config.mk.in.patch
# Patches for Sun-Studio Compiler
# PATCHFILES += 0001-Remove-unknown-flag-to-Sun-Studio.patch
# PATCHFILES += 0002-fix-depend-flag-config.mk.in.patch
# PATCHFILES += 0003-type-cast-basicio.cpp.patch
# PATCHFILES += 0004-rsc-remove-error.cpp.patch
# PATCHFILES += 0005-include-XML_Node.cpp.patch
# PATCHFILES += 0006-include-basicio.cpp.patch
# PATCHFILES += 0006-include-bmpimage.cpp.patch
# PATCHFILES += 0006-include-canonmn.cpp.patch
# PATCHFILES += 0006-include-convert.cpp.patch
# PATCHFILES += 0006-include-cr2image.cpp.patch
# PATCHFILES += 0006-include-dataset.cpp.patch
# PATCHFILES += 0006-include-easyaccess.cpp.patch
# PATCHFILES += 0006-include-epsimage.cpp.patch
# PATCHFILES += 0006-include-futils.cpp.patch
# PATCHFILES += 0006-include-gifimage.cpp.patch
# PATCHFILES += 0006-include-jp2image.cpp.patch
# PATCHFILES += 0006-include-jpgimage.cpp.patch
# PATCHFILES += 0006-include-makernote.cpp.patch
# PATCHFILES += 0006-include-mrwimage.cpp.patch
# PATCHFILES += 0006-include-pgfimage.cpp.patch
# PATCHFILES += 0006-include-pngchunk.cpp.patch
# PATCHFILES += 0006-include-pngimage.cpp.patch
# PATCHFILES += 0006-include-preview.cpp.patch
# PATCHFILES += 0006-include-proteries.cpp.patch
# PATCHFILES += 0006-include-psdimage.cpp.patch
# PATCHFILES += 0006-include-rafimage.cpp.patch
# PATCHFILES += 0006-include-tags.cpp.patch
# PATCHFILES += 0006-include-tgaimage.cpp.patch
# PATCHFILES += 0006-include-tiffcomposite.cpp.patch
# PATCHFILES += 0006-include-tiffvisitor.cpp.patch
# PATCHFILES += 0006-include-types.cpp.patch
# PATCHFILES += 0006-include-value.cpp.patch

GARCOMPILER = GCC4 # SOS12U3

PACKAGES += CSWlibexiv2-12
CATALOGNAME_CSWlibexiv2-12 = libexiv2_12
PKGFILES_CSWlibexiv2-12 += $(call baseisadirs,$(libdir),libexiv2\.so\.12\.0\.0)
PKGFILES_CSWlibexiv2-12 += $(call baseisadirs,$(libdir),libexiv2\.so\.12(\.\d+)*)
SPKG_DESC_CSWlibexiv2-12 += $(DESCRIPTION), libexiv2.so.12
RUNTIME_DEP_PKGS_CSWlibexiv2-12 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibexiv2-12 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibexiv2-12 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibexiv2-12 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibexiv2-12 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibexiv2-12 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibexiv2-12 += file-with-bad-content|/usr/local|root/opt/csw/lib/libexiv2.so.12.0.0


PACKAGES += CSWexiv2-dev
CATALOGNAME_CSWexiv2-dev = exiv2_dev
SPKG_DESC_CSWexiv2-dev += $(DESCRIPTION), development files
PKGFILES_CSWexiv2-dev += /opt/csw/lib/libexiv2.so
PKGFILES_CSWexiv2-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWexiv2-dev += CSWlibexiv2-12

PACKAGES += CSWexiv2
CATALOGNAME_CSWexiv2 = exiv2
SPKG_DESC_CSWexiv2 += $(DESCRIPTION), tools
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWexiv2 += CSWlibexiv2-12
CHECKPKG_OVERRIDES_CSWexiv2 += file-with-bad-content|/usr/local|root/opt/csw/bin/exiv2

# BUILD64_LIBS_ONLY = 1

# Options for Sun-Studio-Compiler
# see: http://solaris.bionicmutton.org/hg/kde4-specs-460/file/26c2cab27bbe/specs/patches/exiv2/0.14/README.STUDIO12
# EXTRA_CXXFLAGS = -features=anachronisms,except,rtti,export,extensions,nestedaccess,tmplife,tmplrefstatic -library=stlport4 
# EXTRA_LINKER_FLAGS += -library=stlport4
EXTRA_LINKER_FLAGS += -lintl

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)
# Sun Studio doesn't unerstand g++ features
# CONFIGURE_ARGS += --disable-visibility

include gar/category.mk

PATH:=/opt/csw/gnu:$(PATH)

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
PATCHFILES += 0001-Remove-unknown-flag-to-Sun-Studio.patch
PATCHFILES += 0002-fix-depend-flag-config.mk.in.patch
PATCHFILES += 0003-type-cast-basicio.cpp.patch
PATCHFILES += 0004-rsc-remove-error.cpp.patch

GARCOMPILER = SOS12U3

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1

# see: http://solaris.bionicmutton.org/hg/kde4-specs-460/file/26c2cab27bbe/specs/patches/exiv2/0.14/README.STUDIO12
EXTRA_CXXFLAGS = -features=anachronisms,except,rtti,export,extensions,nestedaccess,tmplife,tmplrefstatic

CONFIGURE_ARGS = $(DIRPATHS)

# Sun Studio doesn't unerstand g++ features
CONFIGURE_ARGS += --disable-visibility

include gar/category.mk

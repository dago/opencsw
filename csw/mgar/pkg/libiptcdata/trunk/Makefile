NAME = libiptcdata
VERSION = 1.0.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = IPTC Tag Parsing Library
define BLURB
   libiptcdata is a library for manipulating the International Press
   Telecommunications Council (IPTC) metadata stored within multimedia
   files such as images.  The library provides routines for parsing,
   viewing, modifying, and saving this metadata.
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://libiptcdata.sourceforge.net

LICENSE = COPYING

PACKAGES = CSWlibiptcdata CSWlibiptcdatadevel CSWlibiptcdatadoc
#PACKAGES += CSWpy-libiptcdata
CATALOGNAME_CSWlibiptcdata = libiptcdata
CATALOGNAME_CSWlibiptcdatadevel = libiptcdata_devel
CATALOGNAME_CSWlibiptcdatadoc = libiptcdata_doc
#CATALOGNAME_CSWpy-libiptcdata = py_libiptcdata
SPKG_DESC_CSWlibiptcdata = $(DESCRIPTION)
SPKG_DESC_CSWlibiptcdatadevel = $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibiptcdatadoc = $(DESCRIPTION) - documentation package
#SPKG_DESC_CSWpy-libiptcdata = $(DESCRIPTION) - Python bindings

RUNTIME_DEP_PKGS_CSWlibiptcdata = CSWggettextrt CSWiconv
RUNTIME_DEP_PKGS_CSWlibiptcdatadevel = CSWlibiptcdata
RUNTIME_DEP_PKGS_CSWlibiptcdatadoc = CSWlibiptcdata
#RUNTIME_DEP_PKGS_CSWpy-libiptcdata = CSWlibiptcdata CSWpython

PKGFILES_CSWlibiptcdatadevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibiptcdatadoc = $(sharedstatedir)/gtk-doc/.*
#PKGFILES_CSWpy-libiptcdata = $(libdir).*/python/site-packages/.*

ARCHALL_CSWlibiptcdatadoc = 1

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=130582
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
# Python isn't 64-bit yet
#CONFIGURE_ARGS += --enable-python
CONFIGURE_ARGS += --enable-gtk-doc

include gar/category.mk

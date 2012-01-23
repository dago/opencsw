NAME = libgdiplus
VERSION = 2.6
CATEGORIES = lib

DESCRIPTION = Mono library that provide a GDI+ comptible API
define BLURB
  Mono is a comprehensive open source development platform based on the .NET
  framework that allows developers to build Linux and cross-platform
  applications with unprecedented productivity. Mono's .NET implementation is
  based on the ECMA standards for C# and  the Common Language Infrastructure.
endef

MASTER_SITES = http://ftp.novell.com/pub/mono/sources/mono/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2 

#PATCHFILES += Makefile.in.patch
#PATCHFILES += configure.patch
#PATCHFILES += metafile.c.patch
#PATCHFILES += win32structs.h.patch

RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWglib2
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWlibexif
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWpango
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWpng
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWtiff
RUNTIME_DEP_PKGS_CSWlibgdiplus += CSWgcc4corert

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-pango

GARCOMPILER = GCC4
include gar/category.mk

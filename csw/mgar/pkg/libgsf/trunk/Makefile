NAME = libgsf
VERSION = 1.14.21
CATEGORIES = gnome

DESCRIPTION = GNOME Structured File Library
define BLURB
	The GNOME Structured File Library (GSF) is an I/O abstraction for
	reading/writing compound files. GSF is released under the GNU Lesser
	General Public License (GNU LGPL), which allows for flexible licensing of
	client applications. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# New glib is Solaris 10 only
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWgnulinks
BUILD_DEP_PKGS += CSWgtk-doc
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWlibxml2devel

RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgsf += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgio2-0-0

# No package split yet
CHECKPKG_OVERRIDES_CSWlibgsf += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWlibgsf += shared-lib-pkgname-mismatch

# The -L/opt/csw/lib is too early and disturbs the build with the installed libgsf
LINKER_FLAGS =

CONFIGURE_ARGS += $(DIRPATHS)

# There are link errors on newly built gnomemodule.la, disable for now
CONFIGURE_ARGS += --without-python

# Missing 64-bit libs:
# libgnomevfs-2.so libgconf-2.so libbonobo-2.so libbonobo-activation.so
BUILD64 = 1

STRIP_LIBTOOL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-install-isa-sparcv8plus:
	@cp -p $(FILEDIR)/libgsf-1.so.1.9.1.s $(INSTALLISADIR)$(libdir)/libgsf-1.so.1
	@cp -p $(FILEDIR)/libgsf-gnome-1.so.1.9.1.s $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1

post-install-isa-pentium_pro:
	@cp -p $(FILEDIR)/libgsf-1.so.1.9.1.i $(INSTALLISADIR)$(libdir)/libgsf-1.so.1
	@cp -p $(FILEDIR)/libgsf-gnome-1.so.1.9.1.i $(INSTALLISADIR)$(libdir)/libgsf-gnome-1.so.1

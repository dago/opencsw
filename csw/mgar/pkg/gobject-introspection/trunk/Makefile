NAME = gobject-introspection
VERSION = 1.34.2
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Package for extending API for GObject based libraries
define BLURB
	GObject-introspection is a package which will collect and extend the API
	metadata for GObject based libraries. The main motivation of this work is to
	centralize all introspection information required to write a language binding.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.xz

# PATCHFILES += 0001-Use-named-union.patch

VENDOR_URL = http://live.gnome.org/GObjectIntrospection

GARCOMPILER = GCC4

# the warn tests fail, because it reports more warnings than expected
SKIPTEST ?= 1

BUILD_DEP_PKGS += CSWbison
BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWgtk-doc


PACKAGES += CSWlibgirepository1-0-1
CATALOGNAME_CSWlibgirepository1-0-1 = libgirepository1_0_1
PKGFILES_CSWlibgirepository1-0-1 += $(call baseisadirs,$(libdir),libgirepository-1\.0\.so\.1\.0\.0)
PKGFILES_CSWlibgirepository1-0-1 += $(call baseisadirs,$(libdir),libgirepository-1\.0\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgirepository1-0-1 += $(DESCRIPTION), libgirepository-1.0.so.1
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibffi4
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibglib2-0-0

PACKAGES += CSWgobject-introspection-dev
CATALOGNAME_CSWgobject-introspection-dev = gobject_introspection_dev
SPKG_DESC_CSWgobject-introspection-dev += $(DESCRIPTION), development files
PKGFILES_CSWgobject-introspection-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWgobject-introspection-dev += /opt/csw/lib/libgirepository-1.0.so
RUNTIME_DEP_PKGS_CSWgobject-introspection-dev += CSWlibgirepository1-0-1
RUNTIME_DEP_PKGS_CSWgobject-introspection-dev += CSWgobject-introspection

PACKAGES += CSWgobject-introspection
SPKG_DESC_CSWgobject-introspection += $(DESCRIPTION), bins
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgirepository1-0-1
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWpython
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibffi4
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibglib2-0-0

# These are just docs
CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/local|root/opt/csw/share/gir-1.0/GLib-2.0.gir
CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/share|root/opt/csw/share/gir-1.0/Gio-2.0.gir
CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/share|root/opt/csw/lib/gobject-introspection/giscanner/transformer.py

# Python isn't 64-bit yet
#BUILD64 = 1

PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

BUILD_OVERRIDE_VARS = V
BUILD_OVERRIDE_VARS_V = 1

# this has not helped, I have added -lgmodule-2.0 in glib-2.0.pc (dirty hack)
# EXTRA_LINKER_FLAGS += -lgmodule-2.0

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --enable-gtk-doc

include gar/category.mk

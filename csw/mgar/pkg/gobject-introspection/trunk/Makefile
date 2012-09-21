NAME = gobject-introspection
VERSION = 1.29.17
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Package for extending API for GObject based libraries
define BLURB
	GObject-introspection is a package which will collect and extend the API
	metadata for GObject based libraries. The main motivation of this work is to
	centralize all introspection information required to write a language binding.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Use-named-union.patch

VENDOR_URL = http://live.gnome.org/GObjectIntrospection

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
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
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgirepository1-0-1 += CSWlibintl8
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

PACKAGES += CSWgobject-introspection
SPKG_DESC_CSWgobject-introspection += $(DESCRIPTION), bins
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgirepository1-0-1
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWpython
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibffi4
RUNTIME_DEP_PKGS_CSWgobject-introspection += CSWlibglib2-0-0

CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/share|root/opt/csw/share/gir-1.0/Gio-2.0.gir
# CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/share|root/opt/csw/lib/gobject-introspection/giscanner/transformer.pyc
CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/share|root/opt/csw/lib/gobject-introspection/giscanner/transformer.py
# CHECKPKG_OVERRIDES_CSWgobject-introspection += file-with-bad-content|/usr/share|root/opt/csw/lib/gobject-introspection/giscanner/transformer.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/__init__.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/__init__.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/annotationmain.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/annotationmain.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/annotationparser.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/annotationparser.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/ast.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/ast.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/cachestore.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/cachestore.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/codegen.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/codegen.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/config.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/config.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/dumper.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/dumper.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/gdumpparser.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/gdumpparser.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girparser.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girparser.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girwriter.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girwriter.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/introspectablepass.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/introspectablepass.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/libtoolimporter.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/libtoolimporter.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/maintransformer.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/maintransformer.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/message.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/message.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/odict.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/odict.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/scannermain.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/scannermain.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/shlibs.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/shlibs.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/sourcescanner.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/sourcescanner.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/testcodegen.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/testcodegen.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/transformer.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/transformer.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/utils.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/utils.pyo
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/xmlwriter.pyc
# CHECKPKG_OVERRIDES_CSWgobject-introspection += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/xmlwriter.pyo

# PACKAGES = CSWgobjintrospect
# CATALOGNAME_CSWgobjintrospect = gobj_introspect
# SPKG_DESC_CSWgobjintrospect = $(DESCRIPTION)
# RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWggettextrt
# RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWglib2
# RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWlibffi
# RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWpython

# PACKAGES += CSWgobjintrospectdev
# CATALOGNAME_CSWgobjintrospectdev = gobj_introspect_dev
# SPKG_DESC_CSWgobjintrospectdev = $(DESCRIPTION) - developer package
# PKGFILES_CSWgobjintrospectdev = $(PKGFILES_DEVEL)
# RUNTIME_DEP_PKGS_CSWgobjintrospectdev += CSWgobjintrospect

# Python isn't 64-bit yet
#BUILD64 = 1

PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

BUILD_OVERRIDE_VARS = V
BUILD_OVERRIDE_VARS_V = 1

EXTRA_LINKER_FLAGS += -lgmodule-2.0

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --enable-gtk-doc

include gar/category.mk

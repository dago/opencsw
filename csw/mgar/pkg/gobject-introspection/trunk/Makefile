NAME = gobject-introspection
VERSION = 0.10.8
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

PACKAGING_PLATFORMS = solaris10-sparc soalris10-i386

BUILD_DEP_PKGS += CSWbison
BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWgtk-doc

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

BUILD_OVERRIDE_VARS = V
BUILD_OVERRIDE_VARS_V = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --enable-gtk-doc

include gar/category.mk

NAME = gobject-introspection
VERSION = 0.6.7
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

PACKAGES = CSWgobjintrospect CSWgobjintrospectdev
CATALOGNAME_CSWgobjintrospect = gobj_introspect
CATALOGNAME_CSWgobjintrospectdev = gobj_introspect_dev

SPKG_DESC_CSWgobjintrospect = $(DESCRIPTION)
SPKG_DESC_CSWgobjintrospectdev = $(DESCRIPTION) - developer package

PKGFILES_CSWgobjintrospectdev = $(PKGFILES_DEVEL)

ARCHALL_CSWgobjintrospectdoc = 1

BUILD_DEP_PKGS += CSWbison CSWlibffi

RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWglib2
RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWlibffi
RUNTIME_DEP_PKGS_CSWgobjintrospect += CSWpython
RUNTIME_DEP_PKGS_CSWgobjintrospectdev += CSWgobjintrospect

CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/__init__.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/__init__.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/annotationparser.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/annotationparser.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/ast.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/ast.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/cachestore.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/cachestore.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/config.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/config.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/dumper.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/dumper.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girparser.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girparser.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girwriter.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/girwriter.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/glibast.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/glibast.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/glibtransformer.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/glibtransformer.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/libtoolimporter.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/libtoolimporter.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/minixpath.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/minixpath.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/odict.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/odict.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/scannermain.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/scannermain.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/shlibs.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/shlibs.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/sourcescanner.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/sourcescanner.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/transformer.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/transformer.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/utils.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/utils.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/xmlwriter.pyc
CHECKPKG_OVERRIDES_CSWgobjintrospect += discouraged-path-in-pkgmap|/opt/csw/lib/gobject-introspection/giscanner/xmlwriter.pyo
CHECKPKG_OVERRIDES_CSWgobjintrospectdev += surplus-dependency|CSWgobjintrospect

PATCHFILES += gobject-introspection-01-ginvoke.diff
PATCHFILES += gobject-introspection-02-glib-compilation.diff
PATCHFILES += gobject-introspection-03-ginfo.diff
PATCHFILES += gobject-introspection-04-big-ending.diff
PATCHFILES += sunstudio.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GObjectIntrospection

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

#NOISAEXEC = 1
# Python isn't 64-bit yet
#BUILD64 = 1

BUILD_OVERRIDE_VARS = V
BUILD_OVERRIDE_VARS_V = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --enable-gtk-doc

#SHELL = /opt/csw/bin/bash

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check 

include gar/category.mk

pre-configure-modulated:
	( cd $(WORKSRC); 						\
		rm -f m4/lt~obsolete.m4	;	\
		rm -f m4/ltoptions.m4 	;	\
		rm -f m4/libtool.m4 		;	\
		rm -f m4/ltsugar.m4 		;	\
		rm -f m4/ltversion.m4 	;	\
		libtoolize --copy --force	;	\
		aclocal -I m4	;	\
		autoheader	;	\
		automake -a -c -f	;	\
		autoconf	;	\
	)
	$(MAKECOOKIE)

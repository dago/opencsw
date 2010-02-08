GARNAME = gobject-introspection
GARVERSION = 0.6.7
CATEGORIES = gnome

DESCRIPTION = Package for extending API for GObject based libraries
define BLURB
	GObject-introspection is a package which will collect and extend the API
	metadata for GObject based libraries. The main motivation of this work is to
	centralize all introspection information required to write a language binding.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

#PACKAGES = CSWgobjectintrospection CSWgobjectintrospectiondevel CSWjsonglibdoc
#CATALOGNAME_CSWgobjectintrospection = gobject_introspection
#CATALOGNAME_CSWgobjectintrospectiondevel = gobject_introspection_devel
#CATALOGNAME_CSWgobjectintrospectiondoc = gobject_introspection_doc

#PKGFILES_CSWgobjectintrospectiondevel = $(PKGFILES_DEVEL)
#PKGFILES_CSWgobjectintrospectiondoc = $(sharedstatedir)/gtk-doc/.*

#ARCHALL_CSWgobjectintrospectiondoc = 1

BUILD_DEP_PKGS += CSWbison CSWlibffi

PATCHFILES += gobject-introspection-01-ginvoke.diff
PATCHFILES += gobject-introspection-02-glib-compilation.diff
PATCHFILES += gobject-introspection-03-ginfo.diff
PATCHFILES += gobject-introspection-04-big-ending.diff
PATCHFILES += sunstudio.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GObjectIntrospection

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

NOISAEXEC = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#SHELL = /opt/csw/bin/bash

CONFIGURE_ARGS = $(DIRPATHS)

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

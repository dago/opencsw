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

PREREQUISITE_PKGS += CSWbison CSWlibffi

REQUIRED_PKGS += CSWgcc4corert

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GObjectIntrospection

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

NO_ISAEXEC = 1
NOISALIST = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

SHELL = /opt/csw/bin/bash

#PKGFILES_CSWgobjectintrospectiondevel = $(PKGFILES_DEVEL)
#PKGFILES_CSWgobjectintrospectiondoc = $(sharedstatedir)/gtk-doc/.*

#ARCHALL_CSWgobjectintrospectiondoc = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

#PATH := /opt/csw/gnu:$(PATH)

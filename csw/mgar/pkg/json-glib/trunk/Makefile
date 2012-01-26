NAME = json-glib
VERSION = 0.9.2
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Library providing serialization and deserialization support for the JSON format
define BLURB
	JSON-GLib is a C library based on GLib and released under the terms of the
	GNU Lesser General Public License version 2.1. It provides a parser and a
	generator GObject classes and various wrappers for the complex data types
	employed by JSON, such as arrays and objects.

	JSON-GLib uses GLib native data types and the generic value container GValue
	for ease of development. It also provides integration with the GObject
	classes for direct serialization into, and deserialization from, JSON data
	streams. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWjson-glib CSWjson-glibdevel CSWjson-glibdoc
CATALOGNAME_CSWjson-glib = json_glib
CATALOGNAME_CSWjson-glibdevel = json_glib_devel
CATALOGNAME_CSWjson-glibdoc = json_glib_doc

SPKG_DESC_CSWjson-glib += Library providing serialization and deserialization support for the JSON format
SPKG_DESC_CSWjson-glibdevel += Library providing serialization and deserialization support for the JSON format develiper package
SPKG_DESC_CSWjson-glibdoc += Library providing serialization and deserialization support for the JSON format documentation

PKGFILES_CSWjson-glibdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWjson-glibdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWjson-glibdoc = 1

RUNTIME_DEP_PKGS_CSWjson-glib += CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWjson-glibdevel += CSWjson-glib
RUNTIME_DEP_PKGS_CSWjson-glibdoc += CSWjson-glib

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/JsonGlib

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

#NOISAEXEC = 1
#NOISALIST = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

SHELL = /opt/csw/bin/bash

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

#PATH := /opt/csw/gnu:$(PATH)

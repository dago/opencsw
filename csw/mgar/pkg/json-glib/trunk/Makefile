GARNAME = json-glib
GARVERSION = 0.9.2
CATEGORIES = gnome

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWjsonglib CSWjsonglibdevel CSWjsonglibdoc
CATALOGNAME_CSWjsonglib = json_glib
CATALOGNAME_CSWjsonglibdevel = json_glib_devel
CATALOGNAME_CSWjsonglibdoc = json_glib_doc

SPKG_DESC_CSWjsonglib += Library providing serialization and deserialization support for the JSON format
SPKG_DESC_CSWjsonglibdevel += Library providing serialization and deserialization support for the JSON format develiper package
SPKG_DESC_CSWjsonglibdoc += Library providing serialization and deserialization support for the JSON format documentation

#PREREQUISITE_PKGS += CSWlibxcbdevel CSWlibpthreadstubs CSWlibxaudevel
#PREREQUISITE_PKGS += CSWxproto CSWrenderproto CSWkbproto CSWpython-devel

#REQUIRED_PKGS += CSWbonobo2 CSWgconf2 CSWggettextrt CSWglib2 CSWgnomekeyring
#REQUIRED_PKGS += CSWgnomevfs2 CSWgtk2 CSWlibart CSWlibatk CSWlibbonoboui
#REQUIRED_PKGS += CSWlibcairo CSWlibglade2 CSWlibgnome CSWlibgnomecanvas
#REQUIRED_PKGS += CSWlibgnomeui CSWlibgoffice CSWlibgsf CSWlibpopt CSWlibxml2
#REQUIRED_PKGS += CSWorbit2 CSWpango CSWperl CSWzlib
REQUIRED_PKGS_CSWjsonglib += CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWjsonglibdevel += CSWjsonglib
REQUIRED_PKGS_CSWjsonglibdoc += CSWjsonglib

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/JsonGlib

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

PKGFILES_CSWjsonglibdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWjsonglibdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWjsonglibdoc = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

#PATH := /opt/csw/gnu:$(PATH)

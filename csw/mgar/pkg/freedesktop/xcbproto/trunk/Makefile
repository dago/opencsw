# $Id$

VERSION = 1.6
CATEGORIES = lib
PROTONAME = xcb-proto
NAME = $(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = XCB protocol descriptions (in XML)
define BLURB
  The xcb-proto package provides the XML-XCB (X C Bindings) protocol
  descriptions that libxcb uses to generate the majority of its code and API.
  We provide them separately from libxcb to allow reuse by other projects,
  such as additional language bindings, protocol dissectors, or
  documentation generators.

  Separation of XCB's transport and protocol layers simplifies both
  writing extensions and client-side support for extensions.
  By contrast, with the xlib infrastructure, client-side support for
  new extensions requires significant duplication of effort. With XCB and
  the XML-XCB protocol descriptions, client-side support for a new
  extension requires only an XML description of the extension--and not a
  single line of code.

  Python libraries: xcb-proto also contains language-independent Python
  libraries that are used to parse an XML description and create objects
  used by Python code generators in individual language bindings.
endef

MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES    = $(DISTNAME).tar.gz

PACKAGES = CSWxcbproto CSWpyxcbproto

CATALOGNAME_CSWxcbproto = xcbproto
CATALOGNAME_CSWpyxcbproto = py_xcbproto

BUILD_DEP_PKGS = CSWpython
RUNTIME_DEP_PKGS_CSWxcbproto = CSWx11common
RUNTIME_DEP_PKGS_CSWpyxcbproto = CSWxcbproto CSWpython

SPKG_DESC_CSWxcbproto = XCB protocol descriptions (in XML)
SPKG_DESC_CSWpyxcbproto = $(SPKG_DESC_CSWxcbproto) Python Bindings

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

PYTHON_PREFIX = $(BUILD_PREFIX)/lib/python/site-packages

PYCOMPILE = 1

PKGFILES_CSWpyxcbproto = .*\.py
ARCHALL_CSWpyxcbproto = 1

CHECKPKG_OVERRIDES_CSWpyxcbproto += surplus-dependency|CSWxcbproto
CHECKPKG_OVERRIDES_CSWxcbproto += surplus-dependency|CSWx11common
CHECKPKG_OVERRIDES_CSWpyxcbproto += pkgname-does-not-start-with-CSWpy-

EXTRA_MERGE_EXCLUDE_FILES = .*.py[co]

include gar/category.mk

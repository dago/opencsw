GARVERSION = 1.5
CATEGORIES = x11
PROTONAME = xcb-proto
GARNAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(GARVERSION)

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

MASTER_SITES = $(XCB_MASTER_SITES)
DISTFILES    = $(DISTNAME).tar.gz

PACKAGES = CSWx11xcbproto CSWpyx11xcbproto

CATALOGNAME_CSWx11xcbproto = x11_xcbproto
CATALOGNAME_CSWpyx11xcbproto = py_x11xcbproto

PREREQUISITE_PKGS = CSWpython
REQUIRED_PKGS_CSWxcbproto = CSWx11common
REQUIRED_PKGS_CSWpyxcbproto = CSWx11xcbproto CSWpython

SPKG_DESC_CSWx11xcbproto = XCB protocol descriptions (in XML)
SPKG_DESC_CSWpyx11xcbproto = XCB protocol descriptions (in XML) Python Bindings

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

PYTHON_PREFIX=$(BUILD_PREFIX)/lib/python/site-packages

EXTRA_PAX_ARGS = -s ',^.*/\(xcbgen/.*\.py\),.$(BUILD_PREFIX)/lib/python/site-packages/\1,'
EXTRA_PAX_ARGS += -s ',^\.$(libdir)/python.*,,'

PYCOMPILE = 1

PKGFILES_CSWpyx11xcbproto = .*\.py

include gar/category.mk

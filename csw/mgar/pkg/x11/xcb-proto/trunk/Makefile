GARNAME = xcb-proto
GARVERSION = 1.4

CATEGORIES = x11

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
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWxcbproto

PREREQUISITE_PKGS = CSWpython
REQUIRED_PKGS = CSWpython
REQUIRED_PKGS += CSWx11common

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk



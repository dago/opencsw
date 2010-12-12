# $Id$

VERSION = 1.6
CATEGORIES = x11
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

MASTER_SITES = $(XCB_MASTER_SITES)
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

include gar/category.mk

# This bit is probably somewhat objectionable, but it gets the job done.
post-merge:
	ginstall -m 755 -d $(PKGROOT)/opt/csw/lib
	if [ -d $(PKGROOT)$(prefix)/lib/python ]; then \
		gmv -v $(PKGROOT)$(prefix)/lib/python $(PKGROOT)/opt/csw/lib; \
	fi
	grm -fv $(PKGROOT)/opt/csw/lib/python/site-packages/xcbgen/*.py[co]
	@$(MAKECOOKIE)

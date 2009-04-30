GARNAME = libxcb
GARVERSION = 1.1
CATEGORIES = x11

DESCRIPTION = The XCB library
define BLURB
  The XCB library provides an interface to the X Window System protocol,
  designed to replace the Xlib interface
endef

MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS = CSWlibxaudevel CSWlibpthreadstubs CSWdoxygen
REQUIRED_PKGS_CSWlibxcb = CSWxcbproto CSWlibxau
PACKAGES = CSWlibxcb CSWlibxcbdevel CSWlibxcbdoc

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxcb      = The XCB library
SPKG_DESC_CSWlibxcbdevel = The XCB library development package
SPKG_DESC_CSWlibxcbdoc   = The XCB library documentation

CATALOGNAME_CSWlibxcb      = libxcb
CATALOGNAME_CSWlibxcbdevel = libxcb_dev
CATALOGNAME_CSWlibxcbdoc   = libxcb_doc

PKGFILES_CSWlibxcbdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxcbdoc   = $(PKGFILES_DOC)

REQUIRED_PKGS_CSWlibxcbdevel = CSWlibxcb
REQUIRED_PKGS_CSWlibxcb	     = CSWlibxau

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


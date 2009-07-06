GARNAME = libxcb
GARVERSION = 1.3
CATEGORIES = x11

DESCRIPTION = The XCB library
define BLURB
  The XCB library provides an interface to the X Window System protocol,
  designed to replace the Xlib interface
endef

MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS = CSWlibxaudevel CSWlibpthreadstubs CSWdoxygen CSWpython CSWxcbproto CSWgraphviz2
REQUIRED_PKGS_CSWlibxcb = CSWlibxau
PACKAGES = CSWlibxcb CSWlibxcbdevel CSWlibxcbdoc

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxcb      = The XCB library
SPKG_DESC_CSWlibxcbdevel = The XCB library development package
SPKG_DESC_CSWlibxcbdoc   = The XCB library documentation

CATALOGNAME_CSWlibxcb      = libxcb
CATALOGNAME_CSWlibxcbdevel = libxcb_devel
CATALOGNAME_CSWlibxcbdoc   = libxcb_doc

PKGFILES_CSWlibxcbdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxcbdoc   = $(PKGFILES_DOC)

REQUIRED_PKGS_CSWlibxcbdevel = CSWlibxcb
REQUIRED_PKGS_CSWlibxcb	     = CSWx11common CSWlibxau CSWlibxdmcp

ARCHALL_CSWlibxcbdoc = 1

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CFLAGS = -D__solaris__

include gar/category.mk

PATH := $(PATH):/opt/csw/graphviz2/bin

post-install-modulated:
	perl -pi -e 's/^(Cflags:.*)/\1 $(EXTRA_CFLAGS)/' $(DESTDIR)$(libdir)/pkgconfig/xcb.pc
	@$(MAKECOOKIE)

post-merge:
	ginstall -d $(PKGROOT)$(BUILD_PREFIX)/lib
	for lib in composite damage dpms glx record render res screensaver shape shm sync xevie xf86dri xfixes xinerama xprint xtest xv xvmc ; \
	do gln -sf libxcb-$${lib}.so.0.0.0 $(PKGROOT)$(BUILD_PREFIX)/lib/lbxcb-$${lib}.so.0 ; \
	gln -sf libxcb-$${lib}.so.0.0.0 $(PKGROOT)$(BUILD_PREFIX)/lib/lbxcb-$${lib}.so ; \
	done
	gln -sf libxcb-randr.so.1.0.0 $(PKGROOT)$(BUILD_PREFIX)/lib/lbxcb-randr.so.1
	gln -sf libxcb-randr.so.0.0.0 $(PKGROOT)$(BUILD_PREFIX)/lib/lbxcb-randr.so
	gln -sf libxcb.so.1.1.0 $(PKGROOT)$(BUILD_PREFIX)/lib/lbxcb.so.1
	gln -sf libxcb.so.1.1.0 $(PKGROOT)$(BUILD_PREFIX)/lib/lbxcb.so

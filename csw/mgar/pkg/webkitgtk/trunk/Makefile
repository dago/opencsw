# $Id$

USNAME		=	webkit
NAME		=	$(USNAME)gtk
VERSION		=	1.8.1
GARTYPE		=	v2
CATEGORIES	=	gnome

DESCRIPTION = WebKitGTK+ is the port of the portable web rendering engine WebKit to the GTK+ platform.
define BLURB
  WebKitGTK+ is the port of the portable web rendering engine WebKit to the
  GTK+ platform.
endef

MASTER_SITES	=	http://www.webkitgtk.org/releases/
DISTNAME		=	$(USNAME)-$(VERSION)
DISTFILES		=	$(DISTNAME).tar.xz
PATCHFILES		+=	0001-Fix-GLib-run-test.patch

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		+=	CSWgperf
BUILD_DEP_PKGS		+=	CSWlibglib2-dev

EXTRA_CONFIGURE_ENV	+=	GLIB_CFLAGS="-I$(includedir)/glib-2.0 -I$(libdir)/glib-2.0/include"
EXTRA_CONFIGURE_ENV	+=	GLIB_LIBS="-L$(libdir) -R$(libdir) -lglib-2.0"

CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_ARGS		+=	--with-gtk=2.0

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

include gar/category.mk

# pre-configure-modulated:
# 	@echo "executing $@"
# 	cd $(WORKSRC) && libtoolize
# 	cd $(WORKSRC) && aclocal -I Source/autotools
# 	cd $(WORKSRC) && automake -a
# 	cd $(WORKSRC) && autoconf
# 	$(MAKECOOKIE)

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done

# $Id$

NAME = libgnet
VERSION = 2.0.8
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Network library based on glib2
define BLURB
  GNet is a simple network library. It is written in C, object-oriented,
  and built upon GLib. It is intended to be easy to use and port.
endef

DISTNAME		=	gnet-$(VERSION)
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/gnet/2.0/
DISTFILES  = $(DISTNAME).tar.gz

# until the glib development package is installed on Solaris 9 we
# limit the scope:
PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev

RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibiconv2
RUNTIME_DEP_PKGS	+=	CSWlibintl8

CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER			=	GNU

include gar/category.mk

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

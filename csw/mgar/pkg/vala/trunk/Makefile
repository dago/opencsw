# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = vala
VERSION = 0.20.1
GARTYPE = v2

DESCRIPTION = Compiler for the GObject type system
define BLURB
  Vala is a new programming language that aims to bring modern programming
  language features to GNOME developers without imposing any additional
  runtime requirements and without using a different ABI compared to
  applications and libraries written in C.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.xz
GARCOMPILER = GNU

BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWlibxslt-dev
BUILD_DEP_PKGS += CSWpkgconfig

RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWpcre
RUNTIME_DEP_PKGS += CSWlibffi
RUNTIME_DEP_PKGS += CSWintltool
RUNTIME_DEP_PKGS += CSWlibxslt

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk


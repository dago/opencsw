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

RUNTIME_DEP_PKGS += CSWlibglib2-0-0
RUNTIME_DEP_PKGS += CSWpcre
RUNTIME_DEP_PKGS += CSWlibxslt
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS += CSWlibgobject2-0-0

CONFIGURE_ARGS = $(DIRPATHS)

# Will fail with "error: Package `GLib-2.0' not found in specified Vala API directories or GObject-Introspection GIR directories"
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWvala += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libvala-0.20.so
CHECKPKG_OVERRIDES_CSWvala += shared-lib-pkgname-mismatch|file=opt/csw/lib/libvala-0.20.so.0.0.0|soname=libvala-0.20.so.0|pkgname=CSWvala|expected=CSWlibvala0-20-0

include gar/category.mk


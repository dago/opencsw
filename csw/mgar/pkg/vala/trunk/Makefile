# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = vala
VERSION = 0.27.1
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

PACKAGES += CSWvala
SPKG_DESC_CSWvala = Compiler for the GObject type system
# PKGFILES is catchall for now
CHECKPKG_OVERRIDES_CSWvala += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libvala-0.28.so
CHECKPKG_OVERRIDES_CSWvala += shared-lib-pkgname-mismatch|file=opt/csw/lib/libvala-0.28.so.0.0.0|soname=libvala-0.28.so.0|pkgname=CSWvala|expected=CSWlibvala0-28-0
RUNTIME_DEP_PKGS_CSWvala += CSWlibintl8
RUNTIME_DEP_PKGS_CSWvala += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWvala += CSWpcre
RUNTIME_DEP_PKGS_CSWvala += CSWlibxslt
RUNTIME_DEP_PKGS_CSWvala += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWvala += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWvala += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWvala += CSWlibgobject2-0-0

# Linker anomaly between sparc and i386
CHECKPKG_OVERRIDES_CSWvala += surplus-dependency|CSWlibintl8

# Testsuite fails for 64 bit, disable for now
#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

# The testsuite expect "grep" to take -q
TEST_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk


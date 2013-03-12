NAME = ocaml
VERSION = 3.12.1
GARTYPE = v2

DESCRIPTION = Objective Caml programming language
define BLURB
  OCaml's toolset includes an interactive top level interpreter, a bytecode compiler, and an optimizing native code compiler. It has a large standard library that makes it useful for many of the same applications as Python or Perl, as well as robust modular and object-oriented programming constructs that make it applicable for large-scale software engineering. OCaml is the successor to Caml Light. The acronym CAML originally stood for Categorical Abstract Machine Language, although OCaml abandons this abstract machine.  Long description
endef

MASTER_SITES = http://caml.inria.fr/pub/distrib/ocaml-3.11/
DISTFILES  = $(NAME)-GARCOMPILER = GCC4

LICENSE = LICENSE

REINPLACE_USRLOCAL += configure

PATCHFILES += 0-patch
PATCHFILES += 10-patch
PATCHFILES += 12-patch
# PATCHFILES += 13-patch
PATCHFILES += 14-patch
PATCHFILES += 15-patch
PATCHFILES += 16-patch
PATCHFILES += 17-patch
PATCHFILES += 18-patch
PATCHFILES += 19-patch
PATCHFILES += 2-patch
PATCHFILES += 20-patch
PATCHFILES += 21-patch
PATCHFILES += 3-patch
PATCHFILES += 4-patch
PATCHFILES += 5-patch
PATCHFILES += 6-patch
PATCHFILES += 7-patch
PATCHFILES += 8-patch
PATCHFILES += 9-patch
PATCHFILES += 0023-fix-build-for-tk-X11.patch
#
# this is only a error ignor patch taken from here:
# http://caml.inria.fr/mantis/view.php?id=4663
# the real reason for the problem is described probably here:
# http://irccrew.org/~cras/nfs-coding-howto.html
PATCHFILES += 01-nfs-close-bug.patch

PACKAGES +=  CSWocaml
SPKG_DESC_CSWocaml = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWocaml += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWocaml += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWocaml += CSWlibtk8-5

# include static libs
MERGE_EXCLUDE_STATICLIBS =
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libasmrun.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libasmrunp.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libbigarray.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libcamlrun.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libgraphics.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libmldbm.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libnums.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libstr.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libthreads.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libthreadsnat.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/libunix.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/vmthreads/libvmthreads.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/labltk/liblabltk.a
CHECKPKG_OVERRIDES_CSWocaml += discouraged-path-in-pkgmap|/opt/csw/lib/ocaml/labltk/libtkanim.a

LICENSE = LICENSE

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $# BUILD_ARGS = world.opt
BUILD_ARGS = world opt
#CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += -bindir $(bindir)
# -bindir $(bindir)
CONFIGURE_ARGS += -libdir $(libdir)
CONFIGURE_ARGS += -mandir $(mandir)
CONFIGURE_ARGS += -prefix $(prefix)
Cverbose
CONFIGURE_ARGS += -cc "$(notdir $(CC)) $(CFLAGS)"
CONFIGURE_ARGS += -x11include /usr/include
CONFIGURE_ARGS += -x11lib /usr/X11/lib
# CONFIGURE_ARGS += -tklibs -lXext
INSTALL_ARGS += PWD=${PWD}/$(WORKSRC)

TEST_TARGET =

include gar/category.mk

NAME = libgnomeprint
VERSION = 2.18.6
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = TODO
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWlibgnomeprint CSWlibgnomeprintdevel CSWlibgnomeprintdoc
CATALOGNAME_CSWlibgnomeprint = libgnomeprint
CATALOGNAME_CSWlibgnomeprintdevel = libgnomeprint_devel
CATALOGNAME_CSWlibgnomeprintdoc = libgnomeprint_doc

SPKG_DESC_CSWlibgnomeprint += $(DESCRIPTION)
SPKG_DESC_CSWlibgnomeprintdevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibgnomeprintdoc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWlibgnomeprintdevel += CSWlibgnomeprint
RUNTIME_DEP_PKGS_CSWlibgnomeprintdoc += CSWlibgnomeprint

#BUILD_DEP_PKGS += CSWgnomeicontheme
#BUILD_DEP_PKGS += CSWlibgnomeprint
#BUILD_DEP_PKGS += CSWlibgnomecanvas
BUILD_DEP_PKGS += CSWlibgtk2-dev

RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWpango
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibgnomecups
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgnomeprint += CSWlibssl1-0-0

CHECKPKG_OVERRIDES_CSWlibgnomeprintdoc += surplus-dependency|CSWlibgnomeprint

CHECKPKG_OVERRIDES_CSWlibgnomeprintdoc += catalogname-does-not-match-pkgname|pkgname=CSWlibgnomeprintdoc|catalogname=libgnomeprint_doc|expected-catalogname=libgnomeprintdoc
CHECKPKG_OVERRIDES_CSWlibgnomeprintdevel += catalogname-does-not-match-pkgname|pkgname=CSWlibgnomeprintdevel|catalogname=libgnomeprint_devel|expected-catalogname=libgnomeprintdevel
CHECKPKG_OVERRIDES_CSWlibgnomeprint += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libgnomeprint/2.18.6/modules/libgnomeprintpapi.so
CHECKPKG_OVERRIDES_CSWlibgnomeprint += shared-lib-pkgname-mismatch|file=opt/csw/lib/libgnomeprint-2-2.so.0.1.0|soname=libgnomeprint-2-2.so.0|pkgname=CSWlibgnomeprint|expected=CSWlibgnomeprint2-2-0


UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/libgnomeprint

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_LDFLAGS = -lm
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
#BUILD64 = 1

PKGFILES_CSWlibgnomeprintdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgnomeprintdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibgnomeprintdoc = 1

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# To make sure the FILE type is recognized
PATCHFILES += 0001-add-missing-stdio.h-inclusion.patch

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

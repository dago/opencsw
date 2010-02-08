GARNAME = gnomevfs2
GNOME_PROJ = gnome-vfs
GARVERSION = 2.24.2
CATEGORIES = gnome

DESCRIPTION = GnomeVFS - Filesystem Abstraction library
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTNAME = $(GNOME_PROJ)-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2

PACKAGES = CSWgnomevfs2 CSWgnomevfs2devel CSWgnomevfs2doc
CATALOGNAME_CSWgnomevfs2 = gnomevfs2
CATALOGNAME_CSWgnomevfs2devel = gnomevfs2_devel
CATALOGNAME_CSWgnomevfs2doc = gnomevfs2_doc

SPKG_DESC_CSWgnomevfs2 += $(DESCRIPTION)
SPKG_DESC_CSWgnomevfs2devel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWgnomevfs2doc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWgtk2 CSWlibatk CSWlibcairo CSWlibx11
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWdbusglib CSWlibdbus CSWlibxext CSWpango
RUNTIME_DEP_PKGS_CSWgnomevfs2devel += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWgnomevfs2doc += CSWgnomevfs2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://projects.gnome.org/gnome-vfs/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

NOISAEXEC = 1
#NOISALIST = 1
# libdbus not 64-bit yet
BUILD64 = 1

PKGFILES_CSWgnomevfs2devel = $(PKGFILES_DEVEL)
PKGFILES_CSWgnomevfs2doc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgnomevfs2doc = 1

LIBS = -lsocket -lnsl
export LIBS

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk

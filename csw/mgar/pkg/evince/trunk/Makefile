# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = evince
GNOME_VERSION = 2.30
VERSION = $(GNOME_VERSION).3
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = Document viewer for multiple document formats
define BLURB
endef

SPKG_SOURCEURL = http://projects.gnome.org/evince/
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(GNOME_VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += 0001-honor-aclocal_flags.patch

# GARFLAVOR = DBG
# GARCOMPILER=GNU
GARCOMPILER=SOS12U3
STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --enable-introspection 
# CONFIGURE_ARGS_DBG = --enable-debug
# CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# use dogtail which we dont have
TEST_TARGET = 

# EXTRA_CFLAGS_DBG = -g
# EXTRA_CFLAGS += $(EXTRA_CFLAGS_$(GARFLAVOR))
# EXTRA_CXXFLAGS += -DPOPPLER_WITH_GDK
EXTRA_CXXFLAGS += -DHAVE_POPPLER_PAGE_RENDER -DPOPPLER_HAS_CAIRO
EXTRA_CFLAGS += -I/opt/csw/include/nautilus -I/opt/csw/include/gnome-vfs-2.0

EXTRA_LD_OPTIONS = -lm
# EXTRA_LD_OPTIONS = /opt/csw/X11/lib/libX11.so -lm
# There are no shared-object dependencies on CSWdbus, but it's required for
# evince to work.

# Shared libraries
RUNTIME_DEP_PKGS_CSWevince += CSWdbusglib
RUNTIME_DEP_PKGS_CSWevince += CSWdjvulibrert
RUNTIME_DEP_PKGS_CSWevince += CSWfconfig
RUNTIME_DEP_PKGS_CSWevince += CSWftype2
RUNTIME_DEP_PKGS_CSWevince += CSWgconf2
RUNTIME_DEP_PKGS_CSWevince += CSWggettextrt
RUNTIME_DEP_PKGS_CSWevince += CSWglib2
RUNTIME_DEP_PKGS_CSWevince += CSWgnomekeyring
RUNTIME_DEP_PKGS_CSWevince += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWevince += CSWgtk2
RUNTIME_DEP_PKGS_CSWevince += CSWlibatk
RUNTIME_DEP_PKGS_CSWevince += CSWlibcairo
RUNTIME_DEP_PKGS_CSWevince += CSWlibdbus
RUNTIME_DEP_PKGS_CSWevince += CSWlibglade2
RUNTIME_DEP_PKGS_CSWevince += CSWlibice
RUNTIME_DEP_PKGS_CSWevince += CSWlibsm
RUNTIME_DEP_PKGS_CSWevince += CSWlibx11
RUNTIME_DEP_PKGS_CSWevince += CSWlibxml2
RUNTIME_DEP_PKGS_CSWevince += CSWnautilus
RUNTIME_DEP_PKGS_CSWevince += CSWpango
RUNTIME_DEP_PKGS_CSWevince += CSWtiff
RUNTIME_DEP_PKGS_CSWevince += CSWzlib
RUNTIME_DEP_PKGS_CSWevince += CSWdbus
CHECKPKG_OVERRIDES_CSWevince += surplus-dependency|CSWdbus
# Shared MIME info is needed to detect file types
RUNTIME_DEP_PKGS_CSWevince += CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWevince += surplus-dependency|CSWsharedmimeinfo

BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibgconf-dev
BUILD_DEP_PKGS += CSWgnomedocutils
BUILD_DEP_PKGS += CSWintltool
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWgnomeicontheme
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWgnomekeyring-dev
BUILD_DEP_PKGS += CSWlibdbus-glib-dev
BUILD_DEP_PKGS += CSWpoppler-dev
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWlibspectre-dev
BUILD_DEP_PKGS += CSWlibdjvulibre-dev
BUILD_DEP_PKGS += CSWgobject-introspection-dev
BUILD_DEP_PKGS += CSWbinutils
BUILD_DEP_PKGS += CSWgnulinks
BUILD_DEP_PKGS += CSWtetex
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibpixman-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibatk-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWgnomevfs2-dev
BUILD_DEP_PKGS += CSWpy-libxml2

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && autoreconf
	@$(MAKECOOKIE)

PATH := /opt/csw/gnu:$(PATH)
AM_DEFAULT_VERBOSITY := 1

# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = evince
GNOME_VERSION = 2.30
VERSION = $(GNOME_VERSION).3
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = Document viewer for multiple document formats: pdf, ps ,dvi
define BLURB
endef

SPKG_SOURCEURL = http://projects.gnome.org/evince/
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(GNOME_VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# GARFLAVOR = DBG
# GARCOMPILER=GNU
GARCOMPILER=SOS12U3
STRIP_LIBTOOL = 1

PATCHFILES += 0001-honor-aclocal_flags.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

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
EXTRA_LINKER_FLAGS = -norunpath -xnorunpath
# EXTRA_LD_OPTIONS = /opt/csw/X11/lib/libX11.so -lm
# There are no shared-object dependencies on CSWdbus, but it's required for
# evince to work.

PACKAGES += CSWlibevdocument2
CATALOGNAME_CSWlibevdocument2 = libevdocument2
PKGFILES_CSWlibevdocument2 += $(call baseisadirs,$(libdir),libevdocument\.so\.2\.0\.0)
PKGFILES_CSWlibevdocument2 += $(call baseisadirs,$(libdir),libevdocument\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibevdocument2 += $(DESCRIPTION), libevdocument.so.2
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWpango
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibevdocument2 += CSWlibgio2-0-0

PACKAGES += CSWlibevview2
CATALOGNAME_CSWlibevview2 = libevview2
PKGFILES_CSWlibevview2 += $(call baseisadirs,$(libdir),libevview\.so\.2\.0\.0)
PKGFILES_CSWlibevview2 += $(call baseisadirs,$(libdir),libevview\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibevview2 += $(DESCRIPTION), libevview.so.2
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibevdocument2
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWpango
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibevview2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWevince-dev += CSWlibevdocument2
RUNTIME_DEP_PKGS_CSWevince-dev += CSWlibevview2

PACKAGES += CSWevince-dev
CATALOGNAME_CSWevince-dev = evince_dev
SPKG_DESC_CSWevince-dev += $(DESCRIPTION), development files
PKGFILES_CSWevince-dev += $(PKGFILES_DEVEL)

PACKAGES += CSWevince
SPKG_DESC_CSWevince += $(DESCRIPTION), base
RUNTIME_DEP_PKGS_CSWevince += CSWlibevdocument2
RUNTIME_DEP_PKGS_CSWevince += CSWlibevview2
RUNTIME_DEP_PKGS_CSWevince += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibdjvulibre21
RUNTIME_DEP_PKGS_CSWevince += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibpoppler-glib5
RUNTIME_DEP_PKGS_CSWevince += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWevince += CSWlibintl8
RUNTIME_DEP_PKGS_CSWevince += CSWlibz1
RUNTIME_DEP_PKGS_CSWevince += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWevince += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWevince += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWevince += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWevince += CSWlibspectre1
RUNTIME_DEP_PKGS_CSWevince += CSWlibpoppler7
RUNTIME_DEP_PKGS_CSWevince += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWevince += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWevince += CSWlibatk1-0-0

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
# Solaris10 paths: these are resuts of cmd: 
# $ scrollkeeper-config --pkglocalstatedir
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper/C
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper/C/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper/C/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper/TOC
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper/index
CHECKPKG_OVERRIDES_CSWevince += bad-location-of-file|file=/var/lib/scrollkeeper/scrollkeeper_docs

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

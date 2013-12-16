# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = evince
GNOME_VERSION = 2.32
VERSION = $(GNOME_VERSION).0
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = Document viewer for multiple document formats: pdf, ps ,dvi
define BLURB
endef

SPKG_SOURCEURL = http://projects.gnome.org/evince/
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(GNOME_VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWevince.postinstall
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# GARFLAVOR = DBG
GARCOMPILER=GCC4
# GARCOMPILER=SOS12U3
STRIP_LIBTOOL = 1

PATCHFILES += 0001-honor-aclocal_flags.patch
# PATCHFILES += 0002-poppler-api-changed.patch
# PATCHFILES += 0001-add-norunpath-to-allowed-compiler-flags-ltmain.sh.patch
PATCHFILES += 0001-fix-poppler-api-linearized-problem.patch
# remove this patch if Mantis 5130 is closed!!!

# PATCHFILES += 0003-libxml-2.0.pc-workaround

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-nautilus
# CONFIGURE_ARGS += --enable-introspection 
# CONFIGURE_ARGS_DBG = --enable-debug
# CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# use dogtail which we dont have
TEST_TARGET = 

# EXTRA_CFLAGS_DBG = -g
# EXTRA_CFLAGS += $(EXTRA_CFLAGS_$(GARFLAVOR))
# EXTRA_CXXFLAGS += -DPOPPLER_WITH_GDK
EXTRA_CXXFLAGS += -DHAVE_POPPLER_PAGE_RENDER -DPOPPLER_HAS_CAIRO  # -norunpath
EXTRA_CFLAGS += -I/opt/csw/include/nautilus -I/opt/csw/include/gnome-vfs-2.0 # -xnorunpath
EXTRA_CONFIGURE_ENV += PATH=/opt/csw/gnu:$(PATH)
EXTRA_INSTALL_ENV += PATH=/opt/csw/gnu:$(PATH)

EXTRA_LD_OPTIONS = -lm
# EXTRA_LD_OPTIONS = -lgmodule-2.0 -lm -lz
# EXTRA_LINKER_FLAGS = -norunpath -xnorunpath
# EXTRA_LD_OPTIONS = /opt/csw/X11/lib/libX11.so -lm
# There are no shared-object dependencies on CSWdbus, but it's required for
# evince to work.
EXTRA_BUILD_ENV = V=1

PACKAGES += CSWlibevdocument3
CATALOGNAME_CSWlibevdocument3 = libevdocument3
PKGFILES_CSWlibevdocument3 += $(call baseisadirs,$(libdir),libevdocument\.so\.3\.0\.0)
PKGFILES_CSWlibevdocument3 += $(call baseisadirs,$(libdir),libevdocument\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibevdocument3 += $(DESCRIPTION), libevdocument.so.3
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibevdocument3 += CSWlibgdk-pixbuf2-0-0
# sparc, there is not realy a difference either elfdump nor ldd
RUNTIME_DEP_PKGS_CSWlibevdocument3_sparc += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3_sparc+= CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3_sparc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibevdocument3_sparc += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3_sparc += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibevdocument3_sparc += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWlibevdocument3 += $(RUNTIME_DEP_PKGS_CSWlibevdocument3_$(GARCH))

PACKAGES += CSWlibevview3
CATALOGNAME_CSWlibevview3 = libevview3
PKGFILES_CSWlibevview3 += $(call baseisadirs,$(libdir),libevview\.so\.3\.0\.0)
PKGFILES_CSWlibevview3 += $(call baseisadirs,$(libdir),libevview\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibevview3 += $(DESCRIPTION), libevview.so.3
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibevdocument3
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibgailutil18
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibevview3 += CSWlibgcc-s1
# sparc, there is not realy a difference either elfdump nor ldd
RUNTIME_DEP_PKGS_CSWlibevview3_sparc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibevview3_sparc += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibevview3_sparc += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWlibevview3_sparc += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWlibevview3_sparc += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibevview3 += $(RUNTIME_DEP_PKGS_CSWlibevview3_$(GARCH))

PACKAGES += CSWevince-dev
CATALOGNAME_CSWevince-dev = evince_dev
SPKG_DESC_CSWevince-dev += $(DESCRIPTION), development files
PKGFILES_CSWevince-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWevince-dev += CSWlibevdocument3
RUNTIME_DEP_PKGS_CSWevince-dev += CSWlibevview3
RUNTIME_DEP_PKGS_CSWevince-dev += CSWevince

PACKAGES += CSWevince
SPKG_DESC_CSWevince += $(DESCRIPTION), base
RUNTIME_DEP_PKGS_CSWevince += CSWlibevdocument3
RUNTIME_DEP_PKGS_CSWevince += CSWlibevview3
RUNTIME_DEP_PKGS_CSWevince += CSWlibdjvulibre21
RUNTIME_DEP_PKGS_CSWevince += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibintl8
RUNTIME_DEP_PKGS_CSWevince += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWevince += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWevince += CSWlibspectre1
RUNTIME_DEP_PKGS_CSWevince += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWevince += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWevince += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWevince += CSWlibpoppler-glib8
RUNTIME_DEP_PKGS_CSWevince += CSWlibkpathsea6
RUNTIME_DEP_PKGS_CSWevince += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWevince += CSWlibglib2-dev
# sparc, there is not realy a difference either elfdump nor ldd
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWevince_sparc += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWevince += $(RUNTIME_DEP_PKGS_CSWevince_$(GARCH))
CHECKPKG_OVERRIDES_CSWevince += surplus-dependency|CSWlibglib2-dev

# at least the machine-id file must exist, dbus-daemon creates this
# CHECKPKG_OVERRIDES_CSWevince += surplus-dependency|CSWdbus
# Solaris10 paths: these are resuts of cmd: 
# $ scrollkeeper-config --pkglocalstatedir
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/C
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/C/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/C/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/TOC
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/am
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/am/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/am/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/az
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/az/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/az/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/be
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/be/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/be/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ca
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ca/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ca/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/cs
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/cs/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/cs/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/da
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/da/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/da/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/de
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/de/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/de/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/el
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/el/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/el/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/es
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/es/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/es/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/fr
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/fr/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/fr/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/hu
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/hu/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/hu/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/index
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/it
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/it/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/it/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ja
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ja/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ja/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/kn
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/kn/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/kn/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ko
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ko/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ko/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/nl
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/nl/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/nl/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/no
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/no/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/no/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/pl
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/pl/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/pl/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/pt_BR
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/pt_BR/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/pt_BR/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ro
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ro/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ro/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ru
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ru/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/ru/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/scrollkeeper_docs
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sk
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sk/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sk/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sl
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sl/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sl/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sr
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sr/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sr/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sr@Latn
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sr@Latn/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sr@Latn/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sv
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sv/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/sv/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/tr
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/tr/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/tr/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/uk
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/uk/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/uk/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/vi
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/vi/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/vi/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/zh_CN
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/zh_CN/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/zh_CN/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/zh_TW
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/zh_TW/scrollkeeper_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/zh_TW/scrollkeeper_extended_cl.xml
CHECKPKG_OVERRIDES_CSWevince += discouraged-path-in-pkgmap|/opt/csw/var/lib/scrollkeeper/scrollkeeper_docs



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

# pre-configure:
# 	( cd $(WORKSRC); \
# 	[ -f ltmain.sh ] && rm ltmain.sh || true; \
# 	libtoolize --copy --force; \
##  	aclocal-1.11 --force; \
# 	autoconf --force; \
# 	autoheader --force; \
# 	automake-1.11 --add-missing --copy --force-missing  )
# 	@$(MAKECOOKIE)

AM_DEFAULT_VERBOSITY := 1

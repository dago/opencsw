# $Id$
NAME = dia
VERSION = 0.97.2
GARTYPE = v2

DESCRIPTION = A GTK+ based diagram creation program

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES += $(NAME)-$(VERSION).tar.xz

PATCHFILES += 0001-Keep-norunpath-during-libtool.patch

VENDOR_URL = http://live.gnome.org/Dia

# BUILD_DEP_PKGS += 

PACKAGES += CSWdia
SPKG_DESC_CSWdia = A GTK+ based diagram creation program
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWdia += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWdia += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWdia += CSWlibemf1
RUNTIME_DEP_PKGS_CSWdia += CSWlibintl8
RUNTIME_DEP_PKGS_CSWdia += CSWlibz1
RUNTIME_DEP_PKGS_CSWdia += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWdia += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWdia += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWdia += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWdia += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWdia += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWdia += CSWlibart

# Linker difference between sparc and i386
CHECKPKG_OVERRIDES_CSWdia += surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWdia += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWdia += surplus-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWdia += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWdia += surplus-dependency|CSWlibatk1-0-0

# Locations of locale.alias:
#   /usr/share/locale/locale.alias: not used in Solaris
#   /usr/local/share/locale/locale.alias: replace with /opt/csw/share/locale/locale.alias
#   /usr/lib/X11/locale/locale.alias: not used in Solaris
#   /usr/openwin/lib/locale/locale.alias: ok
REINPLACEMENTS += locale
REINPLACE_MATCH_locale = /usr/local/share/locale/locale.alias
REINPLACE_WITH_locale = $(sharedstatedir)/locale/locale.alias
REINPLACE_FILES_locale += lib/intl.c

# Doesn't harm, see above
CHECKPKG_OVERRIDES_CSWdia += file-with-bad-content|/usr/share|root/opt/csw/lib/dia/libdia.so

# For GNU gettext like msgmerge
CONFIGURE_ENV_PATH = $(prefix)/gnu:$(PATH)

EXTRA_INC += $(includedir)/libEMF

EXTRA_LINKER_FLAGS += -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

# Tests for i386 fail in /Dia/Objects/Istar - goal/Copy with
#   g_str_hash (100) + 16

# For GNU xgettext
TEST_ENV_PATH = $(prefix)/gnu:$(PATH)

include gar/category.mk


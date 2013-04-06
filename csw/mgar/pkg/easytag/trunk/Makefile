NAME = easytag
VERSION = 2.1.8
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Tag editor for MP3, Ogg Vorbis files and more
define BLURB
  EasyTAG is a utility for viewing and editing tags for MP3, MP2, MP4/AAC, FLAC,
  Ogg Vorbis, MusePack, Monkey's Audio and WavPack files. Its simple and nice GTK+
  interface makes tagging easier under GNU/Linux or Windows.
endef
GNOME_MIRRORS)
DISTFILES += $(NAME)-$(VERSION).tar.xz

VENDOR_URL = http://projects.gnome.org/easytag/al_search_fix.diff

BUILD_DEP_PKGS += CSWlibogg-dev
BUILD_DEP_PKGS += CSWlibvorbis-dev
BUILD_DEP_PKGS += CSWlibflac-dev
BUILD_DEP_PKGS += CSWlibspeex-dev
BUILD_DEP_PKGS += CSWlibwavpack-dev

RUNTIME_DEP_PKGS_CSgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibid3-3-8-3
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibgtk-x11-2-0-0CSWlibwavpack-dev

RUNTIME_DEP_PKGS_CSWeasytag += CSWlibintl8
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibogg0
RUNTIME_DEP_PKGS_CSid3tag
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibwavpack1
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibflac8ytag += CSWfconfig
RUNTIME_DEP_PKGS_CSWeasytag += CSWpango
RUNTIME_DEP_PKGSlibspeex1
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWeasytag += CSWlibgio2-0-0

# This macro is being phased out of Pango, so this seems like an acceptable fix for now:
#   https://bugzilla.gnome.org/show_bug.cgi?id=652202
EXTRA_CFLAGS += -DG_CONST_RETURN=const

EXTRA_LINKER_FLAGS = -norunpath

# For msgfmt, msgmerge, xgettext and gettext to be used from GNU
CONFIGURE_ENV_PATH = $(prefix)/gnu:$(PATH)

include gar/category.mk

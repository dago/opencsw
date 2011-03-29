NAME = bluefish
VERSION = 2.0.3
CATEGORIES = apps

DESCRIPTION = Advanced Gtk+ HTML editor
define BLURB
Bluefish is a GTK+ HTML editor for the experienced web designer. Its features include nice wizards for startup, tables and frames; a fully featured image insert dialog; thumbnail creation and automatically linking of the thumbnail with the original image; and configurable HTML syntax highlighting. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =

CONFIGURE_ARGS += $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWbluefish += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbluefish += CSWenchant
RUNTIME_DEP_PKGS_CSWbluefish += CSWftype2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibcairo
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibxml2
RUNTIME_DEP_PKGS_CSWbluefish += CSWgtk2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibatk
RUNTIME_DEP_PKGS_CSWbluefish += CSWpango
RUNTIME_DEP_PKGS_CSWbluefish += CSWfconfig
RUNTIME_DEP_PKGS_CSWbluefish += CSWglib2

CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/treemagic|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/globs|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/generic-icons|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/aliases|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/subclasses|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/magic|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/globs2|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/applications/mimeinfo.cache|CSWbluefish|CSWcontrolcenter
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/mime.cache|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/types|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/XMLnamespaces|CSWbluefish|CSWsharedmimeinfo
CHECKPKG_OVERRIDES_CSWbluefish += file-collision|/opt/csw/share/mime/icons|CSWbluefish|CSWsharedmimeinfo

CHECKPKG_OVERRIDES_CSWbluefish += file-with-bad-content|/usr/local|root/opt/csw/share/bluefish/bflang/all-php.bfinc

include gar/category.mk

# ./configure needs this to find ggettext
PATH := /opt/csw/gnu:$(PATH)

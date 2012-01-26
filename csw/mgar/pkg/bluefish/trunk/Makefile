NAME = bluefish
VERSION = 2.2.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Advanced Gtk+ HTML editor
define BLURB
Bluefish is a GTK+ HTML editor for the experienced web designer. Its features include nice wizards for startup, tables and frames; a fully featured image insert dialog; thumbnail creation and automatically linking of the thumbnail with the original image; and configurable HTML syntax highlighting. 
endef

MASTER_SITES = http://www.bennewitz.com/bluefish/stable/source/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =

CONFIGURE_ARGS += $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWbluefish += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbluefish += CSWenchant
RUNTIME_DEP_PKGS_CSWbluefish += CSWftype2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWbluefish += CSWgtk2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWpango
RUNTIME_DEP_PKGS_CSWbluefish += CSWfconfig
RUNTIME_DEP_PKGS_CSWbluefish += CSWglib2

EXTRA_MERGE_EXCLUDE_FILES = .*treemagic.*
EXTRA_MERGE_EXCLUDE_FILES += .*globs.*
EXTRA_MERGE_EXCLUDE_FILES += .*generic-icons.*
EXTRA_MERGE_EXCLUDE_FILES += .*aliases.*
EXTRA_MERGE_EXCLUDE_FILES += .*subclasses.*
EXTRA_MERGE_EXCLUDE_FILES += .*magic.*
EXTRA_MERGE_EXCLUDE_FILES += .*globs2.*
EXTRA_MERGE_EXCLUDE_FILES += .*mimeinfo.cache.*
EXTRA_MERGE_EXCLUDE_FILES += .*mime.cache.*
EXTRA_MERGE_EXCLUDE_FILES += .*types.*
EXTRA_MERGE_EXCLUDE_FILES += .*XMLnamespaces.*
EXTRA_MERGE_EXCLUDE_FILES += .*icons.*

# these packages have not been installed/updated on the buildfarm yet
# but they are in the unstable catalog.  Temporarily overriding until
# buildfarm is updated.
CHECKPKG_OVERRIDES_CSWbluefish += missing-dependency|CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWbluefish += missing-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWbluefish += missing-dependency|CSWlibgobject2-0-0
CHECKPKG_OVERRIDES_CSWbluefish += missing-dependency|CSWlibgthread2-0-0
CHECKPKG_OVERRIDES_CSWbluefish += missing-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWbluefish += surplus-dependency|CSWglib2

include gar/category.mk

# ./configure needs this to find ggettext
PATH := /opt/csw/gnu:$(PATH)

# search/replace /usr/local with /opt/csw
post-install-modulated:
	perl -pi -e 's|/usr/local|$(prefix)|' $(DESTDIR)/opt/csw/share/bluefish/bflang/all-php.bfinc

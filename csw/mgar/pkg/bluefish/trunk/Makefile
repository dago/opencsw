NAME = bluefish
VERSION = 2.2.3

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
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWpango
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWpython
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWbluefish += CSWlibgio2-0-0

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

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

# ./configure needs this to find ggettext
PATH := /opt/csw/gnu:$(PATH)

# search/replace /usr/local with /opt/csw
post-install-modulated:
	perl -pi -e 's|/usr/local|$(prefix)|' $(DESTDIR)/opt/csw/share/bluefish/bflang/all-php.bfinc

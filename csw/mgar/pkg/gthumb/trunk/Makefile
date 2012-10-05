# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gthumb
VERSION = 2.10.12
# VERSION = 2.12.4
SUBDIR=$(basename $(VERSION))
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = Image organizer
define BLURB
  gThumb is an image viewer and browser for the GNOME Desktop. It also includes an importer tool for transferring photos from cameras.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/gthumb/$(SUBDIR)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz # xz

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
STRIP_LIBTOOL = 1
# PATCHFILES += 0001-configure.ac.patch

PATCHFILES += mkdtemp-patch

BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibgconf-dev
BUILD_DEP_PKGS += CSWlibexif-dev 
# BUILD_DEP_PKGS += CSWlibunique-dev   
# BUILD_DEP_PKGS += CSWlibsoupdevel 
# BUILD_DEP_PKGS += CSWgnomekeyring-dev

PACKAGES += CSWlibgthumb
PKGFILES_CSWlibgthumb += $(call baseisadirs,$(libdir),libgthumb\.so)
SPKG_DESC_CSWlibgthumb += $(DESCRIPTION), libgthumb.so
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgnomeui2-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibexif12
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibglade2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWpango
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibbonoboui
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibglib2-0-0
# this is reported because lib was not split out in the old package
# CHECKPKG_OVERRIDES_CSWlibgthumb += file-collision|/opt/csw/lib/libgthumb.so|CSWgthumb|CSWlibgthumb
# there is really only the .so name
CHECKPKG_OVERRIDES_CSWlibgthumb += soname-equals-filename|file=/opt/csw/lib/libgthumb.so

PACKAGES += CSWgthumb
SPKG_DESC_CSWgthumb += $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgthumb
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnomeui2-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibexif12
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWorbit2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibz1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibglade2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWpango
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibbonoboui
RUNTIME_DEP_PKGS_CSWgthumb += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibart
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibatk1-0-0
EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/var/lib.*

# for xmllint
EXTRA_TEST_ENV += http_proxy=http://proxy:3128

EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-gnome-3

include gar/category.mk

# pre-configure-modulated:
# 	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
# 	cd $(WORKSRC) && aclocal
# 	cd $(WORKSRC) && autoconf --force
# 	cd $(WORKSRC) && automake -a -c -f
# 	@$(MAKECOOKIE)

PATH:=/opt/csw/gnu:$(PATH)

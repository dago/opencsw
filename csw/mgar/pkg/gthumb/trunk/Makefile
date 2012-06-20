# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gthumb
VERSION = 2.10.12
SUBDIR=$(basename $(VERSION))
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/gthumb/$(SUBDIR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = Solaris10-sparc Solaris10-i386

PATCHFILES += mkdtemp-patch

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
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgnomecanvas
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgthumb += CSWlibgnome
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
CHECKPKG_OVERRIDES_CSWlibgthumb += file-collision|/opt/csw/lib/libgthumb.so|CSWgthumb|CSWlibgthumb
# there is really only the .so name
CHECKPKG_OVERRIDES_CSWlibgthumb += soname-equals-filename|file=/opt/csw/lib/libgthumb.so

RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgthumb
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnomeui2-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibexif12
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnomecanvas
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgthumb += CSWlibgnome
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

# for xmllint
EXTRA_TEST_ENV += http_proxy=http://proxy:3128

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH:=/opt/csw/gnu:$(PATH)

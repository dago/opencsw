# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gdk-pixbuf
VERSION = 2.24.0
GARTYPE = v2
CATEGORIES = gnome

# Those overrides must be removed after gtk 2.24 has been released.
#
# Somewhere between the 2.18 and 2.24 release of gtk, the gtk guys
# decided to spin off gdk-pixbuf.
#
# So in the transition phase of 2.18 to 2.24 we have to face
# collisions, since 2.18 brings its own gdk-pixbuf, whereas 2.24 uses
# this package
#
# A simple test with emacs-gtk and gftp does not indicate that
# installing gdk-pixbuf over an existing gtk 2.18 installation does
# break anything.
CHECKPKG_OVERRIDES_CSWgdkpixbuf += file-collision|/opt/csw/bin/gdk-pixbuf-query-loaders|CSWgdkpixbuf|CSWgtk2
CHECKPKG_OVERRIDES_CSWgdkpixbuf += file-collision|/opt/csw/bin/gdk-pixbuf-csource|CSWgdkpixbuf|CSWgtk2
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-query-loaders.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/GdkPixbufLoader.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-csource.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-4.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/left.png|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/right.png|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-rendering.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/rn02.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-from-drawables.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/license.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-6.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-10.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/style.css|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/composite.png|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/rn01.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf.devhelp2|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Versioning.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-full.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/index.sgml|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-8.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/home.png|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/index.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/up.png|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-deprecated.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-12.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-14.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/api-index-2-2.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += file-collision|/opt/csw/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Module-Interface.html|CSWgdkpixbuf-doc|CSWgtk2doc
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/sparcv9/libgdk_pixbuf-2.0.so|CSWgtk2|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/libgdk_pixbuf_xlib-2.0.so|CSWgtk2|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/pkgconfig/gdk-pixbuf-xlib-2.0.pc|CSWgtk2devel|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/sparcv9/pkgconfig/gdk-pixbuf-2.0.pc|CSWgtk2devel|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/sparcv9/libgdk_pixbuf_xlib-2.0.so|CSWgtk2|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/pkgconfig/gdk-pixbuf-2.0.pc|CSWgtk2devel|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/sparcv9/pkgconfig/gdk-pixbuf-xlib-2.0.pc|CSWgtk2devel|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/libgdk_pixbuf-2.0.so|CSWgtk2|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf2-0-0 += file-collision|/opt/csw/lib/sparcv9/libgdk_pixbuf-2.0.so.0|CSWgtk2|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf2-0-0 += file-collision|/opt/csw/lib/libgdk_pixbuf-2.0.so.0|CSWgtk2|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-xlib2-0-0 += file-collision|/opt/csw/lib/libgdk_pixbuf_xlib-2.0.so.0|CSWgtk2|CSWlibgdk-pixbuf-xlib2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-xlib2-0-0 += file-collision|/opt/csw/lib/sparcv9/libgdk_pixbuf_xlib-2.0.so.0|CSWgtk2|CSWlibgdk-pixbuf-xlib2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf2-0-0 += file-collision|/opt/csw/lib/amd64/libgdk_pixbuf-2.0.so.0|CSWgtk2|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-xlib2-0-0 += file-collision|/opt/csw/lib/amd64/libgdk_pixbuf_xlib-2.0.so.0|CSWgtk2|CSWlibgdk-pixbuf-xlib2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/amd64/libgdk_pixbuf-2.0.so|CSWgtk2|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/amd64/pkgconfig/gdk-pixbuf-2.0.pc|CSWgtk2devel|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/amd64/libgdk_pixbuf_xlib-2.0.so|CSWgtk2|CSWlibgdk-pixbuf-dev
CHECKPKG_OVERRIDES_CSWlibgdk-pixbuf-dev += file-collision|/opt/csw/lib/amd64/pkgconfig/gdk-pixbuf-xlib-2.0.pc|CSWgtk2devel|CSWlibgdk-pixbuf-dev


DESCRIPTION = GNOME tools for pixmap manupulation
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
DISTFILES += CSWgdkpixbuf.postinstall

EXPANDVARS = CSWgdkpixbuf.postinstall

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWgdkpixbuf
# To retain backwards compatibility with gdk pixbuf package 0.22
CATALOGNAME_CSWgdkpixbuf = gdk_pixbuf
SPKG_DESC_CSWgdkpixbuf = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdkpixbuf  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgdk-pixbuf-xlib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibtiff3
# I assume if one installs CSWgdkpixbuf, one wants all the stuff
# except -dev
CHECKPKG_OVERRIDES_CSWgdkpixbuf += surplus-dependency|CSWlibgdk-pixbuf-xlib2-0-0
CHECKPKG_OVERRIDES_CSWgdkpixbuf += catalogname-does-not-match-pkgname|pkgname=CSWgdkpixbuf|catalogname=gdk_pixbuf|expected-catalogname=gdkpixbuf

PACKAGES += CSWgdkpixbuf-doc
# To retain backwards compatibility with gdk pixbuf package 0.22
CATALOGNAME_CSWgdkpixbuf-doc = gdk_pixbuf_doc
SPKG_DESC_CSWgdkpixbuf-doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgdkpixbuf-doc = 1
PKGFILES_CSWgdkpixbuf-doc = .*/gtk-doc/.*
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += catalogname-does-not-match-pkgname|pkgname=CSWgdkpixbuf-doc|catalogname=gdk_pixbuf_doc|expected-catalogname=gdkpixbuf_doc

PACKAGES += CSWlibgdk-pixbuf2-0-0
SPKG_DESC_CSWlibgdk-pixbuf2-0-0 = $(DESCRIPTION), libgdk_pixbuf-2.0.so.0
PKGFILES_CSWlibgdk-pixbuf2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0  = CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibintl8

PACKAGES += CSWlibgdk-pixbuf-xlib2-0-0
SPKG_DESC_CSWlibgdk-pixbuf-xlib2-0-0 = $(DESCRIPTION), libgdk_pixbuf_xlib-2.0.so.0
PKGFILES_CSWlibgdk-pixbuf-xlib2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf_xlib-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibpng12-0

PACKAGES += CSWlibgdk-pixbuf-dev
SPKG_DESC_CSWlibgdk-pixbuf-dev = Developtment files $(DESCRIPTION)
PKGFILES_CSWlibgdk-pixbuf-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev = CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev += CSWlibgdk-pixbuf-xlib2-0-0



BUILD_DEP_PKGS  = CSWggettext-dev
BUILD_DEP_PKGS += CSWjbigkit
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibintl8
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWtiff

BUILD64 = 1

# We need the binaries to query 64 bit modules
MERGE_DIRS_isa-extra = $(bindir) $(libdir)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix
CONFIGURE_ARGS += --with-libintl-prefix

include gar/category.mk


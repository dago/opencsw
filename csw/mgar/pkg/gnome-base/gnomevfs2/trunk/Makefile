NAME = gnomevfs2
GNOME_PROJ = gnome-vfs
VERSION = 2.24.4
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GnomeVFS - Filesystem Abstraction library
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTNAME = $(GNOME_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# The smbc_remove_unused_server function has been deprecated in samba 3.2 
# but gnomevfs code has not been updated: https://bugzilla.gnome.org/show_bug.cgi?id=592341
# Let's try to use instead the new function
PATCHFILES = 0002-dont-use-smbc_remove_unused_server.patch

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://projects.gnome.org/gnome-vfs/

# Many more missing
BUILD_DEP_PKGS += CSWlibgamin-dev
BUILD_DEP_PKGS += CSWlibssl-dev

PACKAGES += CSWgnomevfs2
SPKG_DESC_CSWgnomevfs2 += $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWsambalib
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibfam0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWgnomevfs2 += CSWlibdbus1-3

# This is an explicit fallback *after* /opt/csw/share, see xdg-reinplacement below
CHECKPKG_OVERRIDES_CSWgnomevfs2 += file-with-bad-content|/usr/share|root/opt/csw/lib/libgnomevfs-2.so.0.2400.4
CHECKPKG_OVERRIDES_CSWgnomevfs2 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libgnomevfs-2.so.0.2400.4
CHECKPKG_OVERRIDES_CSWgnomevfs2 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libgnomevfs-2.so.0.2400.4

# No real package split done yet
CHECKPKG_OVERRIDES_CSWgnomevfs2 += shared-lib-pkgname-mismatch

PACKAGES += CSWgnomevfs2-dev
SPKG_DESC_CSWgnomevfs2-dev += Development files for GNOME vfs
PKGFILES_CSWgnomevfs2-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWgnomevfs2-dev += $(sharedstatedir)/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWgnomevfs2-dev += CSWgnomevfs2
OBSOLETED_BY_CSWgnomevfs2-dev = CSWgnomevfs2devel
CATALOGNAME_CSWgnomevfs2devel = gnomevfs2_devel_stub
OBSOLETED_BY_CSWgnomevfs2-dev = CSWgnomevfs2doc
CATALOGNAME_CSWgnomevfs2doc = gnomevfs2_doc_stub

REINPLACEMENTS += xdg
REINPLACE_MATCH_xdg = /usr/local/share
REINPLACE_WITH_xdg = $(sharedstatedir)
REINPLACE_FILES_xdg = libgnomevfs/xdgmime.c

NOISALIST = 1
BUILD64_LIBS_ONLY = 1

# STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc

include gar/category.mk

# For GNU gettext
PATH := /opt/csw/gnu:$(PATH)

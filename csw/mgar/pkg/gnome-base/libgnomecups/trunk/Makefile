NAME = libgnomecups
VERSION = 0.1.13
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GNOME library for CUPS interaction
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWlibgnomecups
CATALOGNAME_CSWlibgnomecups = libgnomecups

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://ftp.gnome.org/pub/GNOME/sources/libgnomecups/

RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibgnomecups += CSWlibglib2-0-0

CHECKPKG_OVERRIDES_CSWlibgnomecups += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libgnomecups-1.0.so
CHECKPKG_OVERRIDES_CSWlibgnomecups += shared-lib-pkgname-mismatch|file=opt/csw/lib/libgnomecups-1.0.so.1.0.0|soname=libgnomecups-1.0.so.1|pkgname=CSWlibgnomecups|expected=CSWlibgnomecups1-0-1

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# cups-config output "-lcups -L/opt/csw/lib ..." but
# -L/opt/csw/lib must be first so that ld search libcups.so
# in this directory.
# This patch workarounds this problem
PATCHFILES = 0001-cups-config-bug-workaround.patch

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


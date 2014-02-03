# $Id$
NAME = mc
VERSION = 4.8.11
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A curses-based visual shell and file manager
define BLURB
endef

# The function "isblank" is not there on Solaris 9, so we can either use
# gnulib and build on Solaris 9, or build on Solaris 10.
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASftp.midnight-commander.org/
DISTFILES  = $(DISTNAME).tar.xz

VENDOR_URL = http://www.midnight-commander.org

RUNTIME_DEP_PKGS_CSWmc += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWmc += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWmc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmc += CSWlibslang2
RUNTIME_DEP_PKGS_CSWmc += CSWlibssh2-1
RUNTIME_DEP_PKGS_CSWmc += CSWperl
/opt/csw/mc/mc.menu
CHECKPKG_OVERRIDES_CSWmc += file-with-bad-content|/usr/local|root/etc/opt/csw/mc/mc.menu
CHECKPKG_OVERRIDES_CSWmc += file-with-bad-content|/usr/local|root/etc/opt/csw/mc/mc.menu.sr
CHECKPKG_OVERRIDES_CSWmc += file-with-bad-content|/usr/local|root/opt/csw/libexec/mc/extfs.d/README
CHECKPKG_file-with-bad-content|/usr/local|root/opt/csw/libexec/mc/extfs.d/ulib
CHECKPKG_OVERRIDES_CSWmc += missing-dependency|CSWemacs-common

GARCOMPILER = GNU

include gar/category.mk

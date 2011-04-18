# $Id$
NAME = gcal
VERSION = 3.6
CATEGORIES = apps

DESCRIPTION = Gcal is a program for calculating and printing calendars
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Need-minor-tweaks-for-Solaris.patch

PACKAGES = CSWgcal
CATALOGNAME_CSWgcal = gcal
RUNTIME_DEP_PKGS_CSWgcal += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgcal += CSWncurses
RUNTIME_DEP_PKGS_CSWgcal += CSWperl

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_CPPFLAGS = -DGCAL_SYS_DATADIR=\\\"$(sharedstatedir)/gcal\\\"

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

# This is ok, there is a list of pathes given
CHECKPKG_OVERRIDES_CSWgcal += file-with-bad-content|/usr/local|root/opt/csw/share/info/gcal.info

include gar/category.mk

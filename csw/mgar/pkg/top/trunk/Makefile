NAME = top
VERSION = 3.8beta1
CATEGORIES = apps

DESCRIPTION = Unix system state reporter
define BLURB
endef

SF_PROJ = unixtop
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Location for browsing these patches is
#   http://src.opensolaris.org/source/xref/userland/src/components/top/patches/
# For safety they have also been put in files/
MASTER_SITES += http://src.opensolaris.org/source/raw/userland/src/components/top/patches/
PATCHFILES += 01.cmds.patch
PATCHFILES += 02.hash-c.patch
PATCHFILES += 03.sunos5.patch

VENDOR_URL = http://www.unixtop.org/

LICENSE = LICENSE

# This is for terminfo:
#   TERMINFO=/usr/share/lib/terminfo/
CHECKPKG_OVERRIDES_CSWtop += file-with-bad-content|/usr/share|root/opt/csw/bin/sparcv8/top
CHECKPKG_OVERRIDES_CSWtop += file-with-bad-content|/usr/share|root/opt/csw/bin/sparcv9/top
CHECKPKG_OVERRIDES_CSWtop += file-with-bad-content|/usr/share|root/opt/csw/bin/i386/top
CHECKPKG_OVERRIDES_CSWtop += file-with-bad-content|/usr/share|root/opt/csw/bin/amd64/top

BUILD64 = 1
ISAEXEC = 1

# No runtime linker path as we don't reference any libs from /opt/csw
RUNPATH_LINKER_FLAGS =

# autoconf tries to compile for the current kernel. Get rid of
# these extra flags as we set them ourselves with BUILD64 = 1
BUILD_OVERRIDE_DIRS = ARCHFLAG

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-dualarch

# top doesn't have a testsuite
TEST_TARGET =

include gar/category.mk

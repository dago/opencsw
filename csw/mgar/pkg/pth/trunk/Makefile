GARNAME = pth
GARVERSION = 2.0.7
CATEGORIES = lib

DESCRIPTION = GNU Pth - The GNU Portable Threads
define BLURB
  Pth is a very portable POSIX/ANSI-C based library for Unix platforms which
  provides non-preemptive priority-based scheduling for multiple threads of
  execution (aka 'multithreading') inside event-driven applications.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpth,)

SPKG_SOURCEURL = http://www.gnu.org/software/pth/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

## Patch PTH.H to increase FD_SETSIZE for 64bit builds
PATCHFILES = patch_pth_fdsetsize64.diff

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

# Add static libs as under Solaris 7/8 x86 shared libpth doesn't work correctly.
MERGE_EXCLUDE_STATICLIBS =

include gar/category.mk

# No shared libraries on Solaris 7/8 x86:
#   http://www.mail-archive.com/pth-users@gnu.org/msg00113.html
# and (from ChangeLog)
#   *) Make --disable-shared the default under Solaris-2.[78]/x86, because
#      it is known to segfault sporadically if Pth is built as a DSO.  As
#      traces showed, it is not a Pth problem, but it looks like a problem with
#      the dynamic linker on Solaris/x86.  The same Solaris versions on SPARC
#      don't have this problem.
#      [Ralf S. Engelschall]

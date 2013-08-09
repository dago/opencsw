NAME = libstatgrab
VERSION = 0.90
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library that provides cross platform access to statistics
define BLURB
  libstatgrab is a library that provides cross platform access to statistics
  about the system on which it's run. It's written in C and presents a selection
  of useful interfaces which can be used to access key system statistics. The
  current list of statistics includes CPU usage, memory utilisation, disk usage,
  process counts, network traffic, disk I/O, and more.
endef

MASTER_SITES = ftp://ftp.uk.i-scream.org/pub/i-scream/libstatsgrab/
MASTER_SITES += http://dl.ambiweb.de/mirrors/ftp.i-scream.org/libsta+= $(DISTNAME).tar.gz

VENDOR_URL = http://www.i-scream.org/libstatgrab/

PACKAGES += CSWlibstatgrab9
SPKG_DESC_CSWlibstatgrab9 = A library that provides cross platform access to statistics, libstatgrab.so.9
PKGFILES_CSWlibstatgrab9 += $(call pkgfiles_lib,libstatgrab.so.9)

PACKAGES += CSWlibstatgrab-dev
SPKG_DESC_CSWlibstatgrab-dev = Development files for libstatgrab.so.9 libstatgrab.so.6
PKGFILES_CSWlibstatgrab-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibstatgrab-dev 9= CSWlibstatgrab6

# Put this in -utils:
#   statgrab-make-mrtg-config
PKGFILES_DEVEL_CONFIG =
PKGFILES_DEVEL_CONFIG_MANPAGE =
DEVEL_EXECUTABLES =
ISAEXEC_EXCLUDE_FILES =

PACKAGES += CSWlibstatgrab-utils
SPKG_DESC_CSWlibstatgrab-utils = Statistic gathering tools based on libstatgrab.so.6
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibstatgrab-utils 9

# Don't pull in ncurses from CSW, but add needed libraries to be self-sufficient
LINKER_FLAGS =fo -lsocket -lnsl

BUILD64 = 1
ISAEXEC = 1
NORUNPATH = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses-prefix=/usr

include
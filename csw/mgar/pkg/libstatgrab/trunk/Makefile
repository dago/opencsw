GARNAME = libstatgrab
GARVERSION = 0.16
CATEGORIES = lib

DESCRIPTION = A library that provides cross platform access to statistics
define BLURB
  libstatgrab is a library that provides cross platform access to statistics
  about the system on which it's run. It's written in C and presents a selection
  of useful interfaces which can be used to access key system statistics. The
  current list of statistics includes CPU usage, memory utilisation, disk usage,
  process counts, network traffic, disk I/O, and more.
endef

MASTER_SITES = ftp://ftp.uk.i-scream.org/pub/i-scream/libstatsgrab/
MASTER_SITES += http://dl.ambiweb.de/mirrors/ftp.i-scream.org/libstatgrab/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Don't pull in ncurses from CSW
LINKER_FLAGS = 

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses-prefix=/usr

TEST_TARGET = check

include gar/category.mk

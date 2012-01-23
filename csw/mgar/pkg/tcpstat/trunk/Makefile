# $Id$
NAME = tcpstat
VERSION = 1.5
CATEGORIES = utils

DESCRIPTION = Report network interface statistics
define BLURB
  tcpstat reports certain network interface statistics much like vmstat does for system statistics.
  tcpstat gets its information by either monitoring a specific interface, or by reading previously
  saved tcpdump data from a file.
endef

MASTER_SITES = http://www.frenchfries.net/paul/tcpstat/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

BUILD_DEP_PKGS = CSWlibpcap CSWlibpcapdevel
RUNTIME_DEP_PKGS = CSWlibpcap

# EXTRA_INC = $(prefix)/bdb48/include
# EXTRA_LIB = $(prefix)/bdb48/lib

# Otherwise inet_ntop(3socket) is not correctly detected
EXTRA_LINKER_FLAGS = -lsocket -lnsl

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_MERGE_EXCLUDE_FILES = .*/tcpprof\.1

include gar/category.mk

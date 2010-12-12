NAME = tcpdump
VERSION = 4.1.1
CATEGORIES = utils

DESCRIPTION = Dump network traffic
define BLURB
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

BUILD_DEP_PKGS = CSWlibpcap CSWosslrt CSWossldevel CSWlibsmi
RUNTIME_DEP_PKGS = CSWlibpcap CSWosslrt CSWlibsmi

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.tcpdump.org/

# No test target for libpcap
TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-crypto=$(prefix)
CONFIGURE_ARGS += --with-smi

# There is a versioned tcpdump, which is not a hardlink. No need for that.
EXTRA_MERGE_EXCLUDE_FILES = $(sbindir)/tcpdump\..*

include gar/category.mk

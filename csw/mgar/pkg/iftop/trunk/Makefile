NAME = iftop
VERSION = 0.17
CATEGORIES = net

DESCRIPTION = Display bandwidth usage on an interface by host
define BLURB
  iftop listens to network traffic on a named interface, or on the first  
  interface it can find which looks like an external interface if none 
  is specified, and displays a table of current bandwidth usage by pairs 
  of hosts.
endef

MASTER_SITES = http://www.ex-parrot.com/~pdw/iftop/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

RUNTIME_DEP_PKGS_CSWiftop += CSWncurses
RUNTIME_DEP_PKGS_CSWiftop += CSWlibpcap1


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-resolver=netdb_1thread

EXTRA_LDFLAGS  = -lpthread

PATCHFILES  = patch-ui.c

TEST_SCRIPTS = 

include gar/category.mk

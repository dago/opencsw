NAME = iftop
VERSION = 0.17
#VERSION = 1.0pre2
CATEGORIES = net

DESCRIPTION = Display bandwidth usage on an interface by host
define BLURB
  iftop listens to network traffic on a named interface, or on the first  
  interface it can find which looks like an external interface if none 
  is specified, and displays a table of current bandwidth usage by pairs 
  of hosts.
endef

MASTER_SITES = http://www.ex-parrot.com/~pdw/iftop/download/
DISTFILES  += $(DISTNAME).tar.gz
PATCHFILES += patch-ui.c

RUNTIME_DEP_PKGS_CSWiftop += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWiftop += CSWlibpcap1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-resolver=netdb_1thread

EXTRA_LDFLAGS  = -lpthread

TEST_SCRIPTS = 

include gar/category.mk

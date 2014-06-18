NAME = iftop
VERSION = 1.0pre4
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Display bandwidth usage on an interface by host
define BLURB
  iftop listens to network traffic on a named interface, or on the first  
  interface it can find which looks like an external interface if none 
  is specified, and displays a table of current bandwidth usage by pairs 
  of hosts.
endef

MASTER_SITES = http://www.ex-parrot.com/~pdw/iftop/download/
DISTFILES  += $(
PATCHFILES += 0003-Add-sys-sockio.h-to-have-SIOCGIFFLAGS.patch

BUILD_DEP_PKGS += CSWlibncurses-dev-autoreconf.patch

RUNTIME_DEP_PKGS_CSWiftop5
RUNTIME_DEP_PKGS_CSWiftop += CSWlibcares2
RUNTIME_DEP_PKGS_CSWiftop += CSWlibpcap1

GARCOMPILER = GCC4

EXTRA_LDFLAGS = -lcares

EXTRA_CPPFLAGS = -I/opt/csw/include/ncurses

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-resolver=ares

include gar/category.mk

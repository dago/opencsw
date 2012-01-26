NAME = iftop
#VERSION = 0.17
VERSION = 1.0pre2
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
DISTFILES  += $(DISTNAME).tar.gz
PATCHFILES += 0001-old-style-patch-patch-ui.c.patch
PATCHFILES += 0002-Omit-static-function-sigalrm.patch
PATCHFILES += 0003-Add-sys-sockio.h-to-have-SIOCGIFFLAGS.patch
PATCHFILES += 0004-Skip-the-parts-not-only-in-Linux-but-also-Solaris.patch

RUNTIME_DEP_PKGS_CSWiftop += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWiftop += CSWlibpcap1

# Because of use of anonymous unions, which are invalid in C (even C99), but valid in C++ with -features=extensions
GARCOMPILER = GNU

EXTRA_LDFLAGS  = -lpthread

CONFIGURE_ARGS  = $(DIRPATHS)
# CONFIGURE_ARGS += --with-resolver=netdb_1thread

# TEST_SCRIPTS = 

include gar/category.mk

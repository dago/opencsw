# TODO
# ! Doesn't compile yet, getopt.h is unhappy about the inclusion of
#   unistd.h (from patch 0002-...)
#
# source='getopt.c' object='getopt.o' libtool=no \
#        DEPDIR=.deps depmode=none /bin/bash ../../depcomp \
#        /opt/studio/SOS11/SUNWspro/bin/cc -DHAVE_CONFIG_H -I. -I../..   -I/opt/csw/include  -xO3 -xarch=386 -DHAVE_SSL -c getopt.c
#"/usr/include/iso/stdio_iso.h", line 165: identifier redeclared: rename
#        current : function(pointer to char, pointer to char) returning int
#        previous: function(pointer to const char, pointer to const char) returning int : "/usr/include/unistd.h", line 382
#"/usr/include/stdio.h", line 265: identifier redeclared: getopt
#        current : function(int, pointer to pointer to char, pointer to char) returning int
#        previous: function(int, pointer to const pointer to char, pointer to const char) returning int : "/usr/include/unistd.h", line 282
#
NAME = httperf
VERSION = 0.9.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A tool for measuring web server performance.
define BLURB
  Httperf is a tool for measuring web server performance. It provides a
  flexible facility for generating various HTTP workloads and for
  measuring server performance.
  
  The focus of httperf is not on implementing one particular benchmark but
  on providing a robust, high-performance tool that facilitates the
  construction of both micro- and macro-level benchmarks. The three
  distinguishing characteristics of httperf are its robustness, which
  includes the ability to generate and sustain server overload, support
  for the HTTP/1.1 and SSL protocols, and its extensibility to new
  workload generators and performance measurements.
endef

VENDOR_URL   = http://code.google.com/p/httperf/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# License taken from one of the .c files in lieu of an official COPYING
DISTFILES   += COPYING

RUNTIME_DEP_PKGS_CSWhttperf += CSWosslrt

# Put source tree -I instructions first so that <event.h> is not picked
# up from -I/opt/csw/lib
PATCHFILES  = 0001-Move-cpp-includes-from-AM_CFLAGS-to-AM_CPPFLAGS.patch
# Avoid implicit declarations for getpid and some str* functions.
# Commented out as unistd.h causes rename()/getopt() redeclarations in getopt.c
#PATCHFILES += 0002-getopt.c-include-header-files-for-getpid-and-strlen-.patch

# Rewrite non-constant subscript in array declaration to make cc happy
PATCHFILES += 0003-avoid-variably-modified-type-in-struct.patch

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk

# Patch 0001 tweaks "Makefile.am"s so we then pull out the autoreconf hammer
pre-configure-modulated:
	autoreconf -fi $(WORKSRC)
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -D $(WORKSRC)/AUTHORS $(DOCDEST)/AUTHORS
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)

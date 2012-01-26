#
# TODO: Consider adding this patch: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=549484

NAME = freehdl
VERSION = 0.0.7
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = A free, open source, GPL'ed VHDL simulator
define BLURB
To develop a VHDL simulator that:
 o Has a graphical waveform viewer.
 o Has a source level debugger.
 o Is VHDL-93 compliant.
 o Is of commercial quality. (on par with, say, V-System - it'll take us a while to get there, but that should be our aim)
 o Is freely distributable - both source and binaries - like Linux itself. (Under the Gnu General Public License (GPL)).
endef

MASTER_SITES = http://freehdl.seul.org/~enaroska/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES  = 0000-Mirring-strings.h-include.patch
PATCHFILES += 0001-Use-OpenCSW-pkg-config.patch
PATCHFILES += fix_seg_fault_2-1.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GNU

#GARFLAVOR           = DBG
CONFIGURE_ARGS      = $(DIRPATHS)
CONFIGURE_ARGS     += $(CONFIGURE_ARGS_$(GARFLAVOR))
CONFIGURE_ARGS_DBG  = --enable-trace --enable-warnings

TEST_SCRIPTS =

RUNTIME_DEP_PKGS = CSWlibtool CSWgcc4corert CSWgcc4g++ CSWgcc4g++rt CSWpkgconfig
#CSWgcc3core CSWgcc3corert CSWgcc3g++ CSWgcc3g++rt

include gar/category.mk

# We want the .la files, freehdl is based around those
MERGE_EXCLUDE_LIBTOOL =

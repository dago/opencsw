GARNAME = freehdl
GARVERSION = 0.0.7
CATEGORIES = devel

DESCRIPTION = A project to develop a free, open source, GPL'ed VHDL simulator for Linux!
define BLURB
To develop a VHDL simulator that:
 o Has a graphical waveform viewer.
 o Has a source level debugger.
 o Is VHDL-93 compliant.
 o Is of commercial quality. (on par with, say, V-System - it'll take us a while to get there, but that should be our aim)
 o Is freely distributable - both source and binaries - like Linux itself. (Under the Gnu General Public License (GPL)).
endef

MASTER_SITES = http://freehdl.seul.org/~enaroska/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES  = 0000-Mirring-strings.h-include.patch
PATCHFILES += 0001-Use-OpenCSW-pkg-config.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

REQUIRED_PKGS = CSWgcc4corert CSWgcc4g++ CSWgcc4g++rt CSWpkgconfig
#CSWgcc3core CSWgcc3corert CSWgcc3g++ CSWgcc3g++rt

include gar/category.mk

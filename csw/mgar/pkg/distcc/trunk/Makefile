GARNAME = distcc
GARVERSION = 3.1
CATEGORIES = devel

DESCRIPTION = A fast, free distributed C/C++ compiler
define BLURB
  distcc is a program to distribute builds of C, C++, Objective
  C or Objective C++ code across several machines on a network.
  distcc should always generate the same results as a local build,
  is simple to install and use, and is usually much faster than a
  local compile.
  distcc does not require all machines to share a filesystem, have
  synchronized clocks, or to have the same libraries or header files
  installed. They can even have different processors or operating
  systems, if cross-compilers are installed. 
endef

MASTER_SITES = http://distcc.googlecode.com/files/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://distcc.googlecode.com/

REQUIRED_PKGS += CSWlibpopt CSWpython

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

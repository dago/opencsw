NAME      = pycairo
VERSION   = 1.8.10
CATEGORIES   = lib
GARTYPE = v2

DESCRIPTION  = Python binding for Cairo library
define BLURB
  This package contains the pycairo Python module which implements
  a binding the the cairo Library.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = py2cairo-$(VERSION).tar.gz

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

PYCOMPILE = 1 
# EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'

PACKAGES = CSWpy-cairo
SPKG_DESC_CSWpy-cairo = $(DESCRIPTION); main
OBSOLETED_BY_CSWpy-cairo = CSWpycairo
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWpython
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWlibcairo2

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = py2cairo-(\d+(?:\.\d+)*).tar.gz

CAIRO_LIBS = -L/opt/csw/lib -R/opt/csw/lib/\$$ISALIST -lcairo
CAIRO_CFLAGS = -I/opt/csw/include -I/opt/csw/include/cairo
EXTRA_CONFIGURE_EXPORTS += CAIRO_LIBS CAIRO_CFLAGS

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk



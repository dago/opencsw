NAME      = pycairo
VERSION   = 1.8.10
CATEGORIES   = lib

DESCRIPTION  = Python binding for Cairo library
define BLURB
  This package contains the pycairo Python module which implements
  a binding the the cairo Library.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = py2cairo-$(VERSION).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
RUNTIME_DEP_PKGS += CSWcswclassutils

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = py2cairo-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWpy-cairo
CATALOGNAME      = py_cairo

RUNTIME_DEP_PKGS = CSWlibcairo CSWpython

CAIRO_LIBS = -L/opt/csw/lib -R/opt/csw/lib/\$$ISALIST -lcairo
CAIRO_CFLAGS = -I/opt/csw/include -I/opt/csw/include/cairo
EXTRA_CONFIGURE_EXPORTS += CAIRO_LIBS CAIRO_CFLAGS
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk



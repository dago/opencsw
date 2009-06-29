GARNAME      = pycairo
GARVERSION   = 1.8.0
CATEGORIES   = lib

DESCRIPTION  = Python binder for Cairo library
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWpycairo CSWpycairodevel

CATALOGNAME_CSWpycairo      = pycairo
CATALOGNAME_CSWpycairodevel = pycairo_devel
SPKG_DESC_CSWpycairo        = $(DESCRIPTION)
SPKG_DESC_CSWpycairodevel   = $(DESCRIPTION) development files

PKGFILES_CSWpycairodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpycairodevel += $(prefix)/include/.*
PKGFILES_CSWpycairodevel += $(prefix)/lib/.*\.a
PKGFILES_CSWpycairodevel += $(prefix)/lib/pkgconfig/.*

REQUIRED_PKGS_CSWpycairodevel = CSWpycairo
REQUIRED_PKGS_CSWpycairo = CSWlibcairo CSWpython

CAIRO_LIBS = -L/opt/csw/lib -R/opt/csw/lib/$$ISALIST
CAIRO_CFLAGS = -I/opt/csw/include -I/opt/csw/include/cairo
COMPILER_EXPORTS += CAIRO_LIBS CAIRO_CFLAGS
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk



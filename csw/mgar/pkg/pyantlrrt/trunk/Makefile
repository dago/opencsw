GARNAME = pyantlrrt
GARVERSION = 3.1.1
CATEGORIES = lib

DESCRIPTION = Python ANTLR runtime
define BLURB
  Python ANTLR runtime, needed for Python ANTLR-generated parsers to run.
endef

MASTER_SITES = http://www.antlr.org/download/Python/
DISTFILES  = antlr_python_runtime-$(GARVERSION).tar.gz

WORKSRC = $(WORKDIR)/antlr_python_runtime-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR) --prefix=$(prefix)

TEST_SCRIPTS =

include gar/category.mk

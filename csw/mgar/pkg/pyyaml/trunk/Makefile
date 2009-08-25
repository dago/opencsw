# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header: $

GARNAME = pyyaml
GARVERSION = 3.08
CATEGORIES = lib

PROJ_NAME = PyYAML

DESCRIPTION = YAML parser and emitter for Python
define BLURB
  PyYAML is a YAML parser and emitter for the Python programming language.

  PyYAML features:
  
  * a complete YAML 1.1 parser. In particular, PyYAML can parse all examples
    from the specification. The parsing algorithm is simple enough to be a
    reference for YAML parser implementors.
  * Unicode support including UTF-8/UTF-16 input/output and \u escape
    sequences.
  * low-level event-based parser and emitter API (like SAX).
  * high-level API for serializing and deserializing native Python
    objects (like DOM or pickle).
  * support for all types from the YAML types repository. A
    simple extension API is provided.
  * both pure-Python and fast LibYAML-based parsers and
    emitters.
  * relatively sensible error messages. 
endef

MASTER_SITES = http://pyyaml.org/download/pyyaml/
DISTFILES  = $(PROJ_NAME)-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(PROJ_NAME)-$(GARVERSION)
SPKG_SOURCEURL = http://pyyaml.org/wiki/PyYAML
SPKG_CLASSES = none cswpycompile

PACKAGES = CSWpyyaml CSWpyyamlrt
CATALOGNAME_CSWpyyaml = py_pyyaml
CATALOGNAME_CSWpyyamlrt = py_pyyaml_rt

REQUIRED_PKGS_CSWpyyaml = CSWpython
REQUIRED_PKGS_CSWpyyamlrt = CSWpython-rt CSWlibyaml
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

ARCHALL_CSWpyyaml = 1
PKGFILES_CSWpyyamlrt = /opt/csw/lib/python/site-packages/.*\.so

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = pyyaml
TEST_SCRIPTS =
INSTALL_SCRIPTS = pyyaml

PROTOTYPE_FILTER = awk ' \
  $$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } \
  { print }'

build-pyyaml:
	(cd $(WORKSRC); $(BUILD_ENV) python setup.py --with-libyaml build)
	@$(MAKECOOKIE)

install-pyyaml:
	(cd $(WORKSRC); $(INSTALL_ENV) python setup.py install --root=$(DESTDIR))
	@$(MAKECOOKIE)

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)

include gar/category.mk

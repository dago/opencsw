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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = pyyaml
TEST_SCRIPTS =
INSTALL_SCRIPTS = pyyaml

build-pyyaml:
	(cd $(WORKSRC); python setup.py build)

install-pyyaml:
	(cd $(WORKSRC); python setup.py install --root=$(DESTDIR))

include gar/category.mk

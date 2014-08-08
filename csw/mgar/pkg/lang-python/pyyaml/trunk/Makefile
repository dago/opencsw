# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header$

NAME = pyyaml
VERSION = 3.11
CATEGORIES = python

PROJ_NAME = PyYAML

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
DISTFILES  = $(PROJ_NAME)-$(VERSION).tar.gz
DISTNAME = $(PROJ_NAME)-$(VERSION)
VENDOR_URL = http://pyyaml.org
LICENSE = LICENSE

PACKAGES = CSWpy-yaml
SPKG_DESC_CSWpy-yaml = YAML parser and emitter for Python
RUNTIME_DEP_PKGS_CSWpy-yaml += CSWlibyaml0-2
RUNTIME_DEP_PKGS_CSWpy-yaml += CSWlibpython2-6-1-0

BUILD_SCRIPTS = py-yaml

GARCOMPILER = SUN

include gar/category.mk

build-py-yaml:
	(cd $(WORKSRC); $(BUILD_ENV) python setup.py --with-libyaml build)
	@$(MAKECOOKIE)

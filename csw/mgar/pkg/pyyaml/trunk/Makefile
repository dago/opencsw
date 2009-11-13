# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header$

GARNAME = pyyaml
GARVERSION = 3.09
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
DISTFILES  = $(PROJ_NAME)-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(PROJ_NAME)-$(GARVERSION)
SPKG_SOURCEURL = http://pyyaml.org/wiki/PyYAML

PACKAGES = CSWpy-yaml CSWpy-yaml-rt
CATALOGNAME_CSWpy-yaml = py_yaml
CATALOGNAME_CSWpy-yaml-rt = py_yaml_rt

REQUIRED_PKGS_CSWpy-yaml =
REQUIRED_PKGS_CSWpy-yaml-rt = CSWpython-rt CSWlibyaml
PREREQUISITE_PKGS = $(REQUIRED_PKGS_CSWpy-yaml) $(REQUIRED_PKGS_CSWpy-yaml-rt)

SPKG_DESC_CSWpy-yaml = YAML parser and emitter for Python
SPKG_DESC_CSWpy-yaml-rt = Runtime libraries for YAML parser and emitter

ARCHALL_CSWpy-yaml = 1
PKGFILES_CSWpy-yaml-rt = /opt/csw/lib/python/site-packages/.*\.so

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_SCRIPTS = py-yaml

build-py-yaml:
	(cd $(WORKSRC); $(BUILD_ENV) python setup.py --with-libyaml build)
	@$(MAKECOOKIE)

include gar/category.mk

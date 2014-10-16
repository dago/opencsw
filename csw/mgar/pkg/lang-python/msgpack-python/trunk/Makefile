NAME = msgpack-python
VERSION = 0.4.2
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = MessagePack (de)serializer for Python.
define BLURB
	MessagePack is a binary-based efficient data interchange format that is
	focused on high performance. It is like JSON, but very fast and small.
endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://pypi.python.org/pypi/msgpack-python/

# Python 2.6 was built with Sun Studio which has problems with msgpack
SKIP_MODULATIONS += isa-sparc-python_version-2_6
SKIP_MODULATIONS += isa-i386-python_version-2_6

RUNTIME_DEP_PKGS_CSWpy-msgpack-python += $(RUNTIME_DEP_PKGS_CSWpy-msgpack-python-$(GAROSREL))
RUNTIME_DEP_PKGS_CSWpy-msgpack-python += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-msgpack-python += CSWlibgcc-s1

CHECKPKG_OVERRIDES_CSWpy-msgpack-python += python-package-missing-py26-files

PATCHFILES += 0001-dont-use-stdbool-and-use-inttypes-on-solaris9.patch

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

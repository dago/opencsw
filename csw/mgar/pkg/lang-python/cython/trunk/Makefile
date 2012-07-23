# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Cython
VERSION = 0.16
GARTYPE = v2
CATEGORIES = lang

DESCRIPTION = Cython Compiler
define BLURB
  The Cython language makes writing C extensions for the Python language as easy as Python itself. Cython is a source code translator based on the well-known Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python language (and most Python code is also valid Cython code), but Cython additionally supports calling C functions and declaring C types on variables and class attributes. This allows the compiler to generate very efficient C code from Cython code.

This makes Cython the ideal language for writing glue code for external C libraries, and for fast C modules that speed up the execution of Python code.
endef

MASTER_SITES = http://pypi.python.org/packages/source/C/Cython/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS += Solaris10-sparc Solaris10-i386
GARCOMPILER = SOS12U3

LICENSE = LICENSE.txt

REINPLACE_USRLOCAL = $(libdir)/python/site-packages/pyximport/pyximport.py
REINPLACE_WHEN_USRLOCAL = postinstall

PACKAGES += CSWcython
RUNTIME_DEP_PKGS_CSWcython += CSWpython
RUNTIME_DEP_PKGS_CSWcython += CSWlibpython2-6-1-0

PYCOMPILE = 1
STRIP_LIBTOOL = 1
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk


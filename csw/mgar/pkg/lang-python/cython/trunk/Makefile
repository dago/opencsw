# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Cython
VERSION = 0.18
CATEGORIES = lang

DESCRIPTION = Cython Comp
The Cython language makes writing C extensions for the Python language as easy
as Python itself. Cython is a source code translator based on the well-known
on the well-known Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python language (an
is also valid Cython code), but Cython additionally supports calling
C functions and declaring C types on variables and class attributes. This
 attributes. This allows the compiler to generate very efficient C code from Cython code.

This makes Cython the ideal language for writing glue
C libraries, and for fast C modules that speed up the execution of Python
code.

endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz
arc Solaris10-i386
GARCOMPILER = SOS12U3

LICENSE = LICENSE.txt

REINPLACE_USRLOCAL = $(libdir)/python/site-packages/pyximport/pyximport.py
REINPLACE_WHEN_USRLOCAL = postnstall

PACKAGES += CSWcython
RUNTIME_DEP_PKGS_CSWcython += CSWpython
RUNTIME_DEP_PKGS_CSWcython += CSWlibpython2-6-1-0

PYCOMPILE = 1
STRIP_LIBTOOL = 1
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .PATHS)

CNFIGURE_SCRIPTS= 
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --CHECKPKG_OVERRIDES_CSWcython += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcython += catalogname-does-not-start-with-py_

include gar/category.mk


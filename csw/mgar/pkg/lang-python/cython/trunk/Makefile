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

CATEGORIES = python
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = LICENSE.txt

REINPLACE_USRLOCAL = $(libdir)/python/site-packages.*thon/site-packages/pyximport/pyximport.py
REINPLACE_WHEN_USRLOCAL = postnstall

PACKAGES += CSWcython
RUNTIME_DEP_PKGlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWcython += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWcython += CSWlibgcc-s1

TEST_SCRIPTS =
STRIP_LIBTOOL = 1--CHECKPKG_OVERRIDES_CSWcython += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcython += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWcython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/pyximport/pyximport.py
CHECKPKG_OVERRIDES_CSWcython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/pyximport/pyximport.py

include gar/category.mk

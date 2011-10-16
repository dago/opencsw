# $Id$

NAME = Python
VERSION = 3.2.2
CATEGORIES = lang
VER = 3.2
DVER = 3-2
UVER = 3_2
PVER = python$(VER)
CVER = 32

# Known issues:
#
# - No 64-bit build
# - ctypes module doesn't compile
#   - http://forums.sun.com/thread.jspa?threadID=5148204
#   - http://bugs.python.org/issue4902
#     - Python-2.6.1/Modules/_ctypes/libffi/src/x86/sysv.S

SPKG_SOURCEURL = http://python.org/download/releases/$(VERSION)

DESCRIPTION = A high-level scripting language.
define BLURB
  Python is an interpreted, interactive, object-oriented programming language.
  It combines remarkable power with very clear syntax, and isnt difficult to
  learn.  It has modules, classes, exceptions, very high level data types, and
  dynamic typing. There are interfaces to many system calls and libraries, as
  well as to various windowing systems (Tk, Mac, MFC, GTK+, Qt, wxWindows).
  Newbuilt-in modules are easily written in C or C++. Python is also usable as
  an extension language for applications that need a programmable interface.
endef

MASTER_SITES = http://python.org/ftp/python/$(VERSION)/
UPSTREAM_MASTER_SITES = http://python.org/ftp/python/

DISTFILES  = $(DISTNAME).tar.bz2

# Patches
PATCHFILES += makesetup.diff
PATCHFILES += modules.diff
PATCHFILES += multiprocess.diff

# The test for sunaudiodev fails.  Not that it's a good practice to skip
# tests.
SKIPTEST = 1

# There is a file name conflict over libffi.so symlink between libffi package
# and a gcc-java package.  While it will ultimately belong to libffi_dev, the
# symlink is currently under a subdirectory.
# pkgchk -L CSWlibffi-dev
# (...)
# /opt/csw/lib/ffi/libffi.so=../libffi.so.5.0.10 s none CSWlibffi-dev
EXTRA_LIB += $(libdir)/ffi

BASECFLAGS = $(CFLAGS)
EXTRA_COMMON_EXPORTS = BASECFLAGS

NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-unicode=ucs4
CONFIGURE_ARGS += --without-gcc
CONFIGURE_ARGS += --with-signal-module
CONFIGURE_ARGS += --with-fpectl
CONFIGURE_ARGS += --with-system-ffi

# This doesn't work here, as _PYCOMPILE_FILES is not the directory Python uses.
# PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc
# use prototype filters to set the class 
PROTOTYPE_FILTER = awk '$$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'

PACKAGES  = CSWidle$(CVER)
SPKG_DESC_CSWidle$(CVER)         = Python IDE
CHECKPKG_OVERRIDES_CSWidle$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += catalogname-does-not-start-with-py_
PKGFILES_CSWidle$(CVER) += $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle$(CVER) += $(bindir)/idle
ARCHALL_CSWidle$(CVER)        = 1
RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)-tk
# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)-tk
CHECKPKG_OVERRIDES_CSWidle$(CVER) += file-with-bad-content

# The main Python package. PKGFILES is not set, because it's the catch-all
# package.
PACKAGES += CSWpython$(CVER)
SPKG_DESC_CSWpython$(CVER)       = A high-level scripting language, $(VER) series
INCOMPATIBLE_PKGS_CSWpython$(CVER) = CSWpydistutils
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibffi5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgdbm3
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWosslrt
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpanel5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibreadline6

CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += file-with-bad-content

PACKAGES += CSWpython$(CVER)-test
SPKG_DESC_CSWpython$(CVER)-test  = Python Test modules
PKGFILES_CSWpython$(CVER)-test  = $(libdir)/$(PVER)/test/.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/bsddb/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/ctypes/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/email/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/distutils/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/json/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/lib2to3/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/sqlite3/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/unittest/test.*
RUNTIME_DEP_PKGS_CSWpython$(CVER)-test  += CSWpython$(CVER)
ARCHALL_CSWpython$(CVER)-test = 1
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += file-with-bad-content

PACKAGES += CSWpython$(CVER)-tk
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Interface (TkInter)
PKGFILES_CSWpython$(CVER)-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWtcl
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWtk 
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython$(CVER)

PACKAGES += CSWlibpython$(DVER)-1-0
SPKG_DESC_CSWlibpython$(DVER)-1-0  = Python shared library ($(VER))
PKGFILES_CSWlibpython$(DVER)-1-0 += $(call baseisadirs,$(libdir),libpython$(VER)\.so\.1\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibpython$(DVER)-1-0 += CSWlibintl8

# Devel package
OBSOLETED_BY_CSWpython$(CVER)-dev = CSWpython$(CVER)-devel
PACKAGES += CSWpython$(CVER)-dev
SPKG_DESC_CSWpython$(CVER)-dev = Development Files for Python
# /opt/csw/include/python$(VER)/pyconfig.h is necessary for Python to start up
PKGFILES_CSWpython$(CVER)-dev += $(includedir)/$(PVER)/(?!pyconfig\.h).*
PKGFILES_CSWpython$(CVER)-dev += $(bindir)/.*config.*
PKGFILES_CSWpython$(CVER)-dev += $(libdir)/pkgconfig.*
PKGFILES_CSWpython$(CVER)-dev += $(libdir)/libpython$(VER).so
# No idea why would this be in CSWpython, and no good idea for a better package
# to put it.
PKGFILES_CSWpython$(CVER)-dev += $(bindir)/smtpd.py-$(VER)

RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWlibpython$(DVER)-1-0
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += catalogname-does-not-start-with-py_

BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWggettext-dev

LICENSE = LICENSE

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += catalogname-does-not-start-with-py_

# To avoid file collisions with CSWpython:
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/idle,$(bindir)/idle-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/smtpd.py,$(bindir)/smtpd.py-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/pydoc,$(bindir)/pydoc-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/2to3,$(bindir)/2to3-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/python-config,$(bindir)/python-config-$(VER),'
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python

include gar/category.mk

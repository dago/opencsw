# $Id$

NAME = Python
VERSION = 3.3.0
VER = 3.3
DVER = 3-3
UVER = 3_3
PVER = python$(VER)
CVER = 33

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
PATCHFILES += 0004-Use-PY_CPPFLAGS-in-Modules-makesetup.patch

# The test for sunaudiodev fails.  Not that it's a good practice to skip
# tests.
SKIPTEST = 1
TEST_TARGET = test

BUILD64 = 1
ISAEXEC = 1

# There is a file name conflict over libffi.so symlink between libffi package
# and a gcc-java package.  While it will ultimately belong to libffi_dev, the
# symlink is currently under a subdirectory.
# pkgchk -L CSWlibffi-dev
# (...)
# /opt/csw/lib/ffi/libffi.so=../libffi.so.5.0.10 s none CSWlibffi-dev
EXTRA_LIB += $(libdir)/ffi

# BASECFLAGS = $(CFLAGS)
BASECFLAGS = -g -O2
EXTRA_COMMON_EXPORTS = BASECFLAGS
EXTRA_LINKER_FLAGS = -lsocket -lresolv -lrt

NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-ipv6
# CONFIGURE_ARGS += --without-gcc
CONFIGURE_ARGS += --with-signal-module
CONFIGURE_ARGS += --with-fpectl
CONFIGURE_ARGS += --with-system-ffi

# This doesn't work here, as _PYCOMPILE_FILES is not the directory Python uses.
# PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc
# use prototype filters to set the class
# Do not use 2.6 pycompile for 3.3.
# PROTOTYPE_FILTER = awk '$$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'


PACKAGES  = CSWidle$(CVER)
SPKG_DESC_CSWidle$(CVER)         = Python IDE
CHECKPKG_OVERRIDES_CSWidle$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWidle$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER) += catalogname-does-not-start-with-py_
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
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibffi4
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWliblzma5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpanel5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpython$(DVER)m1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibz1

CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += file-with-bad-content

# Don't merge test files.
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/test
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/test/.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/bsddb/test.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/ctypes/test.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/email/test.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/distutils/tests.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/json/tests.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/lib2to3/tests.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/sqlite3/test.*
MERGE_EXCLUDE_FILES += /opt/csw/lib/$(PVER)/unittest/test.*

PACKAGES += CSWpython$(CVER)-tk
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Interface (TkInter)
PKGFILES_CSWpython$(CVER)-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibpython$(DVER)m1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWpython$(CVER)

CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython$(CVER)

PACKAGES += CSWlibpython$(DVER)m1-0
CATALOGNAME_CSWlibpython$(DVER)m1-0 = libpython$(UVER)m1_0
PKGFILES_CSWlibpython$(DVER)m1-0 += $(call baseisadirs,$(libdir),libpython3\.3m\.so\.1\.0)
PKGFILES_CSWlibpython$(DVER)m1-0 += $(call baseisadirs,$(libdir),libpython3\.3m\.so\.1\.0(\.\d+)*)
SPKG_DESC_CSWlibpython$(DVER)m1-0 += $(DESCRIPTION), libpython$(VER)m.so.1.0
RUNTIME_DEP_PKGS_CSWlibpython$(DVER)m1-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpython$(DVER)m1-0 += CSWlibgcc-s1

# This package looks dodgy to me. The soname-equals-filename is something that
# caused us a lot of grief with libnet.
PACKAGES += CSWlibpython3
PKGFILES_CSWlibpython3 += $(call baseisadirs,$(libdir),libpython3\.so)
SPKG_DESC_CSWlibpython3 += $(DESCRIPTION), libpython3.so
CHECKPKG_OVERRIDES_CSWlibpython3 += soname-equals-filename|file=/opt/csw/lib/libpython3.so
CHECKPKG_OVERRIDES_CSWlibpython3 += soname-equals-filename|file=/opt/csw/lib/sparcv9/libpython3.so
CHECKPKG_OVERRIDES_CSWlibpython3 += soname-equals-filename|file=/opt/csw/lib/amd64/libpython3.so
RUNTIME_DEP_PKGS_CSWlibpython3 += CSWlibgcc-s1

# Devel package
PACKAGES += CSWpython$(CVER)-dev
SPKG_DESC_CSWpython$(CVER)-dev = Development Files for Python 3.x
# /opt/csw/include/python$(VER)/pyconfig.h is necessary for Python to start up
PKGFILES_CSWpython$(CVER)-dev += $(includedir)/$(PVER)/(?!pyconfig\.h).*
PKGFILES_CSWpython$(CVER)-dev += $(bindir)/.*config.*
PKGFILES_CSWpython$(CVER)-dev += $(libdir)/pkgconfig.*
PKGFILES_CSWpython$(CVER)-dev += $(call baseisadirs,$(libdir),libpython$(VER)m.so)
# No idea why would this be in CSWpython, and no good idea for a better package
# to put it.
PKGFILES_CSWpython$(CVER)-dev += $(bindir)/smtpd.py-$(VER)

RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWlibpython$(DVER)m1-0
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += catalogname-does-not-start-with-py_

BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
# Because of /opt/csw/lib/libxtermcap.a
BUILD_DEP_PKGS += CSWschilybase

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

GARCOMPILER = GNU

include gar/category.mk

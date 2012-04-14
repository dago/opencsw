# $Id$

NAME = Python
VERSION = 2.7.3
CATEGORIES = lang
VER = 2.7
DVER = 2-7
UVER = 2_7
PVER = python$(VER)
CVER = 27

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

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Patches
PATCHFILES += faqwiz.diff
PATCHFILES += makesetup.diff
PATCHFILES += modules.diff
PATCHFILES += multiprocess.diff
PATCHFILES += pyport.diff
# This patch needs to go away
# PATCHFILES += site.diff
PATCHFILES += python-config-in.diff
PATCHFILES += setup.diff
# PATCHFILES += 0001-FFI_DEFAULT_ABI-to-use-__i386.patch

# Test for sunaudiodev fails.
SKIPTEST = 1


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
PACKAGES += CSWpython$(CVER)
PACKAGES += CSWpython$(CVER)-test
PACKAGES += CSWpython$(CVER)-tk


PACKAGES += CSWlibpython$(DVER)-1-0
CATALOGNAME_CSWlibpython$(DVER)-1-0  = libpython$(UVER)_1_0
PKGFILES_CSWlibpython$(DVER)-1-0 += $(call baseisadirs,$(libdir),libpython$(DVER)\.so\.1\.0(\.\d+)*)
PKGFILES_CSWlibpython$(DVER)-1-0 += $(libdir)/$(PVER)\.so\.([0-9\.]+)
SPKG_DESC_CSWlibpython$(DVER)-1-0  = Python shared library ($(VER))

INCOMPATIBLE_PKGS_CSWpython$(CVER) = CSWpydistutils

# Devel package
PACKAGES += CSWpython$(CVER)-dev
CATALOGNAME_CSWpython$(CVER)-dev = python_$(CVER)_dev
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

PKGFILES_CSWidle$(CVER) += $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle$(CVER) += $(bindir)/idle
PKGFILES_CSWpython$(CVER)-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
PKGFILES_CSWpython$(CVER)-test  = $(libdir)/$(PVER)/test/.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/bsddb/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/ctypes/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/email/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/distutils/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/json/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/lib2to3/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/sqlite3/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/$(PVER)/unittest/test.*

ARCHALL_CSWpython$(CVER)-test = 1
ARCHALL_CSWidle$(CVER)        = 1

RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)-tk
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWbzip2
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWgdbm
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWggettextrt 
# Was once needed, may need revisiting.
# RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibffi
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWncurses
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWosslrt
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWreadline 
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWzlib
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWtcl
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWtk 
RUNTIME_DEP_PKGS_CSWpython$(CVER)-test  += CSWpython$(CVER)

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)-tk

CATALOGNAME_CSWidle$(CVER)         = idle_$(CVER)
CATALOGNAME_CSWpython$(CVER)       = python_$(CVER)
CATALOGNAME_CSWpython$(CVER)-tk    = python_$(CVER)_tk
CATALOGNAME_CSWpython$(CVER)-test  = python_$(CVER)_test

SPKG_DESC_CSWidle$(CVER)         = Python IDE
SPKG_DESC_CSWpython$(CVER)       = A high-level scripting language, $(VER) series
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Interface (TkInter)
SPKG_DESC_CSWpython$(CVER)-test  = Python Test modules

CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWidle$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += missing-dependency|CSWpython

LICENSE = LICENSE

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython$(CVER)

# Checkpkg does not understand relocatable packages.
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/$(PVER)/lib-dynload/gdbm.so
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/$(PVER)/lib-dynload/_gdbm.so
CHECKPKG_OVERRIDES_CSWpython$(CVER) += surplus-dependency|CSWgdbm

# To avoid file collisions with CSWpython:
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/idle,$(bindir)/idle-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/smtpd.py,$(bindir)/smtpd.py-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/pydoc,$(bindir)/pydoc-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/2to3,$(bindir)/2to3-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/python-config,$(bindir)/python-config-$(VER),'
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python

include gar/category.mk

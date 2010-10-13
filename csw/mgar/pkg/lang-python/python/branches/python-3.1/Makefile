# $Id$

GARNAME = Python
GARVERSION = 3.1.2
CATEGORIES = lang

# Known issues:
#
# - No 64-bit build
# - ctypes module doesn't compile
#   - http://forums.sun.com/thread.jspa?threadID=5148204

SPKG_SOURCEURL = http://python.org/download/releases/$(GARVERSION)

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

MASTER_SITES = http://python.org/ftp/python/$(GARVERSION)/
UPSTREAM_MASTER_SITES = http://python.org/ftp/python/

DISTFILES  = $(DISTNAME).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Patches
PATCHFILES += faqwiz.diff
PATCHFILES += makesetup.diff
PATCHFILES += modules.diff
PATCHFILES += multiprocess.diff
# PATCHFILES += pyport.diff
# PATCHFILES += site.diff
# PATCHFILES += python-config-in.diff
# PATCHFILES += setup.diff

# Test for sunaudiodev fails.
SKIPTEST = 1

EXTRA_INC += $(prefix)/X11/include
EXTRA_LIB += $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

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
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
# use prototype filters to set the class 
PROTOTYPE_FILTER = awk '$$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'

PACKAGES  = CSWidle31
PACKAGES += CSWpython31
PACKAGES += CSWpython31-devel
PACKAGES += CSWpython31-test
PACKAGES += CSWpython31-tk

INCOMPATIBLE_PKGS_CSWpython31 = CSWpydistutils

PKGFILES_CSWidle31  = $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle31 += $(bindir)/idle
PKGFILES_CSWpython31-devel  = $(includedir)/.*
PKGFILES_CSWpython31-devel += $(libdir)/.*/config/.*
PKGFILES_CSWpython31-devel += $(bindir)/.*config.*
# No idea why would this be in CSWpython31, and no good idea for a better package
# to put it.
PKGFILES_CSWpython31-devel += $(bindir)/smtpd.py
PKGFILES_CSWpython31-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython31-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
PKGFILES_CSWpython31-test  = $(libdir)/python/test/.*
PKGFILES_CSWpython31-test += $(libdir)/python/bsddb/test.*
PKGFILES_CSWpython31-test += $(libdir)/python/ctypes/test.*
PKGFILES_CSWpython31-test += $(libdir)/python/email/test.*
PKGFILES_CSWpython31-test += $(libdir)/python/distutils/tests.*
PKGFILES_CSWpython31-test += $(libdir)/python/json/tests.*
PKGFILES_CSWpython31-test += $(libdir)/python/lib2to3/tests.*
PKGFILES_CSWpython31-test += $(libdir)/python/sqlite3/test.*

ARCHALL_CSWpython31-test = 1
ARCHALL_CSWidle31        = 1

RUNTIME_DEP_PKGS_CSWidle31         += CSWpython31
RUNTIME_DEP_PKGS_CSWidle31         += CSWpython31-tk
RUNTIME_DEP_PKGS_CSWpython31       += CSWbzip2
RUNTIME_DEP_PKGS_CSWpython31       += CSWgdbm
RUNTIME_DEP_PKGS_CSWpython31       += CSWggettextrt 
RUNTIME_DEP_PKGS_CSWpython31       += CSWncurses
RUNTIME_DEP_PKGS_CSWpython31       += CSWosslrt
RUNTIME_DEP_PKGS_CSWpython31       += CSWreadline 
RUNTIME_DEP_PKGS_CSWpython31       += CSWsqlite3rt CSWzlib
RUNTIME_DEP_PKGS_CSWpython31-tk    += CSWpython31
RUNTIME_DEP_PKGS_CSWpython31-tk    += CSWtcl
RUNTIME_DEP_PKGS_CSWpython31-tk    += CSWtk 
RUNTIME_DEP_PKGS_CSWpython31-tk    += CSWlibx11
RUNTIME_DEP_PKGS_CSWpython31-devel += CSWpython31
RUNTIME_DEP_PKGS_CSWpython31-test  += CSWpython31

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle31 += surplus-dependency|CSWpython31-tk

CATALOGNAME_CSWidle31         = idle_31
CATALOGNAME_CSWpython31       = python_31
CATALOGNAME_CSWpython31-devel = python_31_devel
CATALOGNAME_CSWpython31-tk    = python_31_tk
CATALOGNAME_CSWpython31-test  = python_31_test

SPKG_DESC_CSWidle31         = Python IDE
SPKG_DESC_CSWpython31       = A high-level scripting language, 3.1 series
SPKG_DESC_CSWpython31-devel = Development Files for Python
SPKG_DESC_CSWpython31-tk    = Python Tk Interface (TkInter)
SPKG_DESC_CSWpython31-test  = Python Test modules

CHECKPKG_OVERRIDES_CSWpython31 += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython31-test += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython31-test += surplus-dependency|CSWpython31
CHECKPKG_OVERRIDES_CSWidle31 += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle31 += surplus-dependency|CSWpython31
CHECKPKG_OVERRIDES_CSWpython31-devel += surplus-dependency|CSWpython31

LICENSE = LICENSE

include gar/category.mk

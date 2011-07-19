# $Id$

NAME = Python
VERSION = 2.6.6
CATEGORIES = lang

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

# Previous Library for compatability
DISTFILES += libpython2.5.so.1.0-isa-sparcv8
DISTFILES += libpython2.5.so.1.0-isa-i386

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Patches
PATCHFILES += faqwiz.diff
PATCHFILES += makesetup.diff
PATCHFILES += modules.diff
PATCHFILES += multiprocess.diff
PATCHFILES += pyport.diff
PATCHFILES += site.diff
PATCHFILES += python-config-in.diff
PATCHFILES += setup.diff
PATCHFILES += 0001-FFI_DEFAULT_ABI-to-use-__i386.patch

# Test for sunaudiodev fails.
SKIPTEST = 1

EXTRA_INC += $(prefix)/bdb47/include
EXTRA_LIB += $(prefix)/bdb47/lib

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

PACKAGES  = CSWidle
PACKAGES += CSWpython
PACKAGES += CSWpython-devel
PACKAGES += CSWpython-test
PACKAGES += CSWpython-tk
PACKAGES += CSWlibpython2-5-1-0
PACKAGES += CSWlibpython2-6-1-0

INCOMPATIBLE_PKGS_CSWpython = CSWpydistutils

PKGFILES_CSWidle  = $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle += $(bindir)/idle
PKGFILES_CSWpython-devel  = $(includedir)/.*
PKGFILES_CSWpython-devel += $(libdir)/.*/config/.*
PKGFILES_CSWpython-devel += $(bindir)/.*config.*
PKGFILES_CSWpython-devel += $(libdir)/libpython2.6.so
# No idea why would this be in CSWpython, and no good idea for a better package
# to put it.
PKGFILES_CSWpython-devel += $(bindir)/smtpd.py
PKGFILES_CSWpython-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
PKGFILES_CSWpython-test  = $(libdir)/python/test/.*
PKGFILES_CSWpython-test += $(libdir)/python/bsddb/test.*
PKGFILES_CSWpython-test += $(libdir)/python/ctypes/test.*
PKGFILES_CSWpython-test += $(libdir)/python/email/test.*
PKGFILES_CSWpython-test += $(libdir)/python/distutils/tests.*
PKGFILES_CSWpython-test += $(libdir)/python/json/tests.*
PKGFILES_CSWpython-test += $(libdir)/python/lib2to3/tests.*
PKGFILES_CSWpython-test += $(libdir)/python/sqlite3/test.*
PKGFILES_CSWlibpython2-5-1-0 += $(libdir)/libpython2\.5\.so\..*
PKGFILES_CSWlibpython2-6-1-0 += $(libdir)/libpython2\.6\.so\..*

ARCHALL_CSWpython-test = 1
ARCHALL_CSWidle        = 1

RUNTIME_DEP_PKGS_CSWidle         += CSWpython
RUNTIME_DEP_PKGS_CSWidle         += CSWpython-tk
RUNTIME_DEP_PKGS_CSWpython       += CSWbdb47
RUNTIME_DEP_PKGS_CSWpython       += CSWbzip2
RUNTIME_DEP_PKGS_CSWpython       += CSWgdbm
RUNTIME_DEP_PKGS_CSWpython       += CSWggettextrt 
RUNTIME_DEP_PKGS_CSWpython       += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpython       += CSWncurses
RUNTIME_DEP_PKGS_CSWpython       += CSWosslrt
RUNTIME_DEP_PKGS_CSWpython       += CSWreadline 
RUNTIME_DEP_PKGS_CSWpython       += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWpython       += CSWzlib
RUNTIME_DEP_PKGS_CSWpython-tk    += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpython-tk    += CSWpython
RUNTIME_DEP_PKGS_CSWpython-tk    += CSWtcl
RUNTIME_DEP_PKGS_CSWpython-tk    += CSWtk 
RUNTIME_DEP_PKGS_CSWpython-devel += CSWpython
RUNTIME_DEP_PKGS_CSWpython-test  += CSWpython

# There are packages depending on libpython2.5, and listing CSWpython as the
# dependency.
RUNTIME_DEP_PKGS_CSWpython               += CSWlibpython2-5-1-0

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle += surplus-dependency|CSWpython-tk

CATALOGNAME_CSWidle         = idle
CATALOGNAME_CSWpython       = python
CATALOGNAME_CSWpython-devel = python_devel
CATALOGNAME_CSWpython-tk    = python_tk
CATALOGNAME_CSWpython-test  = python_test
CATALOGNAME_CSWlibpython2-5-1-0  = libpython2_5_1_0
CATALOGNAME_CSWlibpython2-6-1-0  = libpython2_6_1_0

SPKG_DESC_CSWidle              = Python IDE
SPKG_DESC_CSWpython            = A high-level scripting language.
SPKG_DESC_CSWpython-devel      = Development Files for Python
SPKG_DESC_CSWpython-tk         = Python Tk Interface (TkInter)
SPKG_DESC_CSWpython-test       = Python Test modules
SPKG_DESC_CSWlibpython2-5-1-0  = Python shared library (2.5)
SPKG_DESC_CSWlibpython2-6-1-0  = Python shared library (2.6)

LICENSE = LICENSE

# These won't be fixed.
CHECKPKG_OVERRIDES_CSWlibpython2-5-1-0 += file-with-bad-content

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWpython-test  += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython-test  += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython-tk    += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython-tk    += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWidle         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle         += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython-devel += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython-devel += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython       += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython       += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython       += surplus-dependency|CSWlibpython2-5-1-0

include gar/category.mk

post-install-modulated: install-deprecated-libs
	@$(MAKECOOKIE)

install-deprecated-libs:
	echo "===> Installing deprecated Libraries into $(libdir)"
	cp $(DOWNLOADDIR)/libpython2.5.so.1.0-$(MODULATION) \
		$(DESTDIR)$(libdir)/libpython2.5.so.1.0
	cd $(DESTDIR)$(libdir); ln -s libpython2.5.so.1.0 libpython2.5.so
	@$(MAKECOOKIE)

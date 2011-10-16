# $Id: Makefile 14947 2011-06-30 14:55:12Z wahwah $

NAME = Python
VERSION = 3.2.2
CATEGORIES = lang
VER = 3.2
DVER = 3-2
UVER = 3_2
PVER = python$(VER)
CVER =

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
#PATCHFILES += faqwiz.diff
#PATCHFILES += makesetup.diff
#PATCHFILES += modules.diff
#PATCHFILES += multiprocess.diff
#PATCHFILES += pyport.diff
#PATCHFILES += site.diff
#PATCHFILES += python-config-in.diff
#PATCHFILES += setup.diff
#PATCHFILES += 0001-FFI_DEFAULT_ABI-to-use-__i386.patch
# PATCHFILES += 0010-Hardcoding-the-use-of-libffi.patch
# PATCHFILES += 0011-OpenCSW-specific-libffi-include-dir.patch
# PATCHFILES += 0012-temporary-hack-to-compile-against-system-ffi.patch
#PATCHFILES += 0013-Use-opt-csw-bin-python-in-cgi.py.patch
#PATCHFILES += 0015-Adding-opt-csw-lib-to-dyld.py.patch
#PATCHFILES += 0016-CSW-mimetypes.patch
#PATCHFILES += 0017-Random-insignificant-removals-of-usr-local.patch
#PATCHFILES += 0018-Removing-usr-local-from-mailcap.patch

# Test for sunaudiodev fails.
SKIPTEST = 1

EXTRA_INC += $(prefix)/bdb47/include
EXTRA_LIB += $(prefix)/bdb47/lib

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
PACKAGES += CSWpython$(CVER)
PACKAGES += CSWpython$(CVER)-dev
PACKAGES += CSWpython$(CVER)-test
PACKAGES += CSWpython$(CVER)-tk
PACKAGES += CSWlibpython$(DVER)-1-0
CATALOGNAME_CSWlibpython$(DVER)-1-0 = libpython$(UVER)_1_0
PKGFILES_CSWlibpython$(DVER)-1-0 += $(call baseisadirs,$(libdir),libpython$(VER)\.so\.1\.0(\.\d+)*)
SPKG_DESC_CSWlibpython$(DVER)-1-0  = Python shared library ($(VER))

INCOMPATIBLE_PKGS_CSWpython$(CVER) = CSWpydistutils

PKGFILES_CSWidle$(CVER)  = $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle$(CVER) += $(bindir)/idle
PKGFILES_CSWpython$(CVER)-dev  = $(includedir)/.*
PKGFILES_CSWpython$(CVER)-dev += $(libdir)/.*/config/.*
PKGFILES_CSWpython$(CVER)-dev += $(bindir)/.*config.*
PKGFILES_CSWpython$(CVER)-dev += $(libdir)/libpython$(VER).so
# No idea why would this be in CSWpython, and no good idea for a better package
# to put it.
PKGFILES_CSWpython$(CVER)-dev += $(bindir)/smtpd.py

PKGFILES_CSWpython$(CVER)-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
PKGFILES_CSWpython$(CVER)-test  = $(libdir)/python/test/.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/bsddb/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/ctypes/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/email/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/distutils/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/json/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/lib2to3/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python/sqlite3/test.*

ARCHALL_CSWpython$(CVER)-test = 1
ARCHALL_CSWidle$(CVER)        = 1

RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)-tk
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgdbm3
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpanel5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWosslrt
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibreadline6 
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-test  += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWtcl
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWtk 

BUILD_DEP_PKGS += CSWlibffi-dev

# There are packages depending on libpython2.5, and listing CSWpython as the
# dependency.
RUNTIME_DEP_PKGS_CSWpython               += CSWlibpython3-2-1-0
CHECKPKG_OVERRIDES_CSWpython       += surplus-dependency|CSWlibpython3-2-1-0

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)-tk

CATALOGNAME_CSWidle$(CVER)         = idle
CATALOGNAME_CSWpython$(CVER)       = python
CATALOGNAME_CSWpython$(CVER)-dev = python$(CVER)_dev
CATALOGNAME_CSWpython$(CVER)-tk    = python$(CVER)_tk
CATALOGNAME_CSWpython$(CVER)-test  = python$(CVER)_test

SPKG_DESC_CSWidle$(CVER)         = Python IDE
SPKG_DESC_CSWpython$(CVER)       = A high-level scripting language, $(VER) series
SPKG_DESC_CSWpython$(CVER)-dev = Development Files for Python
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Interface (TkInter)
SPKG_DESC_CSWpython$(CVER)-test  = Python Test modules

LICENSE = LICENSE

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += catalogname-does-not-start-with-py_
#CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += pkgname-does-not-start-with-CSWpy-
#CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += catalogname-does-not-start-with-py_
#CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += pkgname-does-not-start-with-CSWpy-
#CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython += file-collision|/opt/csw/lib/pkgconfig/python3.pc|CSWpython|CSWpython31-dev
CHECKPKG_OVERRIDES_CSWpython += file-collision|/opt/csw/bin/python3|CSWpython|CSWpython31

CHECKPKG_OVERRIDES_CSWpython-tk += surplus-dependency|CSWlibpython3-2-1-0
CHECKPKG_OVERRIDES_CSWpython-tk += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle += file-with-bad-content|/usr/share|root/opt/csw/lib/python3.2/idlelib/EditorWindow.py
CHECKPKG_OVERRIDES_CSWidle += file-with-bad-content|/usr/share|root/opt/csw/lib/python3.2/idlelib/config-main.def
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/trace.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/site.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/mailcap.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/cgi.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/mimetypes.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/ctypes/macholib/dyld.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/pydoc_data/topics.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/config-3.2m/Makefile
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/config-3.2m/Setup
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/distutils/unixccompiler.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python3.2/test/test_subprocess.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/python3.2.1
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/share|root/opt/csw/lib/python3.2/test/test_posixpath.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/share|root/opt/csw/lib/python3.2/test/cfgparser.2
CHECKPKG_OVERRIDES_CSWpython += wrong-docdir|expected=/opt/csw/shared/doc/python/...|in-package=/opt/csw/share/doc/python_devel_stub/license
CHECKPKG_OVERRIDES_CSWpython += file-collision|/opt/csw/share/doc/python_devel_stub/license|CSWpython|CSWpython-devel
CHECKPKG_OVERRIDES_CSWpython += file-collision|/opt/csw/lib/pkgconfig/python3.pc|CSWpython|CSWpython31-dev
CHECKPKG_OVERRIDES_CSWpython += file-collision|/opt/csw/bin/python3|CSWpython|CSWpython31
CHECKPKG_OVERRIDES_CSWlibpython3-2-1-0 += pkginfo-opencsw-repository-uncommitted
CHECKPKG_OVERRIDES_CSWpython-dev += file-collision|/opt/csw/bin/python3-config|CSWpython-dev|CSWpython31-dev
CHECKPKG_OVERRIDES_CSWpython-test += surplus-dependency|CSWpython

include gar/category.mk

post-configure-modulated:
	for f in Modules/Setup \
			Makefile \
			Makefile.pre \
			Lib/idlelib/EditorWindow.py \
			Lib/pydoc_topics.py \
			Lib/idlelib/config-main.def \
			; do \
		gsed -i -e 's+/usr/local+/opt/csw+g' $(WORKSRC)/$${f}; \
		gsed -i -e 's+/usr/share+/opt/csw/share+g' $(WORKSRC)/$${f}; \
	done
	@$(MAKECOOKIE)

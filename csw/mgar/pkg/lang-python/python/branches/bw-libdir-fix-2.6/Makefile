# $Id$

NAME = Python
VERSION = 2.6.8
CATEGORIES = lang
GARTYPE = v2
VER = 2.6
DVER = 2-6
UVER = 2_6
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

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
# Some features are missing on Solaris 9, e.g. functionality required for the
# multiprocessing support.
# http://osdir.com/ml/opensolaris-discuss/2009-07/msg00865.html
# http://bugs.python.org/issue3770
# However, this bug is about better detection of SEM_VALUE_MAX in Solaris
# http://bugs.python.org/issue3110

# There are header differences between Solaris 9 and 10. Programs that include
# pyconfig.h from Solaris 9 installed on Solaris 10 can get wrong settings,
# e.g. wrt _X_OPEN_SOURCE.
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# Patches
PATCHFILES += 0001-patch-a-usr-local-reference-to-opt-csw-in-Tools-faqw.patch
PATCHFILES += 0002-handle-special-options-for-bsddb-in-Modules-makesetu.patch
PATCHFILES += 0003-bash-in-some-linker-options-for-the-curses-module.-m.patch
PATCHFILES += 0004-hack-some-solaris-requirements-into-setup.py.patch
PATCHFILES += 0005-ensure-the-_socket-module-links-with-the-socket-libr.patch
PATCHFILES += 0006-ensure-the-_multiprocessing-module-links-with-the-so.patch

PATCHFILES += 0001-FFI_DEFAULT_ABI-to-use-__i386.patch
# PATCHFILES += 0010-Hardcoding-the-use-of-libffi.patch
# PATCHFILES += 0011-OpenCSW-specific-libffi-include-dir.patch
# PATCHFILES += 0012-temporary-hack-to-compile-against-system-ffi.patch
PATCHFILES += 0013-Use-opt-csw-bin-python-in-cgi.py.patch
PATCHFILES += 0015-Adding-opt-csw-lib-to-dyld.py.patch
PATCHFILES += 0016-CSW-mimetypes.patch
PATCHFILES += 0017-Random-insignificant-removals-of-usr-local.patch
PATCHFILES += 0018-Removing-usr-local-from-mailcap.patch

PATCHFILES_5.10 += 0019-Force-multiprocess-to-compile.patch
PATCHFILES += $(PATCHFILES_$(GAROSREL))

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
OBSOLETED_BY_CSWpython$(CVER)-dev = CSWpython$(CVER)-devel

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
PKGFILES_CSWpython$(CVER)-test  = $(libdir)/python$(VER)/test/.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/bsddb/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/ctypes/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/email/test.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/distutils/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/json/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/lib2to3/tests.*
PKGFILES_CSWpython$(CVER)-test += $(libdir)/python$(VER)/sqlite3/test.*

ARCHALL_CSWpython$(CVER)-test = 1
ARCHALL_CSWidle$(CVER)        = 1

RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)-tk
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWbdb47
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibffi5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpanel5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibz1
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-test  += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk    += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWpython-tk += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpython-tk += CSWlibtk8-5

BUILD_DEP_PKGS += CSWlibffi-dev

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)-tk

# This package is not meant to be released
CHECKPKG_OVERRIDES_CSWpython-test += file-with-bad-content

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
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test  += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_

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

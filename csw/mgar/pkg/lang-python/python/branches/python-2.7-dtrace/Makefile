# $Id$

NAME = Python
VERSION = 2.7.8
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
# - test_threading locks up on Solaris 9: http://bugs.python.org/issue6643

VENDOR_URL = http://python.org/download/releases/$(VERSION)

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
UFILES_REGEX = $(VER)\.\d+

# PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparc

DISTFILES  = $(DISTNAME).tar.xz
DISTFILES += pyport.h

# The test for sunaudiodev fails.  Not that it's a good practice to skip
# tests.
# SKIPTEST_5.9 = 1
SKIPTEST = $(SKIPTEST_$(GAROSREL))
TEST_SCRIPTS = custom

# for a faster turn-around:
#
# For the current 64-bit building issue: http://bugs.python.org/issue18083
# A possible fix is to rename plat-linux to plat-<multiarch-tuple>
# BUILD64 = 1

# GARCOMPILER	=	GNU
# if change this take note of CONFIGURE_ARGS += --without-gcc
GARCOMPILER	=	SOS12U3
# GARFLAVOR = DBG
# remove fPIC for Studio compiler
PATCHFILES += 00-bits.patch
PATCHFILES += 04-solaris-64-bit.patch
# This patch adds Python dtrace support.  Note it is necessary to modify
# test_sys.py to add an integer to the frameobject structure size since this
# patch adds "int f_calllineno" to the structure, so this test does not fail.
# The patch comes from upstream:
# http://www.jcea.es/artic/python_dtrace-2_7_7_af8ecf2352e1.txt
# http://www.jcea.es/artic/python_dtrace.htm
# Follow http://bugs.python.org/issue13405 for plans to get it
# integrated into the main tree.
PATCHFILES += 05-dtrace.patch
# This patch uses fdwalk(3c) to close file descriptors; as that function is not
# widely implemented, this is unsuitable for upstream.
PATCHFILES += 11-closerange.patch 
PATCHFILES += 13-pic-compile.patch
# This patch adds Python debugger support.  It may be contributed upstream at
# some point, but the suitability (or lack thereof) has not yet been determined.
PATCHFILES += 14-py_db.patch 
# This patch adds wget_wch support to the curses module.  It may be contributed
# upstream at some point, but the suitability (or lack thereof) has not yet
# been determined.
PATCHFILES += 15-get_wch.patch
# This patch is needed to make Python understand it can build the OSS plugin.  
# Some OSS ioctls are not supported on Solaris, so they are ifdef'f out.  As
# the patch is Solaris-specific, it is not suitable for upstream.
PATCHFILES += 16-ossaudiodev.patch
# http://bugs.python.org/issue17964 was fixed in 3.4 but not back-ported so we
# need this patch for 2.7 .
PATCHFILES += 18-osconf-long.patch

EXTRA_INC += $(prefix)/bdb48/include
EXTRA_LIB += $(prefix)/bdb48/lib

# There is a file name conflict over libffi.so symlink between libffi package
# and a gcc-java package.  While it will ultimately belong to libffi_dev, the
# symlink is currently under a subdirectory.
# pkgchk -L CSWlibffi-dev
# (...)
# /opt/csw/lib/ffi/libffi.so=../libffi.so.5.0.10 s none CSWlibffi-dev
PREPEND_LINKER_FLAGS += -L$(libdir)/ffi

BASECFLAGS = $(CFLAGS)
EXTRA_COMMON_EXPORTS = BASECFLAGS
EXTRA_BUILD_ENV = DFLAGS=-32

# To fix https://www.opencsw.org/mantis/view.php?id=5040
LINKER_IGNORE =
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-gcc
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-unicode=ucs4
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


PACKAGES += CSWlibpython$(DVER)-1-0
PKGFILES_CSWlibpython$(DVER)-1-0 += $(call baseisadirs,$(libdir),libpython2\.7\.so\.1\.0(\.\d+)*)
SPKG_DESC_CSWlibpython$(DVER)-1-0 += $(DESCRIPTION), libpython2.7.so.1.0
RUNTIME_DEP_PKGS_CSWlibpython$(DVER)-1-0 += CSWlibgcc-s1

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

PKGFILES_CSWidle$(CVER) += $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle$(CVER) += $(bindir)/idle

ARCHALL_CSWidle$(CVER)        = 1

RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)
RUNTIME_DEP_PKGS_CSWidle$(CVER)   += CSWpython$(CVER)-tk
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWbdb48
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibffi5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpanel5
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpython$(CVER) += CSWlibz1

# Don't merge test files.
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/test
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/test/.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/bsddb/test.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/ctypes/test.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/email/test.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/distutils/tests.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/json/tests.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/lib2to3/tests.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/sqlite3/test.*
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python$(VER)/unittest/test.*

BUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibsqlite3-dev
BUILD_DEP_PKGS += CSWlibgdbm-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev

# Allow to choose the default Python version.
# Python 2.6 is the default one as of 2013-07-21.
# alternatives management begins:

# this is rebuilt in the merge phase

ALTERNATIVES_CSWpython$(CVER) = python-$(VER)
ALTERNATIVE_python-$(VER) = $(bindir)/python2 python $(bindir)/python$(VER) 270
ALTERNATIVE_python-$(VER) += $(bindir)/python python2 $(bindir)/python2
ALTERNATIVE_python-$(VER) += $(bindir)/2to3 2to3 $(bindir)/2to32
ALTERNATIVE_python-$(VER) += $(bindir)/2to32 2to32 $(bindir)/2to3$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/idle idle $(bindir)/idle2
ALTERNATIVE_python-$(VER) += $(bindir)/idle2 idle2 $(bindir)/idle$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/pdb pdb $(bindir)/pdb2
ALTERNATIVE_python-$(VER) += $(bindir)/pdb2 pdb2 $(bindir)/pdb$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/pydoc pydoc $(bindir)/pydoc2
ALTERNATIVE_python-$(VER) += $(bindir)/pydoc2 pydoc2 $(bindir)/pydoc$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/python-config python-config $(bindir)/python2-config
ALTERNATIVE_python-$(VER) += $(bindir)/python2-config python2-config $(bindir)/python$(VER)-config
ALTERNATIVE_python-$(VER) += $(bindir)/smtpd.py smtpd $(bindir)/smtpd.py2
ALTERNATIVE_python-$(VER) += $(bindir)/smtpd.py2 smtpd2 $(bindir)/smtpd.py$(VER)
ALTERNATIVE_python-$(VER) += $(mandir)/man1/python.1 man $(mandir)/man1/python2.1
ALTERNATIVE_python-$(VER) += $(mandir)/man1/python2.1 man2 $(mandir)/man1/python$(VER).1

EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/2to3
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/idle
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/pydoc
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python2
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python-config
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python2-config
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/smtpd.py
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/python.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/python2.1

# see also post-install for related actions
# : alternatives management ends

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)-tk

SPKG_DESC_CSWidle$(CVER)         = Python IDE
SPKG_DESC_CSWpython$(CVER)       = A high-level scripting language, $(VER) series

CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWidle$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)

LICENSE = LICENSE

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_

# Checkpkg does not understand relocatable packages.
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/$(PVER)/lib-dynload/gdbm.so
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/$(PVER)/lib-dynload/_gdbm.so
CHECKPKG_OVERRIDES_CSWpython$(CVER) += surplus-dependency|CSWgdbm

CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython

CHECKPKG_OVERRIDES_CSWpython$(CVER) += file-with-bad-content

EXTRA_PAX_ARGS_32  = -s ",^\.$(includedir)/python$(VER)/pyport.h$$,.$(includedir)/python$(VER)/pyport-32.h,p"
EXTRA_PAX_ARGS_64  = -s ",^\.$(includedir)/python$(VER)/pyport.h$$,.$(includedir)/python$(VER)/pyport-64.h,p"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libcurses.so.1
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libncursesw.so.5
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_hashlib.so|is|not|directly|bound|to|soname|libssl.so.1.0.0
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libcurses.so.1|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libncursesw.so.5|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libssl.so.1.0.0|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_hashlib.so|but|never|used

# 64-bit overrides
CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWlibffi4
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libcurses.so.1
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libncursesw.so.5
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_hashlib.so|is|not|directly|bound|to|soname|libssl.so.1.0.0
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libcurses.so.1|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libncurses.so.5|is|needed|by|/opt/csw/lib/python2.7/lib-dynload/_curses_panel_failed.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libncursesw.so.5|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libssl.so.1.0.0|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_hashlib.so|but|never|used

# Package definitions. We'll be gradually moving package definitions from the
# old grouping by variable name into grouping by package.
PACKAGES += CSWpython$(CVER)-tk
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Interface (TkInter)
PKGFILES_CSWpython$(CVER)-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += soname-unused
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_tkinter.so|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += soname-unused|libX11.so.4|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_tkinter.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_tkinter.so|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += soname-unused|libX11.so.4|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_tkinter.so|but|never|used

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

test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k -C $(OBJDIR) test
	$(MAKECOOKIE)

post-install:
	cd $(DESTDIR)$(bindir) && test -f 2to3 && mv -f 2to3 2to3$(VER)
	cd $(DESTDIR)$(bindir) && test -f idle && mv -f idle idle$(VER)
	cd $(DESTDIR)$(bindir) && test -f pydoc && mv -f pydoc pydoc$(VER)
	cd $(DESTDIR)$(bindir) && test -f smtpd.py && mv -f smtpd.py smtpd.py$(VER)
	cd $(DESTDIR)$(bindir) && ln -s -f ../lib/python$(VER)/pdb.py pdb$(VER)
	@$(MAKECOOKIE)

post-merge-modulated:
	# Some checks
	# Prevent things like https://www.opencsw.org/mantis/view.php?id=5040
	test ! -f $(PKGROOT)/opt/csw/lib/python$(VER)/lib-dynload/_socket_failed.so
	test -f $(PKGROOT)/opt/csw/lib/python$(VER)/lib-dynload/_socket.so
	echo "This is post-merge-modulated, which should not work. But it does."
	ginstall -m 755 -d $(PKGROOT)$(includedir)/python$(VER)
	ginstall -m 644 $(WORKDIR)/pyport.h $(PKGROOT)$(includedir)/python$(VER)/pyport.h
	@$(MAKECOOKIE)

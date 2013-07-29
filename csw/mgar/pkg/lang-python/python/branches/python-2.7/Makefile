# $Id$

NAME = Python
VERSION = 2.7.5
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
UFILES_REGEX = $(VER)\.\d+

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparc

DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += pyport.h

PATCHFILES += 0001-manage-previous-site-package.patch

# The test for sunaudiodev fails.  Not that it's a good practice to skip
# tests.
#SKIPTEST = 1
TEST_SCRIPTS = custom

# for a faster turn-around:
#
# For the current 64-bit building issue: http://bugs.python.org/issue18083
# A possible fix is to rename plat-linux to plat-<multiarch-tuple>
# BUILD64 = 1

GARCOMPILER	=	GNU
# GARFLAVOR = DBG

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

# To fix https://www.opencsw.org/mantis/view.php?id=5040
LINKER_IGNORE =
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
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
PACKAGES += CSWpython$(CVER)-tk


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
PKGFILES_CSWpython$(CVER)-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*

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

RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWpython$(CVER)

RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk_5.9    += CSWlibtcl8-4
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk_5.9    += CSWtk
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk_5.10   += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk_5.10   += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += $(RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk_$(GAROSREL))

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
ALTERNATIVES_CSWpython$(CVER) = python-$(VER)
ALTERNATIVE_python-$(VER) = $(bindir)/python python-symlink $(bindir)/python$(VER) 270
# TODO(maciej): Implement alternatives for the man page.
# ALTERNATIVES_CSWpython$(CVER) = python-man-$(VER)
# ALTERNATIVE_python-man-$(VER) = $(mandir)/man1/python.1 python-man-symlink python$(VER) 270

EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/python

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)-tk

SPKG_DESC_CSWidle$(CVER)         = Python IDE
SPKG_DESC_CSWpython$(CVER)       = A high-level scripting language, $(VER) series
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Interface (TkInter)

CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-test += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWidle$(CVER) += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython$(CVER)
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += soname-unused

LICENSE = LICENSE

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-dev += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk    += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython$(CVER)

# Checkpkg does not understand relocatable packages.
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/$(PVER)/lib-dynload/gdbm.so
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-not-found|libgdbm.so.3|is|needed|by|opt/csw/lib/$(PVER)/lib-dynload/_gdbm.so
CHECKPKG_OVERRIDES_CSWpython$(CVER) += surplus-dependency|CSWgdbm

CHECKPKG_OVERRIDES_CSWpython$(CVER) += file-with-bad-content

# To avoid file collisions with CSWpython:
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/idle,$(bindir)/idle-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/smtpd.py,$(bindir)/smtpd.py-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/pydoc,$(bindir)/pydoc-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/2to3,$(bindir)/2to3-$(VER),'
EXTRA_PAX_ARGS += -s ',^\.$(bindir)/python-config,$(bindir)/python-config-$(VER),'
# Needs to be turned into alternatives.
EXTRA_PAX_ARGS += -s ',^\.$(mandir)/man1/python.1,$(mandir)/man1/python.1-$(VER),'

EXTRA_PAX_ARGS_32  = -s ",^\.$(includedir)/python$(VER)/pyport.h$$,.$(includedir)/python$(VER)/pyport-32.h,p"
EXTRA_PAX_ARGS_64  = -s ",^\.$(includedir)/python$(VER)/pyport.h$$,.$(includedir)/python$(VER)/pyport-64.h,p"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libcurses.so.1
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libncursesw.so.5
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_hashlib.so|is|not|directly|bound|to|soname|libssl.so.1.0.0
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libcurses.so.1|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libncursesw.so.5|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libssl.so.1.0.0|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_hashlib.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += no-direct-binding|/opt/csw/lib/python$(VER)/lib-dynload/_tkinter.so|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += soname-unused|libX11.so.4|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_tkinter.so|but|never|used


# 64-bit overrides
CHECKPKG_OVERRIDES_CSWpython$(CVER) += missing-dependency|CSWlibffi4
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libcurses.so.1
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libncursesw.so.5
CHECKPKG_OVERRIDES_CSWpython$(CVER) += no-direct-binding|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_hashlib.so|is|not|directly|bound|to|soname|libssl.so.1.0.0
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libcurses.so.1|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libncurses.so.5|is|needed|by|/opt/csw/lib/python2.7/lib-dynload/_curses_panel_failed.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libncursesw.so.5|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython$(CVER) += soname-unused|libssl.so.1.0.0|is|needed|by|/opt/csw/lib/sparcv9/python$(VER)/lib-dynload/_hashlib.so|but|never|used
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

post-merge-modulated:
	# Some checks
	# Prevent things like https://www.opencsw.org/mantis/view.php?id=5040
	test ! -f $(PKGROOT)/opt/csw/lib/python$(VER)/lib-dynload/_socket_failed.so
	test -f $(PKGROOT)/opt/csw/lib/python$(VER)/lib-dynload/_socket.so
	echo "This is post-merge-modulated, which should not work. But it does."
	ginstall -m 755 -d $(PKGROOT)$(includedir)/python$(VER)
	ginstall -m 644 $(WORKDIR)/pyport.h $(PKGROOT)$(includedir)/python$(VER)/pyport.h
	@$(MAKECOOKIE)

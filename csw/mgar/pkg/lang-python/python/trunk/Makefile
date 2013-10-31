# $Id$

NAME = Python
VERSION = 2.6.9 lang
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
UPSTREAM_MASTER_SITES = http://pythoUFILES_REGEX = $(VER)\.\d+onPACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparcon.org/ftp/python/

DISTFILES  xz(DISTFILES += pyport.harc solaris10-i386

# Patches
PATCHFILES += faqwiz.diff
PATCHFILES += makesetup.diff
PATCHFILES += modules.diff
PATCHFILES += multiprocess.diff
PATCHFIL
# <maciej> This patch is an abomination. It should have never been done.
# e.g.: # http://lists.opencsw.org/pipermail/users/2012-October/009332.html
#
# The only reason it is still here is that once done it's really hard to undo,
# because it affects every single python module and python package, so to
# change this you have to rebuild the whole Python world.
#
# I really hope we never ever do this again.
# PATCHFILES += site.diff
#
# Let's try to break free:
PATCHFILES += 0015-Look-for-modules-in-the-unversioned-directory.patch
FILES += site.diff
PATCHFILES += python-config-in.diff
PATCHFILES += setup.diff
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
PATCHFILES += $(PATCHFILEShe test for sunaudiodev fails.  Not that it's a good practice to skip
# tests.
SKIPTEST = 1

# The 64-bit build is probably not going to happen for Python 2.6.
# A thread on python-list:
# http://mail.python.org/pipermail/python-list/2013-May/647197.html
# BUILD64ev fails.
SKIPTEST = 1

EXTRA_INC += $(prefix)/bdb47/include
EXTRA_LIB += $(prefix)/bdb47/lib

# There is a file name conflict over libffi.so symlink between libffi package
# and a gcc-java package.  While it will ultimately belong to libffi_dev, the
# symlink is currently under a subdirectory.
# pkgchk -L CSWlibffi-dev
# (...)
# /opt/csw/lib/ffi/libffi.so=../libffi.so.5.0.10 s nPREPENDSWlNKER_FLAGS += -L-dev
EXTRA_LIB += $(libdir)/ffi

BASECFLAGS = $(CFLAGS)
EXTRA_COMMON_EXPO# To fix https://www.opencsw.org/mantis/view.php?id=5040
LINKER_IGNORE =
CHECKPKG_OVERRIDES_CSWpython-tk += soname-unused|libX11.so.4|is|needed|by|/opt/csw/lib/python/lib-dynload/_tkinter.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython-tk += no-direct-binding|/opt/csw/lib/python/lib-dynload/_tkinter.so|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWpython += soname-unused|libcurses.so.1|is|needed|by|/opt/csw/lib/python/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython += soname-unused|libncursesw.so.5|is|needed|by|/opt/csw/lib/python/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython += no-direct-binding|/opt/csw/lib/python/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libncursesw.so.5
CHECKPKG_OVERRIDES_CSWpython += no-direct-binding|/opt/csw/lib/python/lib-dynload/_curses_panel.so|is|not|directly|bound|to|soname|libcurses.so.1
CHECKPKG_OVERRIDES_CSWpython += soname-unused|libssl.so.1.0.0|is|needed|by|/opt/csw/lib/python/lib-dynload/_hashlib.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython += no-direct-binding|/opt/csw/lib/python/lib-dynload/_hashlib.so|is|not|directly|bound|to|soname|libssl.so.1.0.0PO# With the versioned directory:
CHECKPKG_OVERRIDES_CSWpython-tk += soname-unused|libX11.so.4|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_tkinter.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/local|root/opt/csw/lib/python$(VER)/test/test_subprocess.py
CHECKPKG_OVERRIDES_CSWpython += file-with-bad-content|/usr/share|root/opt/csw/lib/python$(VER)/test/test_posixpath.py
CHECKPKG_OVERRIDES_CSWpython += soname-unused|libcurses.so.1|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython += soname-unused|libncursesw.so.5|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_curses_panel.so|but|never|used
CHECKPKG_OVERRIDES_CSWpython += soname-unused|libssl.so.1.0.0|is|needed|by|/opt/csw/lib/python$(VER)/lib-dynload/_hashlib.so|but|never|used
PORTS = BASECFLAGS

NOISALIST = 1
CONFIGURE_AGS  = $(DIRPATHS) 
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
# use prototype filter to set the class 
PROTOTYPE_FILTER = awk '$$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'

PACKAGES  = CSWidle$(CVER)
PACKAGES += CSWpython$(CVER)
PACKAGES += CSWpython$(CVER)-dev
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
PKGFILES_CSWpython$(CVER)-tk += $(libdir)/.*/lib-dynlon$(CVER)-test = 1
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
RUNTIME_DEP_PKGS_CSWpython$(CVER)-dev +=
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibpython$(DVER)-1-0
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWpython$(CVER)-tk += CSWpython$(CVER)

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
ALTERNATIVE_python-$(VER) = $(bindir)/python2 python $(bindir)/python$(VER) 2600
ALTERNATIVE_python-$(VER) += $(bindir)/python python2 $(bindir)/python2
ALTERNATIVE_python-$(VER) += $(bindir)/2to3 2to3 $(bindir)/2to32
ALTERNATIVE_python-$(VER) += $(bindir)/2to32 2to32 $(bindir)/2to3$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/idle idle $(bindir)/idle2
ALTERNATIVE_python-$(VER) += $(bindir)/idle2 idle2 $(bindir)/idle$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/pdb pdb $(bindir)/pdb2
ALTERNATIVE_python-$(VER) += $(bindir)/pdb2 pdb2 $(bindir)/pdb$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/pydoc pydoc $(bindir)/pydoc2
ALTERNATIVE_python-$(VER) += $(bindir)/pydoc2 pydoc2 $(bindir)/pydoc$(VER)
ALTERNATIVE_python-$(VER) += $(bindir)/python-config python-config $(bindir)/python-config2
ALTERNATIVE_python-$(VER) += $(bindir)/python-config2 python-config2 $(bindir)/python-config$(VER)
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
# : alternatives management endsS += Cython2-5-1-0

# This could be handled by automatic dependency detection
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWwith-bad-content

CATALOGNAME_CSWidle$(CVER)         = idle
CATALOGNAME_CSWpython$(CVER)       = python
CATALOGNAME_CSW Wpython$(CVER)-dev = python$(CVER)_dev
CATALOGNAME_CSWpython$(CVER)-tk    =ython$(CVER)_test

SPKG_DESC_CSWidle$(CVER)         = Python IDE
SPKG_DESC_CSWpython$(CVER)       = A high-level scripting language, $(VER) series
SPKG_DESC_CSW Wpython$(CVER)-dev = Development Files for Python
SPKG_DESC_CSWpython$(CVER)-tk    = Python Tk Inthon Test modules

LICENSE = LICENSE

# This is an exception, since these are original Python packages.
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWidle$(CVER)         += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDESdevS_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDE-devython$(CVER)-test  += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDEStk   S_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDE-tk  python$(CVER)-test  += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWpython$(CVER) += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpython$(CVER) += catalogname-does-noCHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpython$(CVER)-tk += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWidle$(CVER) += surplus-dependency|CSWpython

include gar/category.mk

# For some reason these definitions must be below the include.
GARCOMPILER_5.9 = SOS12
GARCOMPILER_5.10 = SOS12U3
GARCOMPILER = $(GARCOMPILER_$(GAROSREL))
dEXTRA_PAX_ARGS_32  = -s ",^\.$(includedir)/python$(VER)/pyport.h$$,.$(includedir)/python$(VER)/pyport-32.h,p"
EXTRA_PAX_ARGS_64  = -s ",^\.$(includedir)/python$(VER)/pyport.h$$,.$(includedir)/python$(VER)/pyport-64.h,p"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_$(MEMORYMODEL))
d gar/category.mk

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
	don
post-install:
	cd $(DESTDIR)$(bindir) && test -f 2to3 && mv -f 2to3 2to3$(VER)
	cd $(DESTDIR)$(bindir) && test -f idle && mv -f idle idle$(VER)
	cd $(DESTDIR)$(bindir) && test -f pydoc && mv -f pydoc pydoc$(VER)
	cd $(DESTDIR)$(bindir) && test -f smtpd.py && mv -f smtpd.py smtpd.py$(VER)
	cd $(DESTDIR)$(mandir)/man1 && test -f python.1 && mv -f python.1 python$(VER).1RCcd $(DESTDIR)$(bindir) && ln -s -f ../lib/python$(VER)/pdb.py pdb$(VER)RC)/$${f}; \
	don
post-merge-modulated:
	# Some checks
	# Prevent things like https://www.opencsw.org/mantis/view.php?id=5040
	test ! -f $(PKGROOT)/opt/csw/lib/python$(VER)/lib-dynload/_socket_failed.so
	test -f $(PKGROOT)/opt/csw/lib/python$(VER)/lib-dynload/_socket.so
	# This is post-merge-modulated, which should not work. But it does.
	ginstall -m 755 -d $(PKGROOT)$(includedir)/python$(VER)
	ginstall -m 644 $(WORKDIR)/pyport.h $(PKGROOT)$(includedir)/python$(VER)/pyport.h
	@$(MAKECOOKIE)

GARNAME = Python
GARVERSION = 2.6.4
CATEGORIES = lang

# Known issues:
#
# - No 64-bit build
# - ctypes module doesn't compile
#   - http://forums.sun.com/thread.jspa?threadID=5148204

SPKG_SOURCEURL = http://www.python.org/download/releases/$(GARVERSION)
SPKG_CLASSES = none cswpycompile

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

MASTER_SITES = http://www.python.org/ftp/python/$(GARVERSION)/
UPSTREAM_MASTER_SITES = http://www.python.org/ftp/python/

DISTFILES  = $(DISTNAME).tar.bz2

# Previous Library for compatability
DISTFILES += libpython2.5.so.1.0-isa-sparcv8
DISTFILES += libpython2.5.so.1.0-isa-i386

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Patches
PATCHFILES += faqwiz.diff
PATCHFILES += makesetup.diff
PATCHFILES += modules.diff
PATCHFILES += multiprocess.diff
PATCHFILES += pyport.diff
PATCHFILES += site.diff
PATCHFILES += python-config-in.diff
PATCHFILES += setup.diff
PATCHFILES += getpass.patch

# Test for sunaudiodev fails.
SKIPTEST = 1

DEPENDS += lib/expat
DEPENDS += lib/openssl
DEPENDS += lib/db
DEPENDS += lib/gdbm

ifeq ($(shell uname -p), i386)
    BASECFLAGS = -xO3 -xarch=386
else
    BASECFLAGS = -xO3 -xarch=v8
endif

COMPILER_EXPORTS += BASECFLAGS

ifneq ($(shell uname -r), 5.8)
    GARCOMPILER = SOS12
endif

NOISALIST = 1
LD_OPTIONS = -R/opt/csw/lib
export LD_OPTIONS
CONFIGURE_ARGS  = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-unicode=ucs4
CONFIGURE_ARGS += --without-gcc
CONFIGURE_ARGS += --with-signal-module
CONFIGURE_ARGS += --with-fpectl
CONFIGURE_ARGS += --with-system-ffi
CONFIGURE_ARGS += LDFLAGS='-R/opt/csw/lib -L/opt/csw/lib'

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
# use prototype filters to set the class 
PROTOTYPE_FILTER = awk '$$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'

PACKAGES  = CSWidle
PACKAGES += CSWpython
PACKAGES += CSWpython-devel
PACKAGES += CSWpython-rt
PACKAGES += CSWpython-test
PACKAGES += CSWpython-tk

INCOMPATIBLE_PKGS_CSWpython = CSWpydistutils

PKGFILES_CSWidle  = $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle += $(bindir)/idle
PKGFILES_CSWpython-devel  = $(includedir)/.*
PKGFILES_CSWpython-devel += $(libdir)/.*/config/.*
PKGFILES_CSWpython-devel += $(bindir)/.*config.*
# No idea why would this be in CSWpython, and no good idea for a better package
# to put it.
PKGFILES_CSWpython-devel += $(bindir)/smtpd.py
PKGFILES_CSWpython-rt = non-existing
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

ENABLE_CHECK = 0

REQUIRED_PKGS_CSWidle         = CSWpython CSWpython-tk
REQUIRED_PKGS_CSWpython       = CSWbdb CSWbzip2 CSWgdbm CSWggettextrt 
REQUIRED_PKGS_CSWpython      += CSWncurses CSWosslrt CSWpython-rt CSWreadline 
REQUIRED_PKGS_CSWpython      += CSWsqlite3rt CSWzlib
REQUIRED_PKGS_CSWpython-tk    = CSWpython CSWtcl CSWtk 
REQUIRED_PKGS_CSWpython-tk   += CSWpython-rt
REQUIRED_PKGS_CSWpython-devel = CSWpython
REQUIRED_PKGS_CSWpython-test  = CSWpython

CATALOGNAME_CSWidle = idle
CATALOGNAME_CSWpython = python
CATALOGNAME_CSWpython-devel = python_devel
CATALOGNAME_CSWpython-rt = python_rt
CATALOGNAME_CSWpython-tk = python_tk
CATALOGNAME_CSWpython-test = python_test

SPKG_DESC_CSWidle = Python IDE
SPKG_DESC_CSWpython = A high-level scripting language.
SPKG_DESC_CSWpython-devel = Development Files for Python
SPKG_DESC_CSWpython-rt = An empty, obsolete package
SPKG_DESC_CSWpython-tk = Python Tk Interface (TkInter)
SPKG_DESC_CSWpython-test = Python Test modules

include gar/category.mk

post-install-modulated: install-deprecated-libs
	@$(MAKECOOKIE)

install-deprecated-libs:
	echo "===> Installing deprecated Libraries into $(libdir)"
	cp $(DOWNLOADDIR)/libpython2.5.so.1.0-$(MODULATION) \
		$(DESTDIR)$(libdir)/libpython2.5.so.1.0
	cd $(DESTDIR)$(libdir); ln -s libpython2.5.so.1.0 libpython2.5.so
	@$(MAKECOOKIE)

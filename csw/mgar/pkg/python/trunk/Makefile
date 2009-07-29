GARNAME = Python
GARVERSION = 2.6.2
CATEGORIES = lang

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

PACKAGES  = CSWidle CSWpython CSWpydistutils CSWpython-devel CSWpython-rt CSWpython-tk

PKGFILES_CSWidle  = $(libdir)/.*/idlelib/.*
PKGFILES_CSWidle += $(bindir)/idle
PKGFILES_CSWpython-devel  = $(includedir)/.*
PKGFILES_CSWpython-devel += $(libdir)/.*/config/.*
PKGFILES_CSWpydistutils += $(libdir)/.*/distutils/.*
PKGFILES_CSWpython-rt += $(libdir)/.*libpython.*
PKGFILES_CSWpython-tk  = $(libdir)/.*/lib-tk/.*
PKGFILES_CSWpython-tk += $(libdir)/.*/lib-dynload/_tkinter.so.*

ENABLE_CHECK = 0

REQUIRED_PKGS_CSWidle         = CSWpython CSWpython-tk CSWcswclassutils
REQUIRED_PKGS_CSWpython       = CSWbdb CSWbzip2 CSWgdbm CSWggettextrt 
REQUIRED_PKGS_CSWpython      += CSWncurses CSWosslrt CSWpython-rt CSWreadline 
REQUIRED_PKGS_CSWpython      += CSWsqlite3rt CSWzlib CSWcswclassutils
REQUIRED_PKGS_CSWpython-tk    = CSWpython CSWtcl CSWtk 
REQUIRED_PKGS_CSWpython-tk   += CSWpython-rt CSWcswclassutils
REQUIRED_PKGS_CSWpydistutils  = CSWpython CSWcswclassutils 
REQUIRED_PKGS_CSWpython-devel = CSWpython CSWcswclassutils

CATALOGNAME_CSWpydistutils = pydistutils
CATALOGNAME_CSWidle = idle
CATALOGNAME_CSWpython = python
CATALOGNAME_CSWpython-devel = python_devel
CATALOGNAME_CSWpython-rt = python_rt
CATALOGNAME_CSWpython-tk = python_tk

SPKG_DESC_CSWidle = Python IDE
SPKG_DESC_CSWdistutils = Python Distutils makes modules and extensions easily available
SPKG_DESC_CSWpython = A high-level scripting language.
SPKG_DESC_CSWpython-devel = Development Files for Python
SPKG_DESC_CSWpython-rt = Python Runtime Libraries
SPKG_DESC_CSWpython-tk = Python Tk Interface (TkInter)

POST_INST_SCR  = add-depricated-libs
POST_INST_SCR += remove-compiled-py

post-install-modulated: $(POST_INST_SCR)
	@$(MAKECOOKIE)

add-depricated-libs:
	echo "===> Adding Depricated Libs"
	cp $(DOWNLOADDIR)/libpython2.5.so.1.0-$(MODULATION) \
		$(DESTDIR)$(libdir)/libpython2.5.so.1.0
	cd $(DESTDIR)$(libdir);ln -s libpython2.5.so.1.0 libpython2.5.so
	@$(MAKECOOKIE)

include gar/category.mk


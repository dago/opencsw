GARNAME = Python
GARVERSION = 2.6.2
CATEGORIES = lang
PACKAGES = CSWpython CSWpython-tk CSWidle

SPKG_SOURCEURL = http://www.python.org/download/releases/$(GARVERSION)

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
PATCHFILES += setup.diff
PATCHFILES += site.diff
PATCHFILES += configure.diff
PATCHFILES += python-config-in.diff

# Test for sunaudiodev fails.
SKIPTEST = 1

DEPENDS += lib/expat
DEPENDS += lib/openssl
DEPENDS += lib/db
DEPENDS += lib/gdbm

NOISALIST = 1
LD_OPTIONS = -R/opt/csw/lib
export LD_OPTIONS
CONFIGURE_ARGS  = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-unicode=ucs4
CONFIGURE_ARGS += --with-fpectl
CONFIGURE_ARGS += --with-system-ffi
CONFIGURE_ARGS += LDFLAGS='-R/opt/csw/lib -L/opt/csw/lib'

PKGFILES_CSWidle  = $(libdir)/python(\d+(?:\.\d+)*)/idlelib/.*
PKGFILES_CSWidle += $(bindir)/idle
PKGFILES_CSWpython-tk  = $(libdir)/python(\d+(?:\.\d+)*)/lib-tk/.*
PKGFILES_CSWpython-tk += $(libdir)/python(\d+(?:\.\d+)*)/lib-dynload/_tkinter.so.*

REQUIRED_PKGS_CSWpython  = CSWbdb44 CSWbzip2 CSWgdbm CSWggettextrt 
REQUIRED_PKGS_CSWpython += CSWncurses CSWosslrt CSWreadline CSWzlib
REQUIRED_PKGS_CSWpython += CSWsqlite3 CSWtcl CSWtk
REQUIRED_PKGS_CSWpython-tk = CSWpython CSWtcl CSWtk
REQUIRED_PKGS_CSWidle = CSWpython CSWpython-tk

CATALOGNAME_CSWpython = python
CATALOGNAME_CSWpython-tk = python_tk
CATALOGNAME_CSWidle = idle

SPKG_DESC_CSWpython = A high-level scripting language.
SPKG_DESC_CSWpython-tk = Python Tk Interface (TkInter)
SPKG_DESC_CSWidle = Python IDE

include gar/category.mk

POST_INST_SCR  = add-depricated-libs
POST_INST_SCR += fix-config-makefile
post-install-modulated: $(POST_INST_SCR)

add-depricated-libs:
	echo "===> Adding Depricated Libs"
	cp $(DOWNLOADDIR)/libpython2.5.so.1.0-$(MODULATION) \
		$(DESTDIR)$(libdir)/libpython2.5.so.1.0
	cd $(DESTDIR)$(libdir);ln -s libpython2.5.so.1.0 libpython2.5.so
	$(DONADA)

fix-config-makefile:
	perl -i -plne 's/^CCSHARED=.*/CCSHARED=/' \
		$(DESTDIR)$(libdir)/python/config/Makefile
	$(MAKECOOKIE)



GARNAME = Python
GARVERSION = 3.0
CATEGORIES = lang
PACKAGES = CSWpython3 CSWpython3-tk CSWidle3

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

SPKG_SOURCEURL = http://www.python.org/
MASTER_SITES = http://www.python.org/ftp/python/$(GARVERSION)/

DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Patches
PATCHFILES += 

# Test for sunaudiodev fails.
SKIPTEST = 1

CONFIGURE_ARGS  = $(DIRPATHS) 

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




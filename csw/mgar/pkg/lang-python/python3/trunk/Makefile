NAME = Python
VERSION = 3.2.2
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

SPKG_SOURCEURL = http://python.org/
MASTER_SITES = http://python.org/ftp/python/$(VERSION)/

DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Patches
PATCHFILES += 

# Test for sunaudiodev fails.
SKIPTEST = 1

CONFIGURE_ARGS  = $(DIRPATHS) 

PKGFILES_CSWidle3  = $(libdir)/python(\d+(?:\.\d+)*)/idlelib/.*
PKGFILES_CSWidle3 += $(bindir)/idle
PKGFILES_CSWpython3-tk  = $(libdir)/python(\d+(?:\.\d+)*)/lib-tk/.*
PKGFILES_CSWpython3-tk += $(libdir)/python(\d+(?:\.\d+)*)/lib-dynload/_tkinter.so.*

RUNTIME_DEP_PKGS_CSWpython3  = CSWbdb44 CSWbzip2 CSWgdbm CSWggettextrt 
RUNTIME_DEP_PKGS_CSWpython3 += CSWncurses CSWosslrt CSWreadline CSWzlib
RUNTIME_DEP_PKGS_CSWpython3 += CSWsqlite3 CSWtcl CSWtk
RUNTIME_DEP_PKGS_CSWpython3-tk = CSWpython3 CSWtcl CSWtk
RUNTIME_DEP_PKGS_CSWidle3 = CSWpython3 CSWpython3-tk

CATALOGNAME_CSWpython3 = python
CATALOGNAME_CSWpython3-tk = python_tk
CATALOGNAME_CSWidle3 = idle

SPKG_DESC_CSWpython3 = A high-level scripting language.
SPKG_DESC_CSWpython3-tk = Python Tk Interface (TkInter)
SPKG_DESC_CSWidle3 = Python IDE

include gar/category.mk


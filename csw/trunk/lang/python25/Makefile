GARNAME = python
GARVERSION = 2.4.3
CATEGORIES = lang

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
DISTFILES  = Python-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWpython24,)

WORKSRC = $(WORKDIR)/Python-$(GARVERSION)

DEPENDS += lib/expat
DEPENDS += lib/openssl
DEPENDS += lib/db
DEPENDS += lib/gdbm

CONFIGURE_ARGS = $(DIRPATHS) 

include ../category.mk

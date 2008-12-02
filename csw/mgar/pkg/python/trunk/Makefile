GARNAME = python
GARVERSION = 2.3.5
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
DISTFILES = Python-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = Python-(\d+(?:\.\d+)*).tar.bz2

# Configure some site specific variables
PATCHFILES = site-config.diff

WORKSRC = $(WORKDIR)/Python-$(GARVERSION)

LIBDEPS += lib/expat lib/openssl lib/db lib/gdbm

CONFIGURE_ARGS = $(DIRPATHS) 

include gar/category.mk

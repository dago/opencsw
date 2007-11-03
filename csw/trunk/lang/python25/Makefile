GARNAME = Python
GARVERSION = 2.5.1
GARRELEASE =
DISTVERSION = $(GARVERSION)$(GARRELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)
CATEGORIES = lang

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
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += $(call admfiles,CSWpython,depend prototype)
DISTFILES += $(call admfiles,CSWpython-tk,depend prototype)
DISTFILES += $(call admfiles,CSWidle,depend prototype)

# Configure
PATCHFILES += setup.diff

# Add lib/python2.3/site-packages to the sys.path
PATCHFILES += sitepath.diff

# Fix rcs tool path in faqwiz
PATCHFILES += faqwiz.diff

# Install to lib/python instead of lib/python$(VERSION)
PATCHFILES += instdir.diff

# Overrule bad decision about what Solaris headers provide
PATCHFILES += headers.diff

# Build curses with Solaris provided libs.
PATCHFILES += modules.diff

WORKSRC = $(WORKDIR)/$(DISTNAME)

# Test for sunaudiodev fails.
SKIPTEST = 1

DEPENDS += lib/expat
DEPENDS += lib/openssl
DEPENDS += lib/db
DEPENDS += lib/gdbm

CONFIGURE_ARGS  = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-fpectl

include ../category.mk

OPT = $(OPTFLAGS)
export OPT

post-install: fix-config-makefile

fix-config-makefile:
	perl -i -plne 's/^CCSHARED=.*/CCSHARED=/' \
		$(DESTDIR)$(libdir)/python/config/Makefile
	$(MAKECOOKIE)


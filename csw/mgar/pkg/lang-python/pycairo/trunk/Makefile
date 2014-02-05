NAME      = py2cairo
VERSION   = 1.10.0
GARTYPE = v2
CATEGORIES   = python

DESCRIPTION  = Python binding for Cairo library for Python2
define BLURB
  This package contains the pycairo Python module which implements
  a binding the the cairo Library.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
# DISTFILES     = pycairo-$(VERSION).tar.bz2 
DISTFILES     = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

# EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 

PACKAGES = CSWpy-cairo
SPKG_DESC_CSWpy-cairo = $(DESCRIPTION); main
OBSOLETED_BY_CSWpy-cairo = CSWpycairo
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWpython
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWlibcairo2

CAIRO_LIBS = -L/opt/csw/lib -R/opt/csw/lib/\$$ISALIST -lcairo
CAIRO_CFLAGS = -I/opt/csw/include -I/opt/csw/include/cairo
EXTRA_CONFIGURE_EXPORTS += CAIRO_LIBS CAIRO_CFLAGS

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
SKIPTEST = 1
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

configure-custom:
	cd $(WORKSRC) && ./waf configure --prefix=$(prefix)
	$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && ./waf build
	$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && DESTDIR=$(DESTDIR) ./waf install
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall -d $(DESTDIR)$(docdir)/py_cairo
	ginstall -m 644 $(WORKSRC)/COPYING  $(DESTDIR)$(docdir)/$(NAME)/license
	ginstall -m 644 $(WORKSRC)/COPYING  $(DESTDIR)$(docdir)/py_cairo/
	ginstall -m 644 $(WORKSRC)/COPYING-LGPL-2.1  $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 644 $(WORKSRC)/COPYING-MPL-1.1  $(DESTDIR)$(docdir)/$(NAME)
	$(MAKECOOKIE)

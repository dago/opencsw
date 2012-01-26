NAME = Gtk2
VERSION = 1.221
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TSCH

DESCRIPTION = Perl interface to the 2.x series of the Gimp Toolkit library
define BLURB
  Perl bindings to the 2.x series of the Gtk+ widget set.  This module allows
  you to write graphical user interfaces in a perlish and object-oriented way,
  freeing you from the casting and memory management in C, yet remaining very
  close in spirit to original API.
endef

PACKAGES = CSWpmgtk2
CATALOGNAME = pm_gtk2

LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWpmglib CSWgtk2 CSWpmpango CSWpmcairo CSWfconfig CSWftype2 CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2 CSWlibatk CSWlibcairo CSWpango
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

include gar/category.mk

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(prefix)/share/checkpkg/overrides
	echo "CSWpmgtk2: symbol-not-found" \
	  > $(PKGROOT)$(prefix)/share/checkpkg/overrides/$(CATALOGNAME)
	@$(MAKECOOKIE)


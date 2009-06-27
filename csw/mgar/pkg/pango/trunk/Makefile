GARNAME = libpango
GARVERSION = 1.24.3
CATEGORIES = lib

DESCRIPTION = A framework for the layout and rendering of international text
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  languages.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/1.24/
DISTNAME = pango-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2

PACKAGES = CSWpango CSWpangodevel CSWpangodoc
CATALOGNAME_CSWpango      = libpango
CATALOGNAME_CSWpangodevel = libpango_devel
CATALOGNAME_CSWpangodoc   = libpango_doc

PREREQUISITE_PKGS = CSWgtk-doc CSWlibxslt CSWglib2devel CSWlibxft2devel
REQUIRED_PKGS_CSWpango  = CSWggettextrt CSWglib2 CSWfconfig CSWftype2
REQUIRED_PKGS_CSWpango += CSWlibcairo CSWlibxft2 CSWlibxrender CSWzlib CSWlibx11
REQUIRED_PKGS_CSWpangodevel = CSWpango

SPKG_SOURCEURL = http://www.pango.org/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x --enable-gtk-doc
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
# CONFIGURE_ARGS += --with-included-modules 

STRIP_LIBTOOL = 1

# Dynamic prototype
PKGFILES_CSWpangodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpangodoc    = $(sharedstatedir)/gtk-doc/.*

# Do not execute make test step
TEST_SCRIPTS   = 

EXTRA_MERGE_EXCLUDE_FILES = .*/preload\.1\.gz

include gar/category.mk


NAME = libpango
VERSION = 1.24.5
CATEGORIES = lib

DESCRIPTION = A framework for the layout and rendering of international text
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  languages.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/1.24/
DISTNAME = pango-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWpango.postinstall

PACKAGES = CSWpango CSWpangodevel CSWpangodoc
CATALOGNAME_CSWpango      = libpango
CATALOGNAME_CSWpangodevel = libpango_devel
CATALOGNAME_CSWpangodoc   = libpango_doc

BUILD_DEP_PKGS = CSWgtk-doc CSWlibxslt CSWglib2devel CSWlibxft2devel
RUNTIME_DEP_PKGS_CSWpango  = CSWggettextrt CSWglib2 CSWfconfig CSWftype2
RUNTIME_DEP_PKGS_CSWpango += CSWlibcairo CSWlibxft2 CSWlibxrender CSWlibx11
RUNTIME_DEP_PKGS_CSWpangodevel = CSWpango

SPKG_DESC_CSWpango = Pango, a framework for the layout and rendering of international text
SPKG_DESC_CSWpangodevel = Pango Developer Files
SPKG_DESC_CSWpangodoc = Pango Documentation

SPKG_SOURCEURL = http://www.pango.org/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

BUILD64 = 1
NOISALIST = 1
EXTRA_ISAEXEC_EXCLUDE_FILES = $(bindir)/pango-querymodules
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x --enable-gtk-doc
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
# CONFIGURE_ARGS += --with-included-modules 

STRIP_LIBTOOL = 1

# Dynamic prototype
PKGFILES_CSWpangodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpangodoc    = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWpangodoc = 1

# Do not execute make test step
TEST_SCRIPTS   = 

EXTRA_MERGE_EXCLUDE_FILES = .*/preload\.1\.gz

sysconfdir_isa-sparcv9 = $(prefix)/etc/64
sysconfdir_isa-sparcv8 = $(prefix)/etc
sysconfdir_isa-i386    = $(prefix)/etc
sysconfdir_global      = $(prefix)/etc
sysconfdir_isa-amd64   = $(prefix)/etc/64
sysconfdir         = $(sysconfdir_$(MODULATION))

include gar/category.mk

post-merge:
	mkdir -p $(PKGROOT)$(sysconfdir)/64/pango
	@$(MAKECOOKIE)

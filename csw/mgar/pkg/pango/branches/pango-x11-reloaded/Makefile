GARNAME = libpango
GARVERSION = 1.28.0
CATEGORIES = lib

DESCRIPTION = A framework for the layout and rendering of international text
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  languages.
endef

GNOME_PROJ = pango
MASTER_SITES = $(GNOME_MIRROR)
DISTNAME = pango-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWpango.postinstall

PATCHFILES  = 0001-Do-not-use-fno.-options.patch
PATCHFILES += 0002-Use-inttypes.h-instead-of-stdint.h.patch

# 1.26.0:
# pango/opentype/hb-common.h includes stdint.h (missing on Solaris 8,
# correctly detected during autoconf, instead of sys/int_types.h)

PACKAGES = CSWpango CSWpangodevel CSWpangodoc
# PACKAGES += CSWcxpango CSWcxpangodevel

CATALOGNAME_CSWpango        = libpango
CATALOGNAME_CSWpangodevel   = libpango_devel
CATALOGNAME_CSWpangodoc     = libpango_doc
CATALOGNAME_CSWcxpango      = cx_libpango
CATALOGNAME_CSWcxpangodevel = cx_libpango_devel

BUILD_DEP_PKGS = CSWgtk-doc CSWlibxslt CSWglib2devel
RUNTIME_DEP_PKGS_CSWpango  = CSWggettextrt CSWglib2 CSWfconfig CSWftype2
RUNTIME_DEP_PKGS_CSWpango += CSWlibcairo CSWlibxft2 CSWlibxrender
RUNTIME_DEP_PKGS_CSWpangodevel = CSWpango
RUNTIME_DEP_PKGS_CSWcxpango  = CSWggettextrt CSWglib2 CSWfconfig CSWftype2
RUNTIME_DEP_PKGS_CSWcxpango += CSWcxlibcairo CSWlibxft2 CSWlibxrender CSWlibx11
RUNTIME_DEP_PKGS_CSWcxpangodevel = CSWcxpango

SPKG_DESC_CSWpango = Pango, a framework for the layout and rendering of international text
SPKG_DESC_CSWpangodevel = Pango Developer Files
SPKG_DESC_CSWpangodoc = Pango Documentation
SPKG_DESC_CSWcxpango = Pango, a framework for the layout and rendering of international text (bound against OpenCSW X11)
SPKG_DESC_CSWcxpangodevel = Pango Developer Files (bound against OpenCSW X11)

SPKG_SOURCEURL = http://www.pango.org/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_MODULATORS = X11
MODULATIONS_X11 = sunwx11 cswx11

# We need xrenderproto only
EXTRA_INC_sunwx11 = $(prefix)/X11/include

EXTRA_INC_cswx11 = $(prefix)/X11/include $(prefix)/include
EXTRA_LIB_cswx11 = $(prefix)/lib
EXTRA_PKG_CONFIG_DIRS_cswx11 = $(prefix)/lib

EXTRA_INC = $(EXTRA_INC_$(X11))
EXTRA_LIB = $(EXTRA_LIB_$(X11))
PKG_CONFIG_DIRS = $(PKG_CONFIG_DIRS_$(X11))

prefix_cswx11 = $(BUILD_PREFIX)/X11
prefix = $(or $(prefix_$(X11)),$(BUILD_PREFIX))

sysconfdir = $(abspath $(prefix)/etc/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

BUILD64 = 1
NOISALIST = 1
ISAEXEC_EXCLUDE_FILES = $(bindir)/pango-querymodules
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x --enable-gtk-doc

CONFIGURE_ARGS_sunwx11  = --x-include=/usr/openwin/include
CONFIGURE_ARGS_sunwx11 += --x-libraries=$(abspath /usr/openwin/lib/$(MM_LIBDIR))
CONFIGURE_ARGS_cswx11  = --x-include=$(prefix)/X11/include
CONFIGURE_ARGS_cswx11 += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(X11))

# CONFIGURE_ARGS += --with-included-modules 

MERGE_SCRIPTS_isa-default-x11-sunwx11 = copy-all
MERGE_SCRIPTS_isa-default64-x11-sunwx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-sunwx11 = $(libdir)
MERGE_SCRIPTS_isa-default-x11-cswx11 = copy-only
MERGE_DIRS_isa-default-x11-cswx11 = $(libdir) $(includedir)
MERGE_SCRIPTS_isa-default64-x11-cswx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-cswx11 = $(libdir)

# Dynamic prototype
PKGFILES_CSWpangodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpangodoc    = $(sharedstatedir)/gtk-doc/.*
PKGFILES_CSWcxlibpango     = $(call baseisadirs,/opt/csw/X11/lib,[^/]*\.so(\.\d+)*)
PKGFILES_CSWcxlibpangodevel = $(call baseisadirs,/opt/csw/X11/lib,pkgconfig(/.*)?)
PKGFILES_CSWcxlibpangodevel += /opt/csw/X11/include/.*

ARCHALL_CSWpangodoc = 1

# Do not execute make test step
TEST_SCRIPTS   = 

EXTRA_MERGE_EXCLUDE_FILES = .*/preload\.1\.gz

include gar/category.mk

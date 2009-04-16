GARNAME = libpango
GARVERSION = 1.24.1
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
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += fixme.sh

PACKAGES = CSWpango CSWpangodevel CSWpangodoc
CATALOGNAME_CSWpango      = libpango
CATALOGNAME_CSWpangodevel = libpango_devel
CATALOGNAME_CSWpangodoc   = libpango_doc

SPKG_SOURCEURL = http://www.pango.org/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS   = $(DIRPATHS)
CONFIGURE_ARGS  += --with-x --enable-gtk-doc
# CONFIGURE_ARGS  += --with-included-modules 

PREREQUISITE_PKGS = CSWgtk-doc CSWlibxslt
REQUIRED_PKGS_CSWpango  = CSWggettextrt CSWglib2 CSWfconfig CSWftype2
REQUIRED_PKGS_CSWpango += CSWlibcairo CSWlibxft2 CSWlibxrender CSWzlib
REQUIRED_PKGS_CSWpangodevel = CSWpango

# Dynamic prototype
PKGFILES_CSWpangodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpangodoc    = $(sharedstatedir)/gtk-doc/.*

# Do not execute make test step
TEST_SCRIPTS   = 

include gar/category.mk

post-configure-modulated:
	@echo " ==> Fixing libtool files"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	@$(MAKECOOKIE)



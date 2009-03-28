GARNAME = libpango
GARVERSION = 1.24.0
CATEGORIES = lib

DESCRIPTION = A framework for the layout and rendering of international text
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  languages.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/1.24/
DISTFILES  = pango-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWpango,)
DISTFILES += $(call admfiles,CSWpangodoc,)
DISTFILES += $(call admfiles,CSWpangodevel,)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS   = $(DIRPATHS)
CONFIGURE_ARGS  += --enable-gtk-doc

PREREQUISITE_PKGS += CSWgtk-doc

REQUIRED_PKGS_CSWpango = CSWggettextrt CSWglib2

# Dynamic prototype
PKGFILES_CSWpangodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpangodevel += /opt/csw/share/doc/libpango_devel/license
PKGFILES_CSWpangodoc    = /opt/csw/share/gtk-doc/.*
PKGFILES_CSWpangodoc   += /opt/csw/share/doc/libpango_doc/license

# Do not execute make test step
TEST_SCRIPTS   = 

include gar/category.mk

# CFLAGS := -g $(CFLAGS)
# CXXFLAGS := -g $(CXXFLAGS)
# export CFLAGS CXXFLAGS

# Disable -- it works, but ild gives symbol errors
# pre-configure:
#	@( cd $(WORKSRC)/pango/opentype ; \
#		$(PERL) -i.bak -plne 's/^(\@BUILD_OT_TESTS_TRUE\@noinst_PROGRAMS = ottest)/#$$1/' Makefile.in )

post-extract:
	( cd $(WORKROOTDIR) ; for i in build-isa-* ; do mv $$i/pango-$(GARVERSION) $$i/$(GARNAME)-$(GARVERSION) ; done )
	@$(MAKECOOKIE)

# pre-install:
#	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME) 
#	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)devel
#	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)doc
#	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)-$(GARVERSION)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)/license 
#	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)-$(GARVERSION)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)doc/license 
#	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)-$(GARVERSION)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)devel/license 

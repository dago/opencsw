GARNAME = pango
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWpango,)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/
UFILES_REGEX = (\d+(?:\.\d+)*)

# Dynamic gspec
PACKAGES                     = CSWlibpango CSWlibpangodevel
CATALOGNAME_CSWlibpango      = libpango
CATALOGNAME_CSWlibpangodevel = libpango_devel
SPKG_DESC_CSWlibpango   	 = $(DESCRIPTION)
SPKG_DESC_CSWlibpangodevel   = $(DESCRIPTION) development package

CONFIGURE_ARGS  = $(DIRPATHS)

# Do not execute make test step
TEST_SCRIPTS   = none

include gar/category.mk

# CFLAGS := -g $(CFLAGS)
# CXXFLAGS := -g $(CXXFLAGS)
# export CFLAGS CXXFLAGS

# Disable -- it works, but ild gives symbol errors
# pre-configure:
#	@( cd $(WORKSRC)/pango/opentype ; \
#		$(PERL) -i.bak -plne 's/^(\@BUILD_OT_TESTS_TRUE\@noinst_PROGRAMS = ottest)/#$$1/' Makefile.in )

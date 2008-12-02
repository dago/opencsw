GARNAME = pango
GARVERSION = 1.4.0
CATEGORIES = lib

DESCRIPTION = A framework for the layout and rendering of international text.
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  languages.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/pango/1.4/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWpango,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS += lib/xft

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

TEST_TARGET = check

include gar/category.mk

CFLAGS := -g $(CFLAGS)
CXXFLAGS := -g $(CXXFLAGS)
export CFLAGS CXXFLAGS

# Disable -- it works, but ild gives symbol errors
pre-configure:
	@( cd $(WORKSRC)/pango/opentype ; \
		$(PERL) -i.bak -plne 's/^(\@BUILD_OT_TESTS_TRUE\@noinst_PROGRAMS = ottest)/#$$1/' Makefile.in )

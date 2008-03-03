GARNAME = atk
GARVERSION = 1.6.0
CATEGORIES = lib

DESCRIPTION = An accessibility toolkit for GNOME.
define BLURB
  Accessibility is enabling people with disabilities to participate in
  substantial life activities that include work and the use of services,
  products, and information. GNOME Accessibility is the suite of software
  services and support in GNOME that allows people with disabilities to
  utilize all of the functionality of the GNOME user environment.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/atk/1.6/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

LIBDEPS += lib/glib2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

TEST_TARGET = check

include gar/category.mk

CFLAGS := -g $(CFLAGS)
CXXFLAGS := -g $(CXXFLAGS)
export CFLAGS CXXFLAGS

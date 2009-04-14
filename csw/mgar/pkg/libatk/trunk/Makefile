GARNAME = libatk
GARVERSION = 1.26.0
CATEGORIES = lib

DESCRIPTION = An accessibility toolkit for GNOME
define BLURB
  Accessibility is enabling people with disabilities to participate in
  substantial life activities that include work and the use of services,
  products, and information. GNOME Accessibility is the suite of software
  services and support in GNOME that allows people with disabilities to
  utilize all of the functionality of the GNOME user environment.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/atk/1.26/
DISTNAME = atk-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2
# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
UFILES_REGEX = (\d+(?:\.\d+)*)

REQUIRED_PKGS = CSWggettextrt CSWglib2

BUILD64 = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

TEST_TARGET = check

include gar/category.mk

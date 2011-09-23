NAME = atk
VERSION = 2.0.1
CATEGORIES = lib

DESCRIPTION = An accessibility toolkit for GNOME
define BLURB
  Accessibility is enabling people with disabilities to participate in
  substantial life activities that include work and the use of services,
  products, and information. GNOME Accessibility is the suite of software
  services and support in GNOME that allows people with disabilities to
  utilize all of the functionality of the GNOME user environment.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.xz

PACKAGES += CSWlibatk
CATALOGNAME_CSWlibatk = libatk
SPKG_DESC_CSWlibatk = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibatk = CSWggettextrt CSWglib2

PACKAGES += CSWlibatkdevel
CATALOGNAME_CSWlibatkdevel = libatk_devel
SPKG_DESC_CSWlibatkdevel = Developer files for libatk
RUNTIME_DEP_PKGS_CSWlibatkdevel = CSWlibatk CSWglib2devel

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

PKGFILES_CSWlibatkdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibatkdevel += $(sharedstatedir)/gtk-doc/.*

include gar/category.mk

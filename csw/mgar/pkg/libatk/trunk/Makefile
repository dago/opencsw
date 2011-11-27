NAME = atk
VERSION = 2.2.0
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

PATCHFILES += 0001-Comment-out-problematic-definition-of-AtkTextRange.patch

PACKAGES += CSWlibatk1-0-0
SPKG_DESC_CSWlibatk1-0-0 = An accessibility toolkit for GNOME, libatk-1.0.so.0
PKGFILES_CSWlibatk1-0-0 += $(call pkgfiles_lib,libatk-1.0.so.0)
RUNTIME_DEP_PKGS_CSWlibatk1-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibatk1-0-0 += CSWglib2
OBSOLETED_BY_CSWlibatk1-0-0 += CSWlibatk

PACKAGES += CSWlibatk-dev
SPKG_DESC_CSWlibatk-dev = Development files for libatk-1.0.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibatk-dev += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibatk-dev += CSWglib2devel
OBSOLETED_BY_CSWlibatk-dev = CSWlibatkdevel
CATALOGNAME_CSWlibatkdevel = libatk_devel_stub

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

include gar/category.mk

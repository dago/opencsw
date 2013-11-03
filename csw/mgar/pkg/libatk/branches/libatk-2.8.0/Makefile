NAME = atk
VERSION = 2.8.0
GARTYPE = v2

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386 lib
GARTYPE = v2

DESCRIPTION = An accessibility toolkit for GNOME
define BLURB
  Accessibility is enabling people with disabilities to participate in
  substantial life activities that include work and the use of services,
  products, and information. GNOME Accessibility is the suite of software
  services and support in GNOME that allows people with disabilities to
  utilize all of the functionality of the GNOME user environment.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(D#ISTNAME).tar.xz

PATCHFILES += 0001-Comment-out-problematic-definition-of-AtkTextRange.patch

PACKAGES += CSWlibatk1-0-0
SPKG_DESC_CSWlibatk1-0-0 = An accessibility toolkit for GNOME, libatk-1.0.so.0
PKGFILES_CSWlibatk1-0-0 += $(call pkgfiles_lib,libatk-1.0.so.0)
PKGFILES_CSWlibatk1-0-0 += $(sharedstatedir)/locale/.*
RUNTIME_DEP_PKGS_CSWlibatk1-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWllibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibatk1-0-0 += CSWlibglib2-0-01-0-0 += CSWglib2
OBSOLETED_BY_CSWlibatk1-0-0 += CSWlibatk

PACKAGES += CSWlibatk-dev
SPKG_DESC_CSWlibatk-dev = Development files for libatk-1.0.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibatk-dev += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibatk-dev += CSWglib2devel
OBSOLETED_BY_CSWlibatk-dev = CSWlibatkdevel
CATALOGNAME_CSWlibatkdevel = libatk_devel_stub

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARG# Build fails when using introspection and SOS12U3 (not sure if it would succeed with gcc)
CONFIGURE_ARGS += --enable-introspection=no

include gar/category.mk

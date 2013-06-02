# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = fluidsynth
VERSION = 1.1.6
GARTYPE = v2

DESCRIPTION = A real-time software synthesizer based on the SoundFont 2 specifications. 
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

# Official patches to fix the Solaris build - included upstream
PATCHFILES += 0002-fix-solaris-build.patch
PATCHFILES += 0003-fix-previous.patch

BUILD64_LIBS_ONLY = 1

PACKAGES += CSWfluidsynth
CATALOGNAME_CSWfluidsynth = fluidsynth
PKGFILES_CSWfluidsynth += $(bindir)/.*
PKGFILES_CSWfluidsynth += $(mandir)/man.*
SPKG_DESC_CSWfluidsynth += $(DESCRIPTION), fluidsynth
RUNTIME_DEP_PKGS_CSWfluidsynth += CSWlibfluidsynth1

PACKAGES += CSWlibfluidsynth1
CATALOGNAME_CSWlibfluidsynth1 = libfluidsynth1
PKGFILES_CSWlibfluidsynth1 += $(call baseisadirs,$(libdir),libfluidsynth\.so\.1\.5\.2)
PKGFILES_CSWlibfluidsynth1 += $(call baseisadirs,$(libdir),libfluidsynth\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibfluidsynth1 += $(DESCRIPTION), libfluidsynth.so.1

PACKAGES += CSWfluidsynth-dev
CATALOGNAME_CSWfluidsynth-dev = fluidsynth_dev
SPKG_DESC_CSWfluidsynth-dev += $(DESCRIPTION), development files
# PKGFILES is catchall

RUNTIME_DEP_PKGS_CSWlibfluidsynth1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibfluidsynth1 += CSWlibsndfile1
RUNTIME_DEP_PKGS_CSWlibfluidsynth1 += CSWlibreadline6

RUNTIME_DEP_PKGS_CSWfluidsynth-dev += CSWlibfluidsynth1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


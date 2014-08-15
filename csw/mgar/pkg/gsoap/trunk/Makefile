# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gsoap
VERSION = 2.8
SUBVERSION = 17
GARTYPE = v2

DESCRIPTION = Development toolkit for Web services and XML

SF_PROJECT = gsoap2
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)_$(VERSION).$(SUBVERSION).zip

PACKAGES += CSWgsoap
SPKG_DESC_CSWgsoap = Development toolkit for Web services and XML
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgsoap += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWgsoap += CSWlibz1

# We want the staticlibs
CHECKPKG_OVERRIDES_CSWgsoap += discouraged-path-in-pkgmap|/opt/csw/lib/libgsoap.a
CHECKPKG_OVERRIDES_CSWgsoap += discouraged-path-in-pkgmap|/opt/csw/lib/libgsoapck.a
CHECKPKG_OVERRIDES_CSWgsoap += discouraged-path-in-pkgmap|/opt/csw/lib/libgsoapssl.a

EXTRA_LINKER_FLAGS += -lsocket  -lnsl

# Makefile is missing $CPPFLAGS when compiling C++ files during link phase
EXTRA_CXXFLAGS += $(INCLUDE_FLAGS)
EXTRA_CXXFLAGS += -norunpath

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6

# Do NOT exclude the static libs, these are precompiled and meant to be in the package
MERGE_EXCLUDE_STATICLIBS =

include gar/category.mk


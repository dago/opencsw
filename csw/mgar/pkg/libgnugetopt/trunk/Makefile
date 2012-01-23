NAME = libgnugetopt
VERSION = 1.3
CATEGORIES = lib

DESCRIPTION = Library containing getopt_long
define BLURB
endef

MASTER_SITES = http://distfiles.macports.org/libgnugetopt/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# Patch from http://lists.gnu.org/archive/html/bug-bison/2010-04/msg00046.html
PATCHFILES += 0001-Sanitize-getopt.h.patch

LICENSE = README

PACKAGES += CSWlibgnugetopt0
SPKG_DESC_CSWlibgnugetopt0 = Library containing getopt_long, libgnugetopt.so.0
PKGFILES_CSWlibgnugetopt0 += $(call pkgfiles_lib,libgnugetopt.so.0)
OBSOLETED_BY_CSWlibgnugetopt0 += CSWlibgnugetopt

PACKAGES += CSWlibgnugetopt-dev
SPKG_DESC_CSWlibgnugetopt-dev = Development files for libgnugetopt.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgnugetopt-dev += CSWlibgnugetopt0

EXTRA_CFLAGS += -Xc

BUILD64_LIBS_ONLY = 1

include gar/category.mk

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cracklib
VERSION = 2.9.2
GARTYPE = v2

DESCRIPTION = Next generation version of libCrack password checking library

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cracklib-words-20080507.gz

PATCHFILES += 0001-Set-proper-types-instead-of-void.patch

PACKAGES += CSWlibcrack2
SPKG_DESC_CSWlibcrack2 = Next generation version of libCrack password checking library, libcrack.so.2
PKGFILES_CSWlibcrack2 += $(call pkgfiles_lib,libcrack.so.2)
RUNTIME_DEP_PKGS_CSWlibcrack2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcrack2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcrack2 += CSWlibz1

PACKAGES += CSWlibcrack-dev
SPKG_DESC_CSWlibcrack-dev = Development files for libcrack.so.2
PKGFILES_CSWlibcrack-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibcrack-dev += CSWlibcrack2

PACKAGES += CSWcracklib
SPKG_DESC_CSWcracklib = Next generation version of libCrack password checking
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcracklib += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcracklib += CSWlibcrack2

REINPLACEMENTS += words
REINPLACE_MATCH_words = /usr/share/words
REINPLACE_WITH_words = /usr/share/lib/dict/words
REINPLACE_FILES_words += util/create-cracklib-dict

# Yes, this is ok - we just replaced it with the correct file
CHECKPKG_OVERRIDES_CSWcracklib += file-with-bad-content|/usr/share|root/opt/csw/sbin/create-cracklib-dict

BUILD64 = 1
ISAEXEC = 1

# Unconditional use of -Wall
GARCOMPILER = GNU

# We need standard-conforming definitions, see getpwuid_r(3c)
EXTRA_CPPFLAGS +=  -D_POSIX_PTHREAD_SEMANTICS

CONFIGURE_ARGS += $(DIRPATHS)
# We don't need it and it is involves mixup of Sun Studio / GCC
CONFIGURE_ARGS += --without-python

include gar/category.mk


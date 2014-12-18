# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = gnupg
VERSION = 2.1.1
GARTYPE = v2

DESCRIPTION = GnuPG is a complete and free replacement for PGP
define BLURB
  RFC 2440 compliant tool for secure communication and data storage
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.gnupg.org/

GARCOMPILER = GCC4

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_common)
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWgnupg21)

BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibassuan-dev
BUILD_DEP_PKGS += CSWlibksba-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWopenldap-dev
BUILD_DEP_PKGS += CSWnpth-dev
BUILD_DEP_PKGS += CSWlibp11kit-dev
BUILD_DEP_PKGS += CSWlibadns-dev

PACKAGES += CSWgnupg21
SPKG_DESC_CSWgnupg21 = GnuPG is a complete and free replacement for PGP
# PKGFILES is catchall

RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibksba8
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibassuan0
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibadns1
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWlibldap2-4-2
# For gpg-agent. Pinentry is not because of shared libraries.
RUNTIME_DEP_PKGS_CSWgnupg21 += CSWpinentry
CHECKPKG_OVERRIDES_CSWgnupg21 += surplus-dependency|CSWpinentry

# Modern GnuPG, not a straight upgrade from v2.0
INCOMPATIBLE_PKGS_CSWgnupg21 = CSWgnupg2

NOISALIST = 1

BUILD64 = 1
ISAEXEC = 1

# POSIX forms such as $() are officially used in the tests scripts
REINPLACE_MATCH = ^\#!/bin/sh
REINPLACE_WITH  = \#!$(prefix)/bin/bash
REINPLACE_FILES = tests/openpgp/*.test

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-bzip2=$(prefix)
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-pinentry-pgm=$(prefix)/bin/pinentry-curses
CONFIGURE_ARGS += --enable-gpgtar

EXTRA_LDFLAGS = -lsocket -lnsl

PROTOTYPE_MODIFIERS = suid
PROTOTYPE_FILES_suid = .*/gpg2
PROTOTYPE_PERMS_suid = 4755

include gar/category.mk

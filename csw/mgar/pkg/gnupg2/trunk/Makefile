# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = gnupg
VERSION = 2.0.28
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = GnuPG is a complete and free replacement for PGP
define BLURB
  RFC 2440 compliant tool for secure communication and data storage
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES = $(Ds-in-macro.patch

VENDOR_URL = http:GARCOMPILER = GCC4p://www.gnupg.org/

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_common)
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWgnupg2)

BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibassuan-dev
BUILD_DEP_PKGS += CSWlibksba-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILpenldap-dev
BUILD_DEP_PKGS += CSWlibpth-devS += CSWoldapdevel

PACKAGES += CSWgnupg2
SPKG_DESC_CSWgnupg2 = GnuPG is a complete and free replacement for PGP
# PKGGFILES is catchall
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibksba8
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnup20 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibpth20
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibassuan0
RUNTIME_DEP_PKGlibadns1
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibldap2-4-2e# For gpg-agent. Pinentry is not because of shared libraries.
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWpinentry
CHECKPKG_OVERRIDES_CSWgnupg2 += surplus-dependency|CSWpinentry
dman1/gpg-agent.BUILD64 = 1
ISAEXEC#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl=$(prefix)
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-bzip2=$(prefix)
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-pinentry-pgm=$(prefix)/bin/pinentry-curses
CONFIGURE_ARGS += --with-pthCONFIGURE_ARGS += --enable-gpgtarh-prefix=$(prefix)

PROTOTYPE_MODIFIERS = suid
PROTOTYPE_FILES_suid = .*/gpg2
PROTOTYPE_PERMS_suid = 4755

includ
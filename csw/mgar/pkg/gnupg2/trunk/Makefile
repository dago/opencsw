# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = gnupg
VERSION = 2.0.18
CATEGORIES = apps

DESCRIPTION = GnuPG is a complete and free replacement for PGP
define BLURB
  RFC 2440 compliant tool for secure communication and data storage
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES = $(DISTNAME).tar.bz2

PATCHFILES += 0001-Fix-mutex-stream-return-args-in-macro.patch

VENDOR_URL = http://www.gnupg.org/

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_common)
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWgnupg2)

BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibassuan-dev
BUILD_DEP_PKGS += CSWlibksba-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWoldapdevel

PACKAGES += CSWgnupg2
SPKG_DESC_CSWgnupg2 = GnuPG is a complete and free replacement for PGP
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibksba8
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibpth20
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibassuan0
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWoldaprt

# Documentation overrides
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/share|root/opt/csw/share/gnupg/help.txt
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/gpgconf.1
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/share|root/opt/csw/share/info/gnupg.info-1
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/local|root/opt/csw/share/info/gnupg.info-1
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/local|root/opt/csw/share/info/gnupg.info-2
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/gpgsm.1
CHECKPKG_OVERRIDES_CSWgnupg2 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/gpgsm.1

PACKAGES += CSWgnupg-agent
SPKG_DESC_CSWgnupg-agent = GNU privacy guard - password agent
PKGFILES_CSWgnupg-agent += .*gpg-agent.*
PKGFILES_CSWgnupg-agent += .*gpg-connect-agent.*
PKGFILES_CSWgnupg-agent += .*gpgkey2ssh.*
PKGFILES_CSWgnupg-agent += .*symcryptrun.*
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibpth20
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibassuan0
# Pinentry is not because of shared libraries.
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWpinentry
CHECKPKG_OVERRIDES_CSWgnupg-agent += surplus-dependency|CSWpinentry

# Documentation overrides
CHECKPKG_OVERRIDES_CSWgnupg-agent += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/gpg-agent.1

NOISALIST = 1

# Unfortunately GNU PTH does not handle 64 bit sanely:
#   "/opt/csw/include/pth.h", line 93: #error: "FD_SETSIZE is larger than what GNU Pth can handle."
#BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl=$(prefix)
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-bzip2=$(prefix)
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-pinentry-pgm=$(prefix)/bin/pinentry-curses
CONFIGURE_ARGS += --with-pth-prefix=$(prefix)

PROTOTYPE_MODIFIERS = suid
PROTOTYPE_FILES_suid = .*/gpg2
PROTOTYPE_PERMS_suid = 4755

include gar/category.mk

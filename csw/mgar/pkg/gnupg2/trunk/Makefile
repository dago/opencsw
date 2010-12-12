# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = gnupg
VERSION = 2.0.15
CATEGORIES = apps

DESCRIPTION = GnuPG is a complete and free replacement for PGP.
define BLURB
    RFC 2440 compliant tool for secure communication and data storage
endef

PACKAGES                   = CSWgnupg2 CSWgnupg-agent
CATALOGNAME_CSWgnupg2      = gnupg2
CATALOGNAME_CSWgnupg-agent = gnupg_agent
SPKG_DESC_CSWgnupg2        = GnuPG is a complete and free replacement for PGP.
SPKG_DESC_CSWgnupg-agent   = GNU privacy guard - password agent

SPKG_SOURCEURL = http://www.gnupg.org/
MASTER_SITES   = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES      = $(NAME)-$(VERSION).tar.bz2

# fix some missing libraries for Keyserver tools and gpgsm
# Bug ID 996 filed up stream along with patch
# Supposed to be Fixed in the 01/2009 SVN version but has not
# made it into a release at the time of this packaging
PATCHFILES = sm-libraries.patch

# There's a problem with the testing framework which makes unit tests fail for
# 2.0.15.  Filed upstream as:
# https://bugs.g10code.com/gnupg/issue1214
SKIPTEST ?= 1
# Please remove this upon upgrade to 2.0.16.

UFILES_REGEX = (\d+(?:\.\d+)*)

NOISALIST  = 1
# There are no 64-bit ldap libraries, disabling the 64-bit build
# BUILD64    = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl=/opt/csw
CONFIGURE_ARGS += --with-ldap=/opt/csw
CONFIGURE_ARGS += --with-zlib=/opt/csw
CONFIGURE_ARGS += --with-bzip2=/opt/csw
CONFIGURE_ARGS += --with-readline=/opt/csw

CONFIGURE_ARGS += --with-pinentry-pgm=/opt/csw/bin/pinentry-curses

PROTOTYPE_FILTER = awk '$$$$3 ~/\/gpg2$$$$/ { $$$$4 = 4755 } { print }'

# This is somehow not correctly detected from autoconf
EXTRA_LINKER_FLAGS  = -lgpg-error
# Needed for nanosleep()
EXTRA_LINKER_FLAGS += -lrt

PKGFILES_CSWgnupg-agent  = .*gpg-agent.*
PKGFILES_CSWgnupg-agent += .*gpg-connect-agent.*
PKGFILES_CSWgnupg-agent += .*gpgkey2ssh.*
PKGFILES_CSWgnupg-agent += .*symcryptrun.*

RUNTIME_DEP_PKGS_common  = CSWbzip2
RUNTIME_DEP_PKGS_common += CSWcurlrt
RUNTIME_DEP_PKGS_common += CSWgcrypt
RUNTIME_DEP_PKGS_common += CSWggettextrt
RUNTIME_DEP_PKGS_common += CSWgpgerr
RUNTIME_DEP_PKGS_common += CSWiconv
RUNTIME_DEP_PKGS_common += CSWlibksba
RUNTIME_DEP_PKGS_common += CSWoldaprt
RUNTIME_DEP_PKGS_common += CSWreadline
RUNTIME_DEP_PKGS_common += CSWzlib

RUNTIME_DEP_PKGS_common_sparc += CSWpth
RUNTIME_DEP_PKGS_common += $(RUNTIME_DEP_PKGS_common_$(GARCH))

RUNTIME_DEP_PKGS_CSWgnupg2 += $(RUNTIME_DEP_PKGS_common)
RUNTIME_DEP_PKGS_CSWgnupg2 += CSWlibassuan

# Pinentry is not because of shared libraries.
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWpinentry
CHECKPKG_OVERRIDES_CSWgnupg-agent += surplus-dependency|CSWpinentry

RUNTIME_DEP_PKGS_CSWgnupg-agent_sparc += CSWpth

RUNTIME_DEP_PKGS_CSWgnupg-agent += $(RUNTIME_DEP_PKGS_CSWgnupg-agent_$(GARCH))

RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWgcrypt
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWgpgerr
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWiconv
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWlibassuan
RUNTIME_DEP_PKGS_CSWgnupg-agent += CSWreadline


BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS_common)
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWgnupg2)

TEST_TARGET = check

include gar/category.mk

# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME    = gnupg
GARVERSION = 2.0.13
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
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.bz2

# fix some missing libraries for Keyserver tools and gpgsm
# Bug ID 996 filed up stream along with patch
# Supposed to be Fixed in the 01/2009 SVN version but has not
# made it into a release at the time of this packaging
PATCHFILES = sm-libraries.patch

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

REQUIRED_PKGS_common  = CSWbzip2
REQUIRED_PKGS_common += CSWcurlrt
REQUIRED_PKGS_common += CSWgcrypt
REQUIRED_PKGS_common += CSWggettextrt
REQUIRED_PKGS_common += CSWgpgerr
REQUIRED_PKGS_common += CSWiconv
REQUIRED_PKGS_common += CSWlibassuan
REQUIRED_PKGS_common += CSWlibidn
REQUIRED_PKGS_common += CSWlibksba
REQUIRED_PKGS_common += CSWoldaprt
REQUIRED_PKGS_common += CSWosslrt
REQUIRED_PKGS_common += CSWpth
REQUIRED_PKGS_common += CSWreadline
REQUIRED_PKGS_common += CSWzlib


REQUIRED_PKGS_CSWgnupg2 += $(REQUIRED_PKGS_common)
REQUIRED_PKGS_CSWgnupg2 += CSWgnupg-agent

REQUIRED_PKGS_CSWgnupg-agent  = CSWpinentry
REQUIRED_PKGS_CSWgnupg-agent += CSWgcrypt
REQUIRED_PKGS_CSWgnupg-agent += CSWggettextrt
REQUIRED_PKGS_CSWgnupg-agent += CSWgpgerr
REQUIRED_PKGS_CSWgnupg-agent += CSWiconv
REQUIRED_PKGS_CSWgnupg-agent += CSWpth
REQUIRED_PKGS_CSWgnupg-agent += CSWreadline


PREREQUISITE_PKGS  = $(REQUIRED_PKGS_common)
PREREQUISITE_PKGS += $(REQUIRED_PKGS_CSWgnupg-agent)

TEST_TARGET = check

include gar/category.mk

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
BUILD64    = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzip2
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --enable-threads=solaris

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

REQUIRED_PKGS_common_CSWgnupg2  = CSWbzip2
REQUIRED_PKGS_common_CSWgnupg2 += CSWcurlrt
REQUIRED_PKGS_common_CSWgnupg2 += CSWgcrypt
REQUIRED_PKGS_common_CSWgnupg2 += CSWggettextrt
REQUIRED_PKGS_common_CSWgnupg2 += CSWgpgerr
REQUIRED_PKGS_common_CSWgnupg2 += CSWiconv
REQUIRED_PKGS_common_CSWgnupg2 += CSWlibassuan
REQUIRED_PKGS_common_CSWgnupg2 += CSWlibidn
REQUIRED_PKGS_common_CSWgnupg2 += CSWlibksba
REQUIRED_PKGS_common_CSWgnupg2 += CSWoldaprt
REQUIRED_PKGS_common_CSWgnupg2 += CSWosslrt
REQUIRED_PKGS_common_CSWgnupg2 += CSWpth
REQUIRED_PKGS_common_CSWgnupg2 += CSWreadline
REQUIRED_PKGS_common_CSWgnupg2 += CSWzlib

REQUIRED_PKGS_CSWgnupg2 += $(REQUIRED_PKGS_common_CSWgnupg2)
REQUIRED_PKGS_CSWgnupg2 += CSWgnupg-agent

REQUIRED_PKGS_CSWgnupg-agent = CSWpinentry

PREREQUISITE_PKGS  = $(REQUIRED_PKGS_common_CSWgnupg2)
PREREQUISITE_PKGS += $(REQUIRED_PKGS_CSWgnupg-agent)

TEST_TARGET = check

include gar/category.mk

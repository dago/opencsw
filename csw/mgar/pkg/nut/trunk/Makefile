# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = nut
VERSION = 2.7.2
GARTYPE = v2

DESCRIPTION = Network UPS Tools (NUT) provides support for Power Devices
define BLURB
The primary goal of the Network UPS Tools (NUT) project is to provide support for Power Devices, such as Uninterruptible Power Supplies, Power Distribution Units and Solar Controllers.
NUT provides many control and monitoring features, with a uniform control and management interface.
More than 100 different manufacturers, and several thousands models are compatible.
This software is the combined effort of many individuals and companies.
endef

MASTER_SITES = http://www.networkupstools.org/source/2.7/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-missing-strnlen.patch

GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWlibneon-dev
BUILD_DEP_PKGS += CSWnetsnmp-dev
BUILD_DEP_PKGS += CSWfreeipmi

RUNTIME_DEP_PKGS_CSWnut += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWnut += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWnut += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWnut += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWnut += CSWlibneon27
RUNTIME_DEP_PKGS_CSWnut += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWnut += CSWfreeipmi

# Needed for libusb
EXTRA_CPPFLAGS += -I/usr/sfw/include
EXTRA_LDFLAGS  += -L/usr/sfw/lib -R /usr/sfw/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/$(NAME)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-user=noaccess
CONFIGURE_ARGS += --with-group=noaccess

# No reason to split into small packages
CHECKPKG_OVERRIDES_CSWnut += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWnut += shared-lib-package-contains-so-symlink
# Use of libusb: overrides /usr/sfw/lib
CHECKPKG_OVERRIDES_CSWnut += bad-rpath-entry

# Fix configuration examples
REINPLACE_MATCH = /usr/local/ups/etc
REINPLACE_WITH  = /etc/opt/csw/nut
REINPLACE_FILES = conf/*.sample

include gar/category.mk

pre-configure:
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)


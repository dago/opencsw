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

# For libusb
EXTRA_CPPFLAGS += -I/usr/sfw/include
EXTRA_LDFLAGS  += -L/usr/sfw/lib -R /usr/sfw/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-user=noaccess
CONFIGURE_ARGS += --with-group=noaccess

include gar/category.mk

pre-configure:
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)


# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pnp4nagios
VERSION = 0.6.19
GARTYPE = v2

DESCRIPTION = abc
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Solaris-fixes.patch

BUILD_ARGS = all

# There is no testsuite
TEST_SCRIPTS =

# Do not install as nagios:nagios
INSTALL_OVERRIDE_VARS += INSTALL_OPTS
INSTALL_OVERRIDE_VAR_INSTALL_OPTS = 

INSTALL_ARGS = fullinstall

include gar/category.mk


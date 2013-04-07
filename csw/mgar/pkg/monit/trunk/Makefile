# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = monit
VERSION = 4.10.1
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Utility for monitoring and managing daemons or similar programs
define BLURB
  Long description
endef

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

VENDOR_URL = http://mmonit.com/monit/
MASTER_SITES = http://mmonit.com/monit/dist/
DISTFILES  = #PATCHFILES += 0001-Drop-some-build-flags-that-get-hard-coded-by-configu.patch
#PATCHFILES += 0002-fix-usr-local-references-drop-usr-local-etc-monitrc-.patch

CHECKPKG_OVERRIDES_CSWmonit = file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/monit.1
CHECKPKG_OVERRIDES_CSWmonit += $(CHECKPKG_OVERRIDES_CSWmonit_$(GARCH))
CHECKPKG_OVERRIDES_CSWmonit_sparc = file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8/monit
CHECKPKG_OVERRIDES_CSWmonit_sparc += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/monit
CHECKPKG_OVERRIDES_CSWmonit_i386 = file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/monit

-e#tc-monitrc-.patch

GARCOMPILER = GNU
BUILD64_ONLY = 1

BUILD_DEP_PKGS += CSWlibssl-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl-dir=$(prefix)

RUNTIME_DEP_PKGS_CSWmonit TEST_SCRIPTS = t # Revert to the old configuration path 
# so we don't change anything 
# for the ssl update
sysconfdir = $(prefix)/etc

include gar/category.mk


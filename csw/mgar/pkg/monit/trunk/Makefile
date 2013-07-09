# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = monit
VERSION = 5.5.1
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

CHECKPKG_OVERRIDES_CSWmonit += $(CHECKPKG_OVERRIDES_CSWmonit_$(GARCH))
CHECKPKG_OVERRIDES_CSWmonit_sparc += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/monit
CHECKPKG_OVERRIDES_CSWmonit_i386 = file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/monit

-MIGRATE_FILES_CSWmonit = monitrc
MIGRATE_SOURCE_DIR = $(prefix)/etc/
MIGRATE_DEST_DIR = $(sysconfdir)/
-e#tc-monitrc-.patch
# We build the 64 bits version to be have >2 Go file support
# and because monit build system is configured to build in
# 64 bits mode under Solaris
BUILD64_ONLY = 1
ISA_DEFAULT_sparc = sparcv9
ISA_DEFAULT_i386 = amd64
ISAEXEC_FILES = /opt/csw/bin/monitNU
BUILD64_ONLY = 1

BUILD_DEP_PKGS += CSWlibssl-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl-dir=$(prefix)

RUNTIME_DEP_PKGS_CSWmonit TEST_SCRIPTS = t include gar/category.mk


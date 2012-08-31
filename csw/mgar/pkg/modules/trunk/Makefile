# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = modules
VERSION = 3.2.9
MINOR = c
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Environment modules

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME)$(MINOR).tar.bz2

LICENSE = LICENSE.GPL

# These are all optional
CHECKPKG_OVERRIDES_CSWmodules += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWmodules += missing-dependency|CSWlibruby1-9-1-1|or|CSWruby|or|CSWruby18|or|CSWruby191
CHECKPKG_OVERRIDES_CSWmodules += missing-dependency|CSWtcl
CHECKPKG_OVERRIDES_CSWmodules += missing-dependency|CSWperl

# That is the manpath to /usr/share/man
CHECKPKG_OVERRIDES_CSWmodules += file-with-bad-content|/usr/share|root/opt/csw/bin/modulecmd

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-module-path=$(sharedstatedir)/Modules/modulefiles
CONFIGURE_ARGS += --with-version-path=$(sharedstatedir)/Modules/versions

# TBD: Add TclX
#CONFIGURE_ARGS += --with-tclx-lib=
#CONFIGURE_ARGS += --with-tclx-inc=

# Using exec_prefix prohibits the use of versioned modules
NODIRPATHS += --exec_prefix

# For whoami
TEST_ENV_PATH = /usr/ucb:$(PATH)

include gar/category.mk


# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = aha
VERSION = 0.4.7.2
GARTYPE = v2

DESCRIPTION = ANSI color to HTML converter

MASTER_SITES = https://github.com/theZiz/aha/archive/
DISTFILES  = $(VERSION).tar.gz

GARCOMPILER = GNU

CONFIGURE_SCRIPTS =

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += PREFIX
INSTALL_OVERRIDE_VAR_PREFIX = $(prefix)

# We want /usr/share/man instead of /usr/man
INSTALL_OVERRIDE_VARS += MAN
INSTALL_OVERRIDE_VAR_MAN = $(DESTDIR)$(mandir)/man1

# We need GNU install as 'install'
INSTALL_ENV_PATH = $(prefix)/gnu:$(PATH)

include gar/category.mk


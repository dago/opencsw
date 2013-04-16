# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! generally files are installed into wrong directories
# ! some binaries installed into prefix/bin maybe shouldn't be installed there
#   at all
# ! Python modules are clearly installed in a wrong plac
NAME = mailman
VERSION = 2.1.15

DESCRIPTION = Mailman mailing list software

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tgz

PACKAGES += CSWmailman
SPKG_DESC_CSWmailman = Mailman mailing list software
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWmailman += CSWpython
RUNTIME_DEP_PKGS_CSWmailman += CSWperl

# The mailman build system puts files in all sorts of strange places
prefix=$(BUILD_PREFIX)/$(NAME)

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --without-permcheck
CONFIGURE_ARGS += --with-python=/opt/csw/bin/python2.6

# There is no testsuite
TEST_SCRIPTS =

PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES = .*\.py[co]

CHECKPKG_OVERRIDES_CSWmailman += binary-architecture-does-not-match-placement|file=opt/csw/mailman/mail/mailman|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWmailman += binary-architecture-does-not-match-placement|file=opt/csw/mailman/mail/mailman|arch_id=3|arch_name=i386
CHECKPKG_OVERRIDES_CSWmailman += file-with-bad-content|/usr/share|root/opt/csw/mailman/Mailman/Defaults.py
CHECKPKG_OVERRIDES_CSWmailman += file-with-bad-content|/usr/local|root/opt/csw/mailman/messages/hu/README.hu

include gar/category.mk


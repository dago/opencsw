# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jed
MAJOR = 0.99
MINOR = 19
VERSION = 0.99.$(MINOR)
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Editor based on slang
define BLURB
endef

MASTER_SITES = ftp://space.mit.edu/pub/davis/jed/v$(VERSION)/
DISTNAME = $(NAME)-$(MAJOR)-$(MINOR)
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://www.jedsoft.org/jed/

BUILD_DEP_PKGS += CSWlibslang-dev
BUILD_DEP_PKGS += CSWlibxft2devel

PACKAGES += CSWjed
SPKG_DESC_CSWjed = Editor based on slang
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWjed += CSWlibslang2

# These may or may not be bad and need more investigation
CHECKPKG_OVERRIDES_CSWjed += file-with-bad-content|/usr/local|root/opt/csw/share/jed/lib/compile.sl
CHECKPKG_OVERRIDES_CSWjed += file-with-bad-content|/usr/local|root/opt/csw/share/jed/lib/site.sl
CHECKPKG_OVERRIDES_CSWjed += file-with-bad-content|/usr/local|root/opt/csw/share/jed/doc/txt/script.txt
CHECKPKG_OVERRIDES_CSWjed += file-with-bad-content|/usr/local|root/opt/csw/share/jed/doc/manual/jed.tex
CHECKPKG_OVERRIDES_CSWjed += file-with-bad-content|/usr/share|root/opt/csw/share/jed/lib/site.sl

PACKAGES += CSWxjed
SPKG_DESC_CSWxjed = The 'jed' editor with X11 bindings
PKGFILES_CSWxjed += $(bindir)/xjed
# There is lots of stuff in the base package we need
RUNTIME_DEP_PKGS_CSWxjed += CSWjed
CHECKPKG_OVERRIDES_CSWxjed += surplus-dependency|CSWjed
RUNTIME_DEP_PKGS_CSWxjed += CSWlibslang2
RUNTIME_DEP_PKGS_CSWxjed += CSWlibxft2

# Relocate from /opt/csw/jed
EXTRA_CONFIGURE_EXPORTS = JED_ROOT
CONFIGURE_ENV_JED_ROOT = $(sharedstatedir)/jed

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-x

# GTK is not build by default, "cd src; gmake gtkjed" is missing
# The original package doesn't have this also, so skip for until requested.
#CONFIGURE_ARGS += --with-gtk=$(libdir)/pkgconfig

BUILD_ARGS += all xjed

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk


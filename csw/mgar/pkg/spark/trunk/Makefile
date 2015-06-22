# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = spark
VERSION = 1.0.1

DESCRIPTION = Sparklines for your shell

MASTER_SITES = $(GITHUB_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = https://github.com/holman/spark
LICENSE = LICENSE.md

PACKAGES += CSWspark
SPKG_DESC_CSWspark = Sparklines for your shell
# PKGFILES is catchall
ARCHALL_CSWspark = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/spark $(DESTDIR)$(bindir)/spark
	@$(MAKECOOKIE)


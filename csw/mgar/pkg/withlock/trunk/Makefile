# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = withlock
VERSION = 0.2
GARTYPE = v2

DESCRIPTION = A locking wrapper script 

MASTER_SITES = http://mirrorbrain.org/files/releases/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = https://code.google.com/p/withlock/

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/withlock $(DESTDIR)$(bindir)/withlock
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jsawk
VERSION = 1.4
GARTYPE = v2

DESCRIPTION = Like awk, but for JSON

MASTER_SITES = https://github.com/micha/jsawk/archive/
# Use just version until this is fixed:
#   https://github.com/micha/jsawk/issues/39
DISTFILES += $(VERSION).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/jsawk $(DESTDIR)$(bindir)/jsawk
	ginstall -D -m 0644 $(WORKSRC)/README.markdown $(DESTDIR)$(docdir)/jsawk/README
	@$(MAKECOOKIE)

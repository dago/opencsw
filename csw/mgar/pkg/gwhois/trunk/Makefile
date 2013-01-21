# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gwhois
VERSION = 20120626
GARTYPE = v2

DESCRIPTION = Advanced WHOIS utility
define BLURB
  Advanced WHOIS utility
endef

MASTER_SITES = http://gwhois.de/gwhois/
DISTNAME = $(NAME)_$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)
ARCHALL_CSWgwhois = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
SKIPTEST = 1

INSTALL_SCRIPTS = gwhois

include gar/category.mk

install-gwhois:
	@/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/$(bindir)
	@/opt/csw/bin/ginstall -m 755 $(WORKSRC)/gwhois $(DESTDIR)/$(bindir)/gwhois
	@$(MAKECOOKIE)


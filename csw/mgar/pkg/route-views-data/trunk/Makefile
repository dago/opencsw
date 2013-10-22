# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = oix-full-snapshot
VERSION = 2013.10.22.0000
GARTYPE = v2

DESCRIPTION = OIX route views data

MASTER_SITES = http://archive.routeviews.org/oix-route-views/$(shell echo $(VERSION) | cut -d. -f1).$(shell echo $(VERSION) | cut -d. -f2)/
ROUTEVIEW_FILE = $(NAME)-$(subst .,-,$(VERSION)).bz2
DISTFILES += $(ROUTEVIEW_FILE)

PACKAGES += CSWroute-views-data
SPKG_DESC_CSWroute-views-data = OIX route views data
# PKGFILES is catchall
ARCHALL_CSWroute-views-data = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d -m 0755 $(DESTDIR)$(datadir)/routeviews
	ginstall -m 0644 $(WORKDIR)/$(ROUTEVIEW_FILE) $(DESTDIR)$(datadir)/routeviews
	ln -s $(ROUTEVIEW_FILE) $(DESTDIR)$(datadir)/routeviews/oix-full-snapshot-latest.dat.bz2
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = famfamfam_silk_icons
VERSION = 1.3
GARTYPE = v2

DESCRIPTION = FamFamFam Silk Icons

MASTER_SITES = http://www.famfamfam.com/lab/icons/silk/
DISTNAME = $(NAME)_v0$(subst .,,$(VERSION))
DISTFILES += $(DISTNAME).zip

LICENSE = readme.txt

ARCHALL_CSWfamfamfam-silk-icons = 1

# Come on, these are just pictures
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/famfamfam-silk-icons/
	ginstall -m 0644 $(WORKDIR)/readme.html $(DESTDIR)$(sharedstatedir)/www/famfamfam-silk-icons/
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/famfamfam-silk-icons/icons
	ginstall -m 0644 $(WORKDIR)/icons/* $(DESTDIR)$(sharedstatedir)/www/famfamfam-silk-icons/icons
	@$(MAKECOOKIE)


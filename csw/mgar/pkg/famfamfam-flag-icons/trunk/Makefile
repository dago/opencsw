# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = famfamfam_flag_icons
VERSION = 1.0
GARTYPE = v2

DESCRIPTION = FamFamFam Flag Icons

MASTER_SITES = http://www.famfamfam.com/lab/icons/flags/
DISTNAME = $(NAME)
DISTFILES += $(DISTNAME).zip

LICENSE = readme.txt

ARCHALL_CSWfamfamfam-flag-icons = 1

# Come on, these are just pictures
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/famfamfam-flag-icons/gif
	ginstall -m 0644 $(WORKDIR)/gif/* $(DESTDIR)$(sharedstatedir)/www/famfamfam-flag-icons/gif
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/famfamfam-flag-icons/png
	ginstall -m 0644 $(WORKDIR)/png/* $(DESTDIR)$(sharedstatedir)/www/famfamfam-flag-icons/png
	@$(MAKECOOKIE)


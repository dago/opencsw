# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = alternatives
VERSION = 1.0
CATEGORIES = utils

DESCRIPTION = Alternatives implementation specific to OpenCSW
define BLURB
endef

MASTER_SITES = 
DISTFILES  = alternatives alternatives.8
DISTFILES += CSWalternatives.i.cswalternatives
DISTFILES += CSWalternatives.r.cswalternatives
DISTFILES += LICENSE-2.0.txt

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE-2.0.txt

VENDOR_URL = http://wiki.opencsw.org/project-alternatives

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = 

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/alternatives $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall $(WORKDIR)/alternatives.1 $(DESTDIR)$(mandir)/man8
	ginstall -d $(DESTDIR)/etc/opt/csw/alternatives
	ginstall -d $(DESTDIR)/etc/opt/csw/preserve/CSWalternatives/alternatives
	ginstall -d $(DESTDIR)/var/opt/csw/alternatives
	ginstall -d $(DESTDIR)/usr/sadm/install/scripts
	ginstall $(WORKDIR)/CSWalternatives.i.cswalternatives $(DESTDIR)/usr/sadm/install/scripts/i.cswalternatives
	ginstall $(WORKDIR)/CSWalternatives.r.cswalternatives $(DESTDIR)/usr/sadm/install/scripts/r.cswalternatives
	@$(MAKECOOKIE)

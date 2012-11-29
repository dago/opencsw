# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = phpawl
VERSION = 0.53
GARTYPE = v2

DESCRIPTION = Andrew's Web Libraries - PHP Utility Libraries
define BLURB
  This package contains Andrew's Web Libraries.  This is a set
of hopefully lightweight libraries for handling a variety of
useful things for web programming, including:
 - Session management
 - User management
 - DB Records
 - Simple reporting
 - DB Schema Updating
 - iCalendar parsing

endef

MASTER_SITES = http://debian.mcmillan.net.nz/packages/awl/
DISTFILES  = awl-$(VERSION).tar.gz
DISTNAME = awl-$(VERSION)

ARCHALL = 1
NOGITPATCH=1

PACKAGES += CSWphp5-awl

REINPLACE_USRSHARE = docs/api/awl/* docs/api/awl/*/*

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/$(NAME)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/inc $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/dba $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/docs/api/awl/* $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)

NAME = memconf
VERSION = 2.16
CATEGORIES = utils

DESCRIPTION = Perl script that displays memory modules installed
define BLURB
	memconf reports the size of each SIMM/DIMM memory module installed in
	a system. It also reports the system type and any empty memory sockets.
endef

MASTER_SITES = http://www.4schmidts.com/unix/
DISTFILES  = $(NAME).gz
DISTFILES += memconf.man
DISTFILES += COPYING

SPKG_DESC = $(DESCRIPTION)
ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.4schmidts.com/memconf.html

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@cp $(WORKSRC)/$(NAME) $(DESTDIR)$(bindir)/$(NAME)
	@cp $(WORKSRC)/$(NAME).man $(DESTDIR)$(mandir)/man1/$(NAME).1
	@chmod 755 $(DESTDIR)$(bindir)/$(NAME)
	@chmod 644 $(DESTDIR)$(mandir)/man1/$(NAME).1
	@$(MAKECOOKIE)

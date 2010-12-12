NAME = policyd-weight
VERSION = 0.1.15
CATEGORIES = net
WORKSRC = $(WORKDIR)

DESCRIPTION = Policy daemon for the Postfix MTA (2.1 and later)
define BLURB
  Policy daemon for the Postfix MTA (2.1 and later) intended to eliminate
  forged envelope senders and HELOs (i.e. in bogus mails)
endef

MASTER_SITES  = http://www.policyd-weight.org/releases/
MASTER_SITES += http://www.policyd-weight.org/
DISTFILES += $(NAME)-devel
DISTFILES += $(NAME).conf.sample
DISTFILES += $(NAME).8
DISTFILES += $(NAME).conf.5
DISTFILES += documentation.txt
DISTFILES += todo.txt
DISTFILES += changes.txt
DISTFILES += COPYING

ARCHALL = 1

CATALOGNAME = policydweight

RUNTIME_DEP_PKGS = CSWperl CSWpmnetdns

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

INITSMF = /opt/csw/etc/init.d/csw$(NAME)
USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup

CHECKPKG_OVERRIDES += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES += surplus-dependency|CSWpmnetdns

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/init.d
	@ginstall -m 755 $(FILEDIR)/$(NAME).init $(DESTDIR)/opt/csw/etc/init.d/csw$(NAME)
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw
	@ginstall -m 644 $(WORKSRC)/policyd-weight.conf.sample $(DESTDIR)/etc/opt/csw/
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)/cswusergroup
	@ginstall -m 755 -d $(DESTDIR)$(sbindir)
	@ginstall -m 755 $(WORKSRC)/$(NAME)-devel $(DESTDIR)$(sbindir)/$(NAME)
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@ginstall -m 444 $(WORKSRC)/changes.txt $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@ginstall -m 444 $(WORKSRC)/documentation.txt $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@ginstall -m 444 $(WORKSRC)/todo.txt $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man5
	@ginstall -m 644 $(WORKSRC)/policyd-weight.conf.5 $(DESTDIR)$(mandir)/man5
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 644 $(WORKSRC)/policyd-weight.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

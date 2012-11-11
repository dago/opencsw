NAME = cswpkgloghooks
VERSION = 2.0
GARTYPE = v2

VENDOR_URL = http://opencsw.org

DESCRIPTION = Hook scripts to log package maintenance actions
define BLURB
This set of hook scripts will log package maintenance actions to syslog.
It is dependent on the use of a CSW package tool that is 'hook aware.'
Install, upgrade and removal actions are logged, both on success and on
failure.  Currently, the default of user.notice is used.
endef

VENDOR_URL = http://www.opencsw.org/

MASTER_SITES = 
DISTFILES =

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract-modulated: $(WORKSRC)
	cp $(FILEDIR)/gpl-3.0.txt $(WORKSRC)/COPYING

HOOKDIR=$(DESTDIR)/etc/opt/csw/pkg-hooks
POSTHOOKS = postinstall postupgrade postremove
PREHOOKS = preupgrade
HOOKS = $(PREHOOKS) $(POSTHOOKS)

install-custom:
	@echo Installing CSW$(NAME) files...
	@( ginstall -m 0755 -d $(DESTDIR)/opt/csw/share/doc/$(NAME)/ $(HOOKDIR) $(addprefix $(HOOKDIR)/,$(addsuffix .d,$(HOOKS))); \
	  ginstall -m 0644 $(FILEDIR)/README $(DESTDIR)/opt/csw/share/doc/$(NAME)/; \
	  ginstall -m 0755 $(FILEDIR)/01-CSW$(NAME)-postupgrade $(HOOKDIR)/postupgrade.d/; \
	  ln $(HOOKDIR)/postupgrade.d/01-CSW$(NAME)-postupgrade $(HOOKDIR)/postinstall.d/01-CSW$(NAME)-postinstall; \
	  ln $(HOOKDIR)/postupgrade.d/01-CSW$(NAME)-postupgrade $(HOOKDIR)/postremove.d/01-CSW$(NAME)-postremove; \
	  ginstall -m 0755 $(FILEDIR)/01-CSW$(NAME)-preupgrade $(HOOKDIR)/preupgrade.d/;)

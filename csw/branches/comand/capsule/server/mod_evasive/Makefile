GARNAME = mod_evasive
GARVERSION = 1.10.1
CATEGORIES = server

DESCRIPTION = DOS evasive maneuvers module for Apache 2.x
define BLURB
  mod_evasive is an evasive maneuvers module for Apache to provide evasive
  action in the event of an HTTP DoS or DDoS attack or brute force attack. It
  is also designed to be a detection and network management tool, and can be
  easily configured to talk to ipchains, firewalls, routers, and etcetera.
  mod_evasive presently reports abuses via email and syslog facilities. 
endef

MASTER_SITES = http://www.zdziarski.com/projects/$(GARNAME)/
DISTFILES += $(GARNAME)_$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWap2modevasive,depend prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

include ../category.mk
include ../apache2/files/extensionbuild.mk

WORKSRC := $(WORKDIR)/$(GARNAME)

build-custom:
	@( cd $(WORKSRC) ; $(APXS2_BUILD) $(GARNAME)20.c )
	@$(MAKECOOKIE)

install-custom:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@( cd $(WORKSRC) ; \
		$(APXS2_INSTALL) $(GARNAME)20.la  ; \
		cp README LICENSE $(DESTDIR)$(docdir)/$(GARNAME) )
	@$(MAKECOOKIE)


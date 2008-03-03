GARNAME = daemontools
GARVERSION = 0.76
CATEGORIES = utils

DESCRIPTION = A collection of tools for managing UNIX services
define BLURB
  A collection of tools for managing UNIX services
endef

MASTER_SITES = http://cr.yp.to/daemontools/ http://www.fefe.de/daemontools/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWdaemontools,)
WORKSRC = $(WORKDIR)/admin/$(GARNAME)-$(GARVERSION)

#PATCHFILES = daemontools-0.70-man.diff.bz2

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo "==> Configuring daemontools in $(WORKSRC)"
	@echo "$(CC) $(CFLAGS)" >$(WORKSRC)/src/conf-cc
	@echo "$(CC) $(LDFLAGS)" >$(WORKSRC)/src/conf-ld
	@$(MAKECOOKIE)

build-custom:
	@echo "==> Building daemontools in $(WORKSRC)"
	@( cd $(WORKSRC); ./package/compile )
	@chmod 755 $(WORKSRC)/command/*
	@$(MAKECOOKIE)

install-custom:
	@echo "==> Installing daemontools in $(DESTDIR)"
	@( cd $(WORKSRC) ; \
		install -d $(DESTDIR)$(bindir); cp -p command/* $(DESTDIR)$(bindir); \
	)

	

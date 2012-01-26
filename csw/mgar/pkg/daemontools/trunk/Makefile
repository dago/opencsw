NAME = daemontools
VERSION = 0.76
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A collection of tools for managing UNIX services
define BLURB
  A collection of tools for managing UNIX services
endef

MASTER_SITES += http://cr.yp.to/daemontools/
MASTER_SITES += http://smarden.org/pape/djb/manpages/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += $(DISTNAME)-man.tar.gz
DISTFILES += CSWdaemontools.postinstall CSWdaemontools.preremove
DISTFILES += COPYING

VENDOR_URL = http://cr.yp.to/daemontools.html

PACKAGES += CSWdaemontools
SPKG_DESC_CSWdaemontools = Configures the daemontools services on the local machine
PKGFILES_CSWdaemontools = NOFILES
ARCHALL_CSWdaemontools = 1
RUNTIME_DEP_PKGS_CSWdaemontools += CSWdaemontools-core
CHECKPKG_OVERRIDES_CSWdaemontools += surplus-dependency|CSWdaemontools-core

PACKAGES += CSWdaemontools-core
SPKG_DESC_CSWdaemontools-core = A collection of tools for managing UNIX services
# PKGFILES is catchallke remerge && 

WORKSRC = $(WORKDIR)/admin/$(NAME)-$(VERSION)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo "==> Configuring daemontools in $(WORKSRC)"
	@echo "$(CC) $(CFLAGS)" >$(WORKSRC)/src/conf-cc
	@echo "$(CC) $(LDFLAGS)" >$(WORKSRC)/src/conf-ld
	@$(MAKECOOKIE)

build-custom:
	@echo "==> Building daemontools in $(WORKSRC)"
	cd $(WORKSRC) && ./package/compile
	@$(MAKECOOKIE)

install-custom:
	@echo "==> Installing daemontools in $(DESTDIR)"
	mkdir -p $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/command/* $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(mandir)/man8
	ginstall -m 644 $(WORKDIR)/$(NAME)-man/*.8 $(DESTDIR)$(mandir)/man8
	perl -pi \
		-e 's,/command,$(bindir),g;' \
		-e 's,/usr/local,$(prefix),g;' \
		$(DESTDIR)$(bindir)/svscanboot \
		$(DESTDIR)$(mandir)/man8/svscanboot.8
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = svc-graphite
VERSION = 0.1.0
GARTYPE = v2

DESCRIPTION = A program to send performance data of IBM SVC to Graphite

MASTER_SITES = https://github.com/ivoronin/svc-graphite/releases/download/v$(VERSION)/
DISTFILES += $(DISTNAME)-standalone.jar
DISTFILES += svc-graphite

VENDOR_URL = https://github.com/ivoronin/svc-graphite

PACKAGES += CSWsvc-graphite
SPKG_DESC_CSWsvc-graphite = A program to send performance data of IBM SVC to Graphite
# PKGFILES is catchall
ARCHALL_CSWsvc-graphite = 1
RUNTIME_DEP_PKGS_CSWsvc-graphite += CSWjre8
CHECKPKG_OVERRIDES_CSWsvc-graphite += surplus-dependency|CSWjre8

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0644 $(WORKDIR)/$(DISTNAME)-standalone.jar $(DESTDIR)$(sharedstatedir)/java/$(DISTNAME).jar
	ln -s $(DISTNAME).jar $(DESTDIR)$(sharedstatedir)/java/$(NAME).jar
	ginstall -D -m 0755 $(WORKDIR)/svc-graphite $(DESTDIR)$(bindir)/svc-graphite
	@$(MAKECOOKIE)

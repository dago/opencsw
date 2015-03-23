# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cracklib-words
VERSION = 20080507
GARTYPE = v2

DESCRIPTION = Next generation version of libCrack password checking library

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(DISTNAME).gz

PACKAGES += CSWcracklib-words
SPKG_DESC_CSWcracklib = Cracklib word dictionary
# PKGFILES is catchall
ARCHALL_CSWcracklib-words = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0644 $(WORKDIR)/$(DISTNAME) $(DESTDIR)/opt/csw/share/lib/dict/$(DISTNAME)
	ln -s $(DISTNAME) $(DESTDIR)/opt/csw/share/lib/dict/$(NAME)
	@$(MAKECOOKIE)

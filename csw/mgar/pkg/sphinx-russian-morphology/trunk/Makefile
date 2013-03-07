# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sphinx-russian-morphology
VERSION = 20130120

DESCRIPTION = Russian morphology dictionary for Sphinx lemmatizer

MASTER_SITES = http://sphinxsearch.com/files/dicts/
DISTFILES += ru.pak

PACKAGES += CSWsphinx-russian-morphology
SPKG_DESC_CSWmypkg = Russian morphology dictionary for Sphinx lemmatizer
# PKGFILES is catchall
ARCHALL_CSWsphinx-russian-morphology = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	mkdir -p $(DESTDIR)$(sharedstatedir)/sphinx
	ginstall -m 0644 $(WORKDIR)/ru.pak $(DESTDIR)$(sharedstatedir)/sphinx/
	@$(MAKECOOKIE)

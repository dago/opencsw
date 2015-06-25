# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cardiff
VERSION = 1.2.0
CATEGORIES = python

DESCRIPTION = Cardiff is an extendible statsd clone written in Python

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
MANIFESTS += cswcardiff.xml
DISTFILES += $(MANIFESTS)
DISTFILES += cardiff.yaml

# This is a new package, don't bother building for 2.6
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWcardiff
SPKG_DESC_CSWcardiff = Cardiff is an extendible statsd clone written in Python
# PKGFILES is catchall
ARCHALL_CSWcardiff = 1
RUNTIME_DEP_PKGS_CSWcardiff += CSWpython27
CHECKPKG_OVERRIDES_CSWcardiff += surplus-dependency|CSWpython27

CHECKPKG_OVERRIDES_CSWcardiff += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWcardiff += pkgname-does-not-start-with-CSWpy-

# This is for the SMF DTD
CHECKPKG_OVERRIDES_CSWcardiff += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswcardiff.xml

REINPLACE_USRLOCAL += setup.py

# There is no testsuite
TEST_SCRIPTS =

PRESERVECONF += $(sysconfdir)/cardiff.yaml

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += $(foreach F,$(MANIFESTS),/var/opt/csw/svc/manifest/$F)
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKDIR)/cardiff.yaml $(DESTDIR)$(sysconfdir)/cardiff.yaml
	$(foreach F,$(MANIFESTS),ginstall -D -m 0644 $(WORKDIR)/$F $(DESTDIR)/var/opt/csw/svc/manifest/$F;)
	rm -f $(DESTDIR)$(sharedstatedir)/cardiff/init.d/cardiff
	rmdir $(DESTDIR)$(sharedstatedir)/cardiff/init.d
	@$(MAKECOOKIE)

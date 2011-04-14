# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pyxdg
VERSION = 0.19
CATEGORIES = python

DESCRIPTION = Python library to access freedesktop.org standards
define BLURB
endef

VENDOR_URL   = http://www.freedesktop.org/wiki/Software/pyxdg
MASTER_SITES = http://www.freedesktop.org/~lanius/
DISTFILES    = $(DISTNAME).tar.gz
DISTFILES   += changelog.CSW

PACKAGES = CSWpy-xdg
ARCHALL  = 1

TEST_SCRIPTS =

# XDG_DATADIRS contains /usr/share ... after /opt/csw/share
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/xdg/BaseDirectory.py

include gar/category.mk

pre-configure-modulated:
	gsed -i \
		-e 's,/usr/local/share,$(sharedstatedir),' \
		-e 's,/etc,$(sysconfdir),' \
		$(WORKSRC)/xdg/BaseDirectory.py
	@$(MAKECOOKIE)

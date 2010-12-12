NAME = mod_wsgi
VERSION = 3.2
CATEGORIES = lib


DESCRIPTION = Apache/Python WSGI adapter module.
define BLURB
  Mod_wsgi is a python WSGI adapter module for Apache.
endef

MASTER_SITES = http://modwsgi.googlecode.com/files/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += postinstall preremove space
LICENSE = LICENCE

PACKAGES = CSWap2modwsgi

RUNTIME_DEP_PKGS_CSWap2modwsgi = CSWpython
CATALOGNAME_CSWap2modwsgi   = ap2_modwsgi

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-python-src=../python

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

## Fix Makefile LDFLAGS to correct broken python-config return values
post-configure-modulated:
	@( perl -i -plne 's|^LDFLAGS = .*|LDFLAGS = -L/opt/csw/lib|' \
		$(WORKSRC)/Makefile )

include gar/category.mk


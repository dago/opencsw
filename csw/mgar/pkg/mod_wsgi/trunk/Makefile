GARNAME = mod_wsgi
GARVERSION = 2.5
CATEGORIES = lib

DESCRIPTION = an Apache/Python WSGI adapter module
define BLURB
  Mod_wsgi is a python WSGI adapter module for Apache.
endef

MASTER_SITES = http://modwsgi.googlecode.com/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += postinstall preremove space

PACKAGES = CSWap2modwsgi

REQUIRED_PKGS_CSWap2modwsgi = CSWap2prefork CSWpython
CATALOGNAME_CSWap2modwsgi   = ap2_modwsgi
SPKG_DESC_CSWap2modwsgi     = an Apache/Python WSGI adapter module

#PATCHFILES  = configure.diff
#PATCHFILES += connobject.diff

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


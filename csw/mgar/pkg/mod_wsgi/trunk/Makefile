# $Id$

NAME = mod_wsgi
VERSION = 3.3
CATEGORIES = lib


DESCRIPTION = Apache/Python WSGI adapter module.
define BLURB
  Mod_wsgi is a python WSGI adapter module for Apache.
endef

GOOGLE_PROJECT = modwsgi
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += postinstall preremove space
LICENSE = LICENCE

PACKAGES = CSWap2modwsgi

RUNTIME_DEP_PKGS_CSWap2modwsgi = CSWpython
CATALOGNAME_CSWap2modwsgi   = ap2_modwsgi

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-python-src=../python

## There are no tests for this
TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWap2modwsgi += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWap2modwsgi += CSWapache2

# If the pkgname is CSWap2modwsgi, catalogname should be ap2modwsgi
# If the catalogname is ap2_modwsgi, the pkgname should be CSWap2-modwsgi
CHECKPKG_OVERRIDES_CSWap2modwsgi += catalogname-does-not-match-pkgname|pkgname=CSWap2modwsgi|catalogname=ap2_modwsgi|expected-catalogname=ap2modwsgi

# checkpkg doesn't know why CSWpython is needed
CHECKPKG_OVERRIDES_CSWap2modwsgi += surplus-dependency|CSWpython

# <maciej>: As far as I can tell, python-config returns good values
#
## Fix Makefile LDFLAGS to correct broken python-config return values
# post-configure-modulated:
# 	@( perl -i -plne 's|^LDFLAGS = .*|LDFLAGS = -L/opt/csw/lib|' \
# 		$(WORKSRC)/Makefile )

include gar/category.mk

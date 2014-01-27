# $Id$

NAME = mod_wsgi
VERSION = 3.4
GARTYPE = v2lib
GARTYPE = v2


DESCRIPTION = Apache/Python WSGI adapter module.
define BLURB
  Mod_wsgi is a python WSGI adapter module for Apache.
endef

GOOGLE_PROJECT = modwsgi
MASTER_SITES = $(GOOGLE_M+= $(DISTNAME).tar.gz
DISTFILES += postinstall preremove

VENDOR_URL = https://code.google.com/p/modwsgi/
LICENSE = LICENCE

PACKAGES = CSWap2modwsgi
CATALOGNAME_CSWap2modwsgi   = ap2_modwsgi
RUNTIME_DEP_PKGS_CSWap2modwsgi += CSWpythons
TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWap2modwsgi += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWlibpython2-7= CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWap2modwsge CSWap2-modwsgi
CHECKPKG_OVERRIDES_CSWap2modwsgi += catalogname-does-not-match-pkgname|pkgname=CSWap2modwsgi|catalogname=ap2_modwsgi|expected-cataloCHECKPKG_OVERRIDES_CSWap2modwsgi += surplus-dependency|CSWpython

CHECKPKG_OVERRIDES_CSWap2modwsgi += soname-not-part-of-filename|soname=mod_wsgi.so|filename=mod_wsgi-2.6.so
CHECKPKG_OVERRIDES_CSWap2modwsgi += soname-not-part-of-filename|soname=mod_wsgi.so|filename=mod_wsgi-2.7.so

EXTRA_MODULATORS += PYTHON
MODULATIONS_PYTHON = 2.6 2.7

EXTRA_PAX_ARGS += -s ",^(.*)/mod_wsgi\.so,\1/mod_wsgi-$(PYTHON).so,"i   = ap2_modwsgi

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python$(PYTHON)
CONFIGURE_ARGS += --with-python-src=../python

# There are no tests for this
TEST_SCRIPTS =

MERGE_SCRIPTS_isa-default-python-2.6 = copy-all
MERGE_SCRIPTS_isa-default-python-2.7 = copy-all

include gar/category.mk

post-merge-all:
	gln -s mod_wsgi-2.6.so $(PKGROOT)/opt/csw/apache2/libexec/mod_wsgi.so
	@$(MAKECOOKIE)

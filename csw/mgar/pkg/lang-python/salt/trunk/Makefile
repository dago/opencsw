#TODO:
# * Create init scripts
# * Have mgar copy the minion.template and master.template files into place. (salt-0.10.1/conf/)
NAME = salt
VERSION = 0.10.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Distributed remote execution system
define BLURB
  Salt is a distributed remote execution system used to execute commands and query data. 
endef

MASTER_SITES = https://github.com/downloads/saltstack/salt/
DISTFILES  = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-yaml
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-m2crypto
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-crypto
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-jinja2
#RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-pyzmq
#RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-msgpack

CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/local|root/opt/csw/share/man/man7/salt.7
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/salt/modules/cron.py
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/salt/modules/rvm.py
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/salt/modules/freebsdservice.py
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/salt/modules/brew.py
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/salt/modules/pip.py
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/salt/modules/tomcat.py

ARCHALL_CSWpy-salt = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

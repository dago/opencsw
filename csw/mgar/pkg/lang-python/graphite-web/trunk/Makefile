# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = graphite-web
VERSION = 0.9.13
CATEGORIES = python

DESCRIPTION = Enterprise scalable realtime graphing

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += httpd-graphite-vhost.conf

# This is a new package, don't bother building for 2.6
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWgraphite-web
SPKG_DESC_CSWgraphite-web = Enterprise scalable realtime graphing
# PKGFILES is catchall
ARCHALL_CSWgraphite-web = 1
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-django
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-django-tagging
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-carbon
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-whisper
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWap2modwsgi
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-cairo
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-simplejson
# This is needed to get graphs from specific timeranges as reported in
#   https://github.com/graphite-project/graphite-web/issues/1019
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-tz
# python-hashlib is included in Python 2.5+

# That is because the vhost setting we ship is for Apache 2
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWapache2

CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-django
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-django-tagging
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-carbon
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-whisper
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWap2modwsgi
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-cairo
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-simplejson
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-tz

# This is a new package, don't bother building for 2.6
CHECKPKG_OVERRIDES_CSWgraphite-web += python-package-missing-py26-files

# This is /usr/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWgraphite-web += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/graphite/thirdparty/pytz/__init__.py

# Use upstream naming for main package
CHECKPKG_OVERRIDES_CSWgraphite-web += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgraphite-web += catalogname-does-not-start-with-py_

# This is provided as *.CSW by cswpreserveconf
CHECKPKG_OVERRIDES_CSWgraphite-web += file-needed-but-no-package-satisfies-it|/etc/opt/csw/graphite/local_settings.py|CSWgraphite-web|contains|symlink|/opt/csw/lib/python2.7/site-packages/graphite/local_settings.py|which|needs|the|target|file:|/etc/opt/csw/graphite/local_settings.py

# requires = Django => 1.1.4
#            django-tagging
#            carbon
#            whisper
#            mod_wsgi
#            pycairo
#            pycairo-devel
#            python-simplejson
#            python-sqlite2
#            python-hashlib

CONFDIR = $(sysconfdir)/graphite
STORAGEDIR = $(localstatedir)/graphite
WEBAPPDIR = $(sharedstatedir)/graphite

# Taken from local_settings.py.example
# Most installs done outside of a separate tree such as /opt/graphite will only
# need to change these three settings. Note that the default settings for each
# of these is relative to GRAPHITE_ROOT
#CONF_DIR = '/opt/graphite/conf'
#STORAGE_DIR = '/opt/graphite/storage'
#CONTENT_DIR = '/opt/graphite/webapp/content'

REINPLACEMENTS += localsettings_conf
REINPLACE_MATCH_localsettings_conf = \#CONF_DIR.*
REINPLACE_WITH_localsettings_conf = CONF_DIR = "$(CONFDIR)"
REINPLACE_FILES_localsettings_conf += webapp/graphite/local_settings.py.example

REINPLACEMENTS += localsettings_storage
REINPLACE_MATCH_localsettings_storage = \#STORAGE_DIR.*
REINPLACE_WITH_localsettings_storage = STORAGE_DIR = "$(STORAGEDIR)"
REINPLACE_FILES_localsettings_storage += webapp/graphite/local_settings.py.example

REINPLACEMENTS += localsettings_content
REINPLACE_MATCH_localsettings_content = \#CONTENT_DIR.*
REINPLACE_WITH_localsettings_content = CONTENT_DIR = "$(WEBAPPDIR)/webapp/content"
REINPLACE_FILES_localsettings_content += webapp/graphite/local_settings.py.example

REINPLACEMENTS += buildindex
REINPLACE_MATCH_buildindex = GRAPHITE_STORAGE_DIR\s*=.*
REINPLACE_WITH_buildindex = GRAPHITE_STORAGE_DIR="$(STORAGEDIR)"
REINPLACE_FILES_buildindex += bin/build-index.sh

REINPLACEMENTS += python27
REINPLACE_MATCH_python27 = \#!.*
REINPLACE_WITH_python27 = \#!$(bindir)/python2.7
REINPLACE_FILES_python27 += webapp/graphite/manage.py

EXTRA_INSTALL_ARGS += --install-data=$(CONFDIR)

CONFIG_FILES += dashboard.conf
CONFIG_FILES += graphTemplates.conf
CONFIG_FILES += graphite.wsgi

# There is no testsuite
TEST_SCRIPTS =

PRESERVECONF += $(prefix)/apache2/etc/extra/httpd-graphite-vhost.conf

# TBD: This needs customization of pathes
PRESERVECONF += $(foreach C,$(CONFIG_FILES) local_settings.py,$(CONFDIR)/$C)

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)

post-install:
	ginstall -D -m 0644 $(WORKDIR)/httpd-graphite-vhost.conf $(DESTDIR)$(prefix)/apache2/etc/extra/httpd-graphite-vhost.conf.CSW
	rm -f $(DESTDIR)$(CONFDIR)/examples/example-graphite-vhost.conf	
	mv $(DESTDIR)/opt/csw/lib/python2.7/site-packages/graphite/local_settings.py.example \
           $(DESTDIR)$(CONFDIR)/local_settings.py
	ln -s $(CONFDIR)/local_settings.py \
	      $(DESTDIR)/opt/csw/lib/python2.7/site-packages/graphite/local_settings.py
	cd $(DESTDIR)$(CONFDIR)/conf; $(foreach F,$(CONFIG_FILES),mv $F.example $(DESTDIR)$(CONFDIR)/$F.CSW;)
	rmdir $(DESTDIR)$(CONFDIR)/conf
	ginstall -d -m 0755 $(DESTDIR)$(WEBAPPDIR)
	mv $(DESTDIR)$(CONFDIR)/webapp $(DESTDIR)$(WEBAPPDIR)/webapp
	mv $(DESTDIR)$(CONFDIR)/examples $(DESTDIR)$(WEBAPPDIR)/examples
	ginstall -d -m 0755 $(DESTDIR)$(STORAGEDIR)
	mv $(DESTDIR)$(CONFDIR)/storage/* $(DESTDIR)$(STORAGEDIR)
	rmdir $(DESTDIR)$(CONFDIR)/storage
	chmod 0755 $(DESTDIR)/opt/csw/lib/python2.7/site-packages/graphite/manage.py
	ln -s ../lib/python2.7/site-packages/graphite/manage.py $(DESTDIR)$(bindir)/graphite-manage
	cd $(DESTDIR)$(bindir) && mv build-index.sh graphite-build-index
	cd $(DESTDIR)$(bindir) && mv run-graphite-devel-server.py graphite-run-devel-server
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = graphite-web
VERSION = 0.9.13
CATEGORIES = python

DESCRIPTION = Enterprise scalable realtime graphing

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

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

# This is /usr/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWgraphite-web += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/graphite/thirdparty/pytz/__init__.py
CHECKPKG_OVERRIDES_CSWgraphite-web += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/graphite/thirdparty/pytz/__init__.py

# Use upstream naming for main package
CHECKPKG_OVERRIDES_CSWgraphite-web += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgraphite-web += catalogname-does-not-start-with-py_

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

CONFDIR = $(sysconfdir)/graphite
STORAGEDIR = $(localstatedir)/graphite
WEBAPPDIR = $(sharedstatedir)/graphite

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /opt/graphite/conf
REINPLACE_WITH_conf = $(CONFDIR)
REINPLACE_FILES_conf += examples/example-graphite-vhost.conf

REINPLACEMENTS += storage
REINPLACE_MATCH_storage = /opt/graphite/storage
REINPLACE_WITH_storage = $(STORAGEDIR)
REINPLACE_FILES_storage += examples/example-graphite-vhost.conf
        
REINPLACEMENTS += webapp
REINPLACE_MATCH_webapp = /opt/graphite/webapp
REINPLACE_WITH_webapp = $(WEBAPPDIR)/webapp
REINPLACE_FILES_webapp += conf/graphite.wsgi.example
REINPLACE_FILES_webapp += examples/example-graphite-vhost.conf

REINPLACEMENTS += webperms
REINPLACE_MATCH_webperms = </Directory>
REINPLACE_WITH_webperms = </Directory>\n        <Directory /opt/csw/share/graphite/webapp>\n                Order deny,allow\n                Allow from all\n        </Directory>
REINPLACE_FILES_webperms += examples/example-graphite-vhost.conf

REINPLACEMENTS += wsgi
REINPLACE_MATCH_wsgi = modules/mod_wsgi.so
REINPLACE_WITH_wsgi = libexec/mod_wsgi-2.7.so
REINPLACE_FILES_wsgi += examples/example-graphite-vhost.conf

REINPLACEMENTS += noprefix
REINPLACE_MATCH_noprefix = ^WSGISocketPrefix
REINPLACE_WITH_noprefix = \#WSGISocketPrefix
REINPLACE_FILES_noprefix += examples/example-graphite-vhost.conf

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

EXTRA_INSTALL_ARGS += --install-data=$(CONFDIR)

CONFIG_FILES += dashboard.conf
CONFIG_FILES += graphTemplates.conf
CONFIG_FILES += graphite.wsgi

# There is no testsuite
TEST_SCRIPTS =

PRESERVECONF += $(prefix)/apache2/etc/extra/httpd-graphite-vhost.conf

# TBD: This needs customization of pathes
PRESERVECONF += /opt/csw/lib/python2.6/site-packages/graphite/local_settings.py
PRESERVECONF += /opt/csw/lib/python2.7/site-packages/graphite/local_settings.py
PRESERVECONF += $(foreach C,$(CONFIG_FILES),$(CONFDIR)/$C)

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)

V2_6 = 2.6
V2_7 = 2.7

post-install:
	ginstall -D -m 0644 $(DESTDIR)$(CONFDIR)/examples/example-graphite-vhost.conf $(DESTDIR)$(prefix)/apache2/etc/extra/httpd-graphite-vhost.conf.CSW
	rm -f $(DESTDIR)$(CONFDIR)/examples/example-graphite-vhost.conf	
	mv $(DESTDIR)/opt/csw/lib/python$(V$(PYTHON_VERSION))/site-packages/graphite/local_settings.py.example \
	   $(DESTDIR)/opt/csw/lib/python$(V$(PYTHON_VERSION))/site-packages/graphite/local_settings.py.CSW
	cd $(DESTDIR)$(CONFDIR)/conf; $(foreach F,$(CONFIG_FILES),mv $F.example $(DESTDIR)$(CONFDIR)/$F.CSW;)
	rmdir $(DESTDIR)$(CONFDIR)/conf
	ginstall -d -m 0755 $(DESTDIR)$(WEBAPPDIR)
	mv $(DESTDIR)$(CONFDIR)/webapp $(DESTDIR)$(WEBAPPDIR)/webapp
	mv $(DESTDIR)$(CONFDIR)/examples $(DESTDIR)$(WEBAPPDIR)/examples
	ginstall -d -m 0755 $(DESTDIR)$(STORAGEDIR)
	mv $(DESTDIR)$(CONFDIR)/storage/* $(DESTDIR)$(STORAGEDIR)
	rmdir $(DESTDIR)$(CONFDIR)/storage
	@$(MAKECOOKIE)

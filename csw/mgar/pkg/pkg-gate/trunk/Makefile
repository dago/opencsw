# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pkg-gate
VERSION = 2589
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = IPS package server
define BLURB
endef

MASTER_SITES = manual://
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME = ips

# Code for strncmp taken from
#   http://bugs.mysql.com/bug.php?id=7974
PATCHFILES += 0001-Add-missing-strndup-on-Solaris.patch

VENDOR_URL = http://src.opensolaris.org/source/xref/pkg/gate/

LICENSE = ips/doc/license.txt

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# For xml2po
BUILD_DEP_PKGS += CSWgnomedocutils

# For intltool-merge
BUILD_DEP_PKGS += CSWintltool

PYCOMPILE = 1

PACKAGES += CSWips-pkg-server
SPKG_DESC_CSWips-pkg-server = IPS package server
RUNTIME_DEP_PKGS_CSWips-pkg-server += CSWpython
RUNTIME_DEP_PKGS_CSWips-pkg-server += CSWpy-openssl
RUNTIME_DEP_PKGS_CSWips-pkg-server += CSWcherrypy
RUNTIME_DEP_PKGS_CSWips-pkg-server += CSWpy-simplejson

# With all the replacements and the large repo this takes forever
NOGITPATCH = 1

REINPLACEMENTS += intltool
REINPLACE_MATCH_intltool = /usr/bin/intltool-merge
REINPLACE_WITH_intltool = /opt/csw/bin/intltool-merge
REINPLACE_FILES_intltool = src/setup.py

REINPLACEMENTS += xml2po
REINPLACE_MATCH_xml2po = /usr/bin/xml2po
REINPLACE_WITH_xml2po = /opt/csw/bin/xml2po
REINPLACE_FILES_xml2po = src/setup.py

REINPLACEMENTS += linkopts
REINPLACE_MATCH_linkopts = \[ \"-zstrip-class=nonalloc\" \]
REINPLACE_WITH_linkopts = \[\]
REINPLACE_FILES_linkopts = src/setup.py

PYVARS += py_install_dir
#py_install_dir = 'usr/lib/python2.6/vendor-packages'
PYVAR_py_install_dir = $(libdir)/python/site-packages

PYVARS += scripts_dir
#scripts_dir = 'usr/bin'
PYVAR_scripts_dir = $(bindir)

PYVARS += lib_dir
#lib_dir = 'usr/lib'
PYVAR_lib_dir = $(libdir)

#svc_method_dir = 'lib/svc/method'

PYVARS += man1_dir
#man1_dir = 'usr/share/man/man1'
PYVAR_man1_dir = $(mandir)/man1

PYVARS += man1m_dir
#man1m_dir = 'usr/share/man/man1m'
PYVAR_man1m_dir = $(mandir)/man1m

PYVARS += man5_dir
#man5_dir = 'usr/share/man/man5'
PYVAR_man5_dir = $(mandir)/man5

PYVARS += man1_ja_JP_dir
#man1_ja_JP_dir = 'usr/share/man/ja_JP.UTF-8/man1'
PYVAR_man1_ja_JP_dir = $(mandir)/ja_JP.UTF-8/man1

PYVARS += man1m_ja_JP_dir
#man1m_ja_JP_dir = 'usr/share/man/ja_JP.UTF-8/man1m'
PYVAR_man1m_ja_JP_dir = $(mandir)/ja_JP.UTF-8/man1m

PYVARS += man5_ja_JP_dir
#man5_ja_JP_dir = 'usr/share/man/ja_JP.UTF-8/man5'
PYVAR_man5_ja_JP_dir = $(mandir)/ja_JP.UTF-8/man5

PYVARS += man1_zh_CN_dir
#man1_zh_CN_dir = 'usr/share/man/zh_CN.UTF-8/man1'
PYVAR_man1_zh_CN_dir = $(mandir)/zh_CN.UTF-8/man1

PYVARS += man1m_zh_CN_dir
#man1m_zh_CN_dir = 'usr/share/man/zh_CN.UTF-8/man1m'
PYVAR_man1m_zh_CN_dir = $(mandir)/zh_CN.UTF-8/man1m

PYVARS += man5_zh_CN_dir
#man5_zh_CN_dir = 'usr/share/man/zh_CN.UTF-8/man5'
PYVAR_man5_zh_CN_dir = $(mandir)/zh_CN.UTF-8/man5

PYVARS += resource_dir
#resource_dir = 'usr/share/lib/pkg'
PYVAR_resource_dir = $(sharedstatedir)/lib/pkg

PYVARS += transform_dir
#transform_dir = 'usr/share/pkg/transforms'
PYVAR_transform_dir = $(sharedstatedir)/pkg/transforms

#smf_app_dir = 'lib/svc/manifest/application/pkg'
#execattrd_dir = 'etc/security/exec_attr.d'
#authattrd_dir = 'etc/security/auth_attr.d'

PYVARS += sysrepo_dir
#sysrepo_dir = 'etc/pkg/sysrepo'
PYVAR_sysrepo_dir = $(sysconfdir)/pkg/sysrepo

PYVARS += sysrepo_logs_dir
#sysrepo_logs_dir = 'var/log/pkg/sysrepo'
PYVAR_sysrepo_logs_dir = $(localstatedir)/log/pkg/sysrepo

PYVARS += sysrepo_cache_dir
#sysrepo_cache_dir = 'var/cache/pkg/sysrepo'
PYVAR_sysrepo_cache_dir = $(localstatedir)/cache/pkg/sysrepo

PYVARS += autostart_dir
#autostart_dir = 'etc/xdg/autostart'
PYVAR_autostart_dir = $(sysconfdir)/xdg/autostart

#desktop_dir = 'usr/share/applications'

PYVARS += gconf_dir
#gconf_dir = 'etc/gconf/schemas'
PYVAR_gconf_dir = $(sysconfdir)/gconf/schemas

PYVARS += help_dir
#help_dir = 'usr/share/gnome/help/package-manager'
PYVAR_help_dir = $(sharedstatedir)/gnome/help/package-manager

PYVARS += omf_dir
#omf_dir = 'usr/share/omf/package-manager'
PYVAR_omf_dir = $(sharedstatedir)/omf/package-manager

PYVARS += startpage_dir
#startpage_dir = 'usr/share/package-manager/data/startpagebase'
PYVAR_startpage_dir = $(sharedstatedir)/manager/data/startpagebase

PYVARS += um_lib_dir
#um_lib_dir = 'usr/lib/update-manager'
PYVAR_um_lib_dir = $(libdir)/update-manager

PYVARS += um_share_dir
#um_share_dir = 'usr/share/update-manager'
PYVAR_um_share_dir = $(sharedstatedir)/update-manager

#PYVARS += pm_share_dir
#pm_share_dir = 'usr/share/package-manager'
#PYVAR_pm_share_dir = $(sharedstatedir)/package-manager

PYVARS += locale_dir
#locale_dir = 'usr/share/locale'
PYVAR_locale_dir = $(sharedstatedir)/locale

define pyrep
REINPLACEMENTS += pyvar-$(1)
REINPLACE_MATCH_pyvar-$(1) = $(1) = .*
REINPLACE_WITH_pyvar-$(1) = $(1) = '.$$(PYVAR_$(1))'
REINPLACE_FILES_pyvar-$(1) = src/setup.py
endef

$(foreach VAR,$(PYVARS),$(eval $(call pyrep,$(VAR))))

REINPLACEMENTS += python
REINPLACE_MATCH_python = /usr/bin/python2.6
REINPLACE_WITH_python = /opt/csw/bin/python
REINPLACE_FILES_python += $(libdir)/pkg.depotd
REINPLACE_WHEN_python = postinstall

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	(cd $(WORKSRC)/src; python setup.py build)
	@$(MAKECOOKIE)

install-custom:
	@echo "Copying python files"
	(cd $(WORKSRC)/src; python setup.py install --root=$(DESTDIR))
	@echo "Copying Sparc proto files"
	(cd $(WORKSRC)/proto/root_sparc; tar cvf - .) | (cd $(DESTDIR); tar xf -)
	@$(MAKECOOKIE)

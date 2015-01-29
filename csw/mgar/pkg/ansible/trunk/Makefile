NAME = ansible
VERSION = 1.8.2
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Deploy, manage, and orchestrate computer systems
define BLURB
endef

MASTER_SITES += http://releases.ansible.com/ansible/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += hosts.CSW

PATCHFILES += 0003-Extended-sbin_paths-by-opt-csw-sbin.patch
PATCHFILES += 0003-Add-etc-opt-csw-ssl-certs-to-the-path-searched-for-..patch

PACKAGES += CSWansible
# Stick with upstream naming
CHECKPKG_OVERRIDES_CSWansible += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWansible += catalogname-does-not-start-with-py_
SPKG_DESC_CSWansible = Deploy, manage, and orchestrate computer systems
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWansible += CSWpython
RUNTIME_DEP_PKGS_CSWansible = CSWpy-jinja2
RUNTIME_DEP_PKGS_CSWansible += CSWpy-markupsafe
RUNTIME_DEP_PKGS_CSWansible += CSWpy-yaml
RUNTIME_DEP_PKGS_CSWansible += CSWpy-paramiko
RUNTIME_DEP_PKGS_CSWansible += CSWopenssh-client
# checkpkg cannot detect these
CHECKPKG_OVERRIDES_CSWansible += surplus-dependency|CSWpy-markupsafe
CHECKPKG_OVERRIDES_CSWansible += surplus-dependency|CSWpy-yaml
CHECKPKG_OVERRIDES_CSWansible += surplus-dependency|CSWpy-paramiko
CHECKPKG_OVERRIDES_CSWansible += surplus-dependency|CSWopenssh-client
CHECKPKG_OVERRIDES_CSWansible += surplus-dependency|CSWpy-jinja2

# There are many OS specific (Linux, FreeBSD, etc.) paths stored in those files.
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/module_common.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/callbacks.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/ansible/playbook/__init__.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/ansible/runner/__init__.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/runner/__init__.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/module_utils/basic.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/module_utils/urls.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/ansible/module_utils/urls.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/packaging/os/homebrew_tap.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/packaging/os/homebrew_cask.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/packaging/os/pkgng.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/packaging/os/homebrew.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/packaging/language/composer.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/monitoring/nagios.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/monitoring/logentries.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/packaging/language/pip.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/packaging/os/yum.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/cloud/amazon/s3.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/cloud/google/gc_storage.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/files/unarchive.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/system/service.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/system/alternatives.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/ansible/modules/core/packaging/os/rhn_register.py

REINPLACEMENTS += etc
REINPLACE_MATCH_etc = /etc/ansible
REINPLACE_WITH_etc  = /etc/opt/csw/ansible
REINPLACE_FILES_etc = lib/ansible/constants.py

REINPLACEMENTS += usr
REINPLACE_MATCH_usr = /usr/share/ansible
REINPLACE_WITH_usr = /opt/csw/share/ansible
REINPLACE_FILES_usr = lib/ansible/constants.py

ARCHALL = 1

TEST_SCRIPTS =
LICENSE = COPYING

MODULATIONS_PYTHON_VERSION = 2_6

include gar/category.mk

post-merge:
	if [ -d $(PKGROOT)/usr/share/ansible ] ; then \
		mv $(PKGROOT)/usr/share $(PKGROOT)$(prefix)/share ; \
		rmdir $(PKGROOT)/usr || exit 1 ; \
	fi
	if [ ! -d $(PKGROOT)$(sysconfdir)/ansible ] ; then \
		ginstall -d $(PKGROOT)$(sysconfdir)/ansible ; \
	fi
	cp $(FILEDIR)/hosts.CSW $(PKGROOT)$(sysconfdir)/ansible/
	@$(MAKECOOKIE)

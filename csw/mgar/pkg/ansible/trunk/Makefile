NAME = ansible
VERSION = 1.9.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Deploy, manage, and orchestrate computer systems
define BLURB
endef

MASTER_SITES += http://releases.ansible.com/ansible/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += hosts.CSW

# The .git makes the build system think we have a checkout out repo and not a tarball
NOGITPATCH = 1

PATCHFILES += 0003-Extended-sbin_paths-by-opt-csw-sbin.patch
PATCHFILES += 0003-Add-etc-opt-csw-ssl-certs-to-the-path-searched-for-..patch

PACKAGES += CSWansible
# Stick with upstream naming
CHECKPKG_OVERRIDES_CSWansible += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWansible += catalogname-does-not-start-with-py_
SPKG_DESC_CSWansible = Deploy, manage, and orchestrate computer systems
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWansible += CSWpython
# We really want Python 2.6 which checkpkg cannot detect
CHECKPKG_OVERRIDES_CSWansible += surplus-dependency|CSWpython
RUNTIME_DEP_PKGS_CSWansible += CSWpy-jinja2
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
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/system/svc.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/packaging/os/dnf.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/ansible/modules/extras/system/locale_gen.py

REINPLACEMENTS += etc
REINPLACE_MATCH_etc = /etc/ansible
REINPLACE_WITH_etc  = $(sysconfdir)/ansible

REINPLACE_FILES_etc += bin/ansible-galaxy
REINPLACE_FILES_etc += lib/ansible/constants.py
REINPLACE_FILES_etc += lib/ansible/module_utils/urls.py
REINPLACE_FILES_etc += lib/ansible/modules/core/system/setup.py
REINPLACE_FILES_etc += lib/ansible/playbook/__init__.py
REINPLACE_FILES_etc += plugins/inventory/nova.py
REINPLACE_FILES_etc += plugins/inventory/openstack.py
REINPLACE_FILES_etc += docs/man/man1/ansible.1.asciidoc.in
REINPLACE_FILES_etc += docs/man/man1/ansible-galaxy.1
REINPLACE_FILES_etc += docs/man/man1/ansible-playbook.1.asciidoc.in
REINPLACE_FILES_etc += docs/man/man1/ansible-playbook.1
REINPLACE_FILES_etc += docs/man/man1/ansible.1
REINPLACE_FILES_etc += docs/man/man1/ansible-galaxy.1.asciidoc.in
REINPLACE_FILES_etc += examples/ansible.cfg

REINPLACE_USRSHARE += lib/ansible/constants.py
REINPLACE_USRSHARE += examples/ansible.cfg

ARCHALL = 1

TEST_SCRIPTS =
LICENSE = COPYING

MODULATIONS_PYTHON_VERSION = 2_6

PRESERVECONF += $(sysconfdir)/ansible/hosts
PRESERVECONF += $(sysconfdir)/ansible/ansible.cfg

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKDIR)/hosts.CSW $(DESTDIR)$(sysconfdir)/ansible/hosts.CSW
	ginstall -D -m 0644 $(WORKSRC)/examples/ansible.cfg $(DESTDIR)/$(sysconfdir)/ansible/ansible.cfg.CSW
	ginstall -d -m 0755 $(DESTDIR)$(sharedstatedir)/ansible
	cp -rp $(WORKSRC)/plugins $(DESTDIR)$(sharedstatedir)/ansible/plugins
	@$(MAKECOOKIE)

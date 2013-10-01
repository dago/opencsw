NAME = ansible
VERSION = 1.3.2
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Deploy, manage, and orchestrate computer systems
define BLURB
endef

GITHUB_USER     =       ansible
GITHUB_REFERENCE=       release1.3.2
MASTER_SITES    =       $(GITHUB_MIRROR)
DISTNAME	=	$(GITHUB_USER)-$(NAME)-9d5d88b
DISTFILES       =       $(GITHUB_REFERENCE)$(GITHUB_BALL_EXT)

PACKAGES     = CSWansible
CATALOGNAME  = ansible
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/ansible/module_common.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/ansible/callbacks.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/ansible/playbook/__init__.py
CHECKPKG_OVERRIDES_CSWansible += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/ansible/runner/__init__.py
CHECKPKG_OVERRIDES_CSWansible += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWansible += catalogname-does-not-start-with-py_

REINPLACEMENTS = etc
REINPLACE_MATCH_etc = /etc/ansible
REINPLACE_WITH_etc  = /opt/csw/ansible
REINPLACE_FILES_etc = lib/ansible/constants.py

REINPLACEMENTS += usr
REINPLACE_MATCH_usr = /usr/share/ansible
REINPLACE_WITH_usr  = /opt/csw/share/ansible
REINPLACE_FILES_usr = lib/ansible/constants.py

RUNTIME_PKG_DEPS  = CSWpy-jinja2
RUNTIME_PKG_DEPS += CSWpy-yaml
RUNTIME_PKG_DEPS += CSWopenssh-client

ARCHALL = 1

TEST_SCRIPTS =
LICENSE = COPYING

MODULATIONS_PYTHON_VERSION = 2_7

include gar/category.mk

post-merge:
	if [ -d $(PKGROOT)/usr/share/ansible ] ; then \
		mv $(PKGROOT)/usr/share $(PKGROOT)$(prefix)/share ; \
		rmdir $(PKGROOT)/usr || exit 1 ; \
	fi
	@$(MAKECOOKIE)

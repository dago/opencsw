# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fusioninventory-agent
VERSION = 2.2.4
GARTYPE = v2
CATEGORIES = cpan

DESCRIPTION = FusionInventory agent
define BLURB
  The FusionInventory agent is a generic management agent. It can perform a
  certain number of tasks, according to its own execution plan, or on behalf of
  a GLPI server with fusioninventory plugin, acting as a control point.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = $(CPAN_MIRRORS)
AUTHOR = FUSINV
DISTNAME = FusionInventory-Agent-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

LICENSE = LICENSE

PACKAGES = CSWfusioninventory-agent
ARCHALL = 1

RUNTIME_DEP_PKGS_CSWfusioninventory-agent  = CSWperl
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmcompresszlib
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmdigestmd5
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmfilewhich
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmhttpdaemon
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmiosocket_ssl
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmlibwwwperl
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmprocdaemon
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmprocpidfile
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmnetcups
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmnetip
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmtexttemplate
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmuniversalrequire
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpmxmltreepp

CONFIGURE_ARGS = PREFIX=/opt/csw SYSCONFDIR=/etc/opt/csw

# skip tests
SKIPTEST ?= 1

# ensure usage of gnu coreutils install
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

# checkpkg overrides
CHECKPKG_OVERRIDES_CSWfusioninventory-agent += archall-with-arch-paths|/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory/Input/BSD/Archs/i386.pm
CHECKPKG_OVERRIDES_CSWfusioninventory-agent += archall-with-arch-paths|/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory/Input/Linux/Archs/i386.pm

DOCLIST = LICENSE Changes README THANKS

include gar/category.mk

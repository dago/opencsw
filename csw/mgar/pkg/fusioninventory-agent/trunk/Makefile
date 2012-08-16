# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fusioninventory-agent
VERSION = 2.2.5
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

RUNTIME_DEP_PKGS  = CSWperl
RUNTIME_DEP_PKGS += CSWpmcompresszlib
RUNTIME_DEP_PKGS += CSWpmdigestmd5
RUNTIME_DEP_PKGS += CSWpmfilewhich
RUNTIME_DEP_PKGS += CSWpmhttpdaemon
RUNTIME_DEP_PKGS += CSWpmiosocket_ssl
RUNTIME_DEP_PKGS += CSWpmlibwwwperl
RUNTIME_DEP_PKGS += CSWpmprocdaemon
RUNTIME_DEP_PKGS += CSWpmprocpidfile
RUNTIME_DEP_PKGS += CSWpmnetcups
RUNTIME_DEP_PKGS += CSWpmnetip
RUNTIME_DEP_PKGS += CSWpmtexttemplate
RUNTIME_DEP_PKGS += CSWpmuniversalrequire
RUNTIME_DEP_PKGS += CSWpmxmltreepp
RUNTIME_DEP_PKGS += CSWmemconf

PATCHFILES += 0001-don-t-install-a-private-memconf-copy.patch

CONFIGURE_ARGS = PREFIX=/opt/csw SYSCONFDIR=/etc/opt/csw

# skip tests
SKIPTEST ?= 1

# ensure usage of gnu coreutils install
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

# checkpkg overrides
CHECKPKG_OVERRIDES += archall-with-arch-paths|/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory/Input/BSD/Archs/i386.pm
CHECKPKG_OVERRIDES += archall-with-arch-paths|/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory/Input/Linux/Archs/i386.pm
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory.pm

DOCLIST = LICENSE Changes README THANKS

include gar/category.mk

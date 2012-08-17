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

RUNTIME_DEP_PKGS += CSWpm-file-which
RUNTIME_DEP_PKGS += CSWpm-http-daemon
RUNTIME_DEP_PKGS += CSWpm-io-socket-ssl
RUNTIME_DEP_PKGS += CSWpm-libwww-perl
RUNTIME_DEP_PKGS += CSWpm-proc-daemon
RUNTIME_DEP_PKGS += CSWpm-proc-pid-file
RUNTIME_DEP_PKGS += CSWpm-net-cups
RUNTIME_DEP_PKGS += CSWpm-net-ip
RUNTIME_DEP_PKGS += CSWpm-text-template
RUNTIME_DEP_PKGS += CSWpm-universal-require
RUNTIME_DEP_PKGS += CSWpm-xml-treepp
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
CHECKPKG_OVERRIDES += surplus-dependency|CSWperl

DOCLIST = LICENSE Changes README THANKS

include gar/category.mk

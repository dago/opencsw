# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fusioninventory-agent
VERSION = 2.3.6
GARTYPE = v2
CATEGORIES = cpan

DESCRIPTION = FusionInventory agent
define BLURB
  The fusioninventory agent is a generic agent, running on each managed node. It
  can perform a certain number of tasks, either according to its own execution
  plan, or as requested from a central control server, such as GLPI server with
  fusioninventory plugin.
endef

MASTER_SITES = $(CPAN_MIRRORS)
AUTHOR = GROUSSE
MODDIST =
DISTNAME = FusionInventory-Agent-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += fusioninventory-agent.cron
DISTFILES += fusioninventory-agent.default

UPSTREAM_MASTER_SITES = http://forge.fusioninventory.org/projects/fusioninventory-agent/files

LICENSE = LICENSE
ARCHALL = 1

PACKAGES  = CSWfi-agent
SPKG_DESC_CSWfi-agent = The FusionInventory agent
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-file-which
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-io-socket-ssl
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-proc-daemon
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-proc-pid-file
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-net-ip
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-text-template
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-universal-require
RUNTIME_DEP_PKGS_CSWfi-agent += CSWpm-xml-treepp
# no PKGFILES, to catch all other files
OBSOLETED_BY_CSWfi-agent = CSWfusioninventory-agent
CHECKPKG_OVERRIDES_CSWfi-agent += surplus-dependency|CSWperl

PACKAGES += CSWfi-agent-task-inventory
SPKG_DESC_CSWfi-agent-task-inventory = Local inventory support for FusionInventory agent
RUNTIME_DEP_PKGS_CSWfi-agent-task-inventory = CSWfi-agent
# not available in 5.9
ifneq ($(shell /usr/bin/uname -r),5.9) 
    RUNTIME_DEP_PKGS_CSWfi-agent-task-inventory += CSWpm-net-cups
endif
PKGFILES_CSWfi-agent-task-inventory  = $(bindir)/fusioninventory-inventory
PKGFILES_CSWfi-agent-task-inventory += $(mandir)/man1/fusioninventory-inventory.1
PKGFILES_CSWfi-agent-task-inventory += $(datadir)/fusioninventory/lib/FusionInventory/Agent/Task/Inventory.*
CHECKPKG_OVERRIDES_CSWfi-agent-task-inventory += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWfi-agent-task-inventory += archall-with-arch-paths|/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory/BSD/Archs/i386.pm
CHECKPKG_OVERRIDES_CSWfi-agent-task-inventory += archall-with-arch-paths|/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory/Linux/Archs/i386.pm

PACKAGES += CSWfi-agent-task-wakeonlan
SPKG_DESC_CSWfi-agent-task-wakeonlan = Wake-on-lan support for FusionInventory agent
RUNTIME_DEP_PKGS_CSWfi-agent-task-wakeonlan = CSWfi-agent
PKGFILES_CSWfi-agent-task-wakeonlan  = $(bindir)/fusioninventory-wakeonlan
PKGFILES_CSWfi-agent-task-wakeonlan += $(mandir)/man1/fusioninventory-wakeonlan.1
PKGFILES_CSWfi-agent-task-wakeonlan += $(datadir)/fusioninventory/lib/FusionInventory/Agent/Task/WakeOnLan.pm
CHECKPKG_OVERRIDES_CSWfi-agent-task-wakeonlan += surplus-dependency|CSWperl

PACKAGES += CSWfi-agent-task-esx
SPKG_DESC_CSWfi-agent-task-esx = ESX inventory support for FusionInventory agent
RUNTIME_DEP_PKGS_CSWfi-agent-task-esx = CSWfi-agent
PKGFILES_CSWfi-agent-task-esx  = $(bindir)/fusioninventory-esx
PKGFILES_CSWfi-agent-task-esx += $(mandir)/man1/fusioninventory-esx.1
PKGFILES_CSWfi-agent-task-esx += $(datadir)/fusioninventory/lib/FusionInventory/Agent/Task/ESX.pm
CHECKPKG_OVERRIDES_CSWfi-agent-task-esx += surplus-dependency|CSWperl

PACKAGES += CSWfi-agent-task-network
SPKG_DESC_CSWfi-agent-task-network = Network discovery and inventory support for FusionInventory agent
RUNTIME_DEP_PKGS_CSWfi-agent-task-network  = CSWfi-agent
RUNTIME_DEP_PKGS_CSWfi-agent-task-network += CSWpm-net-snmp
PKGFILES_CSWfi-agent-task-network  = $(bindir)/fusioninventory-netdiscovery
PKGFILES_CSWfi-agent-task-network += $(bindir)/fusioninventory-netinventory
PKGFILES_CSWfi-agent-task-network += $(mandir)/man1/fusioninventory-netdiscovery.1
PKGFILES_CSWfi-agent-task-network += $(mandir)/man1/fusioninventory-netinventory.1
PKGFILES_CSWfi-agent-task-network += $(datadir)/fusioninventory/lib/FusionInventory/Agent/Task/NetDiscovery.*
PKGFILES_CSWfi-agent-task-network += $(datadir)/fusioninventory/lib/FusionInventory/Agent/Task/NetInventory.*
PKGFILES_CSWfi-agent-task-network += $(datadir)/fusioninventory/lib/FusionInventory/Agent/SNMP.*
CHECKPKG_OVERRIDES_CSWfi-agent-task-network += surplus-dependency|CSWperl

PACKAGES += CSWfi-agent-task-deploy
SPKG_DESC_CSWfi-agent-task-deploy = Software deployment support for FusionInventory agent
RUNTIME_DEP_PKGS_CSWfi-agent-task-deploy = CSWfi-agent
PKGFILES_CSWfi-agent-task-deploy  = $(datadir)/fusioninventory/lib/FusionInventory/Agent/Task/Deploy.*
CHECKPKG_OVERRIDES_CSWfi-agent-task-deploy += surplus-dependency|CSWperl

CONFIGURE_ARGS = PREFIX=/opt/csw SYSCONFDIR=/etc/opt/csw/fusioninventory LOCALSTATEDIR=/var/opt/csw/fusioninventory

# skip tests
SKIPTEST ?= 1

# ensure usage of gnu coreutils install
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

# checkpkg overrides
#CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/fusioninventory/lib/FusionInventory/Agent/Task/Inventory.pm

DOCLIST = LICENSE Changes README THANKS

CRONTABS = /etc/opt/csw/pkg/CSWfi-agent/crontabs/root

post-install-modulated:
	/opt/csw/gnu/install -D -m 644 $(WORKDIR)/fusioninventory-agent.cron $(DESTDIR)/etc/opt/csw/pkg/CSWfi-agent/crontabs/root
	/opt/csw/gnu/install -D -m 644 $(WORKDIR)/fusioninventory-agent.default $(DESTDIR)/etc/opt/csw/default/fusioninventory-agent

include gar/category.mk

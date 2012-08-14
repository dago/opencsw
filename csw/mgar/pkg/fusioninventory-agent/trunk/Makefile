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

MASTER_SITES = $(CPAN_MIRRORS)
AUTHOR = FUSINV
DISTNAME = FusionInventory-Agent-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

PACKAGES = CSWfusioninventory-agent
ARCHALL = 1

RUNTIME_DEP_PKGS_CSWfusioninventory-agent  = CSWperl
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_compress_zlib
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_digest_md5
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_file_which
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_http_daemon
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_io_socket_ssl
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_libwww_perl
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_proc_daemon
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_proc_pid_file
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_net_cups
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_net_ip
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_text_template
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_universal_require
RUNTIME_DEP_PKGS_CSWfusioninventory-agent += CSWpm_xml_treepp

CONFIGURE_ARGS = PREFIX=/opt/csw SYSCONFDIR=/etc/opt/csw

# skip tests
SKIPTEST ?= 1

# ensure usage of gnu coreutils install
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

DOCLIST = LICENSE Changes README THANKS

include gar/category.mk

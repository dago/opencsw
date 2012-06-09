NAME = Net-SSH2
VERSION = 0.45
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RKITOVER

DESCRIPTION = Support for the SSH2 protocol via libssh2
define BLURB
  Support for the SSH2 protocol via libssh2
endef

DISTFILES += COPYING

PACKAGES = CSWpm-net-ssh2
SPKG_DESC_CSWpm-net-ssh2 = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-net-ssh2 = CSWpmnetssh2
CATALOGNAME_CSWpmnetssh2 = pm_net_ssh2_stub

RUNTIME_DEP_PKGS_CSWpm-net-ssh2 += CSWlibssh2-1
RUNTIME_DEP_PKGS_CSWpm-net-ssh2 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpm-net-ssh2 += CSWlibz1

CONFIGURE_ARGS = lib=/opt/csw/bdb48/lib include=/opt/csw/bdb48/include

include gar/category.mk

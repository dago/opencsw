NAME = clusterssh
VERSION = 3.28
CATEGORIES = net

DESCRIPTION = ClusterSSH controls a number of xterm windows via a single graphical console window
define BLURB
  ClusterSSH controls a number of xterm windows via a single graphical console
  window to allow commands to be interactively run on multiple servers over an
  ssh connection.
endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89139
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

RUNTIME_DEP_PKGS  = CSWperl
RUNTIME_DEP_PKGS += CSWpmtk
RUNTIME_DEP_PKGS += CSWpmx11protocol
# RUNTIME_DEP_PKGS += CSWossh

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)

# Not gonna do it
TEST_SCRIPTS =

include gar/category.mk

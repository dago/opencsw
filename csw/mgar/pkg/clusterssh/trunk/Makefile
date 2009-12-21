GARNAME = clusterssh
GARVERSION = 3.28
CATEGORIES = net

DESCRIPTION = ClusterSSH controls a number of xterm windows via a single graphical console window
define BLURB
  ClusterSSH controls a number of xterm windows via a single graphical console
  window to allow commands to be interactively run on multiple servers over an
  ssh connection.
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89139
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

REQUIRED_PKGS  = CSWperl
REQUIRED_PKGS += CSWpmtk
REQUIRED_PKGS += CSWpmx11protocol
# REQUIRED_PKGS += CSWossh

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)

# Not gonna do it
TEST_SCRIPTS =

include gar/category.mk

GARNAME = clusterssh
GARVERSION = 3.25
CATEGORIES = net

DESCRIPTION = ClusterSSH controls a number of xterm windows via a single graphical console window
define BLURB
	ClusterSSH controls a number of xterm windows via a single graphical console window to allow commands to be interactively run on multiple servers over an ssh connection.
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclusterssh,)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89139
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

REQUIRED_PKGS = CSWperl CSWpmtk CSWpmx11protocol

PREFIX = /opt/csw/
CONFIGURE_ARGS = --prefix=$(PREFIX)

# Not gonna do it
TEST_SCRIPTS =

include gar/category.mk


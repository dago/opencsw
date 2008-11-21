GARNAME = clusterssh
GARVERSION = 3.22
CATEGORIES = net

DESCRIPTION = ClusterSSH controls a number of xterm windows via a single graphical console window
define BLURB
	ClusterSSH controls a number of xterm windows via a single graphical console window to allow commands to be interactively run on multiple servers over an ssh connection.
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclusterssh,)

PREFIX = /opt/csw/
CONFIGURE_ARGS = --prefix=$(PREFIX)

# Not gonna do it
TEST_SCRIPTS =

include ../category.mk


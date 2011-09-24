NAME = prosody
VERSION = 0.8.2
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = A simple extensible XMPP server written in Lua
define BLURB
  Prosody is a flexible communications server for Jabber/XMPP written in Lua. It
  aims to be easy to use, and light on resources. For developers it aims to be
  easy to extend and give a flexible system on which to rapidly develop added
  functionality, or prototype new protocols.
endef

VENDOR_URL = http://prosody.im
MASTER_SITES = http://prosody.im/downloads/source/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES += 0001-configure-shell.patch
PATCHFILES += 0001-Makefile-test.patch

#CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS  = --prefix=/opt/csw
CONFIGURE_ARGS += --datadir=/var/opt/csw/$(NAME)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw/$(NAME)

SKIPTEST = 1

RUNTIME_DEP_PKGS_CSWprosody += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWprosody += CSWosslrt
RUNTIME_DEP_PKGS_CSWprosody += CSWlibidn11
RUNTIME_DEP_PKGS_CSWprosody += CSWlua

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

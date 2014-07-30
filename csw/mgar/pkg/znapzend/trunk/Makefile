# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = znapzend
VERSION = 0.8.6
GARTYPE = v2

GARCOMPILER = GCC4

DESCRIPTION = The Multilevel Backup Tool for ZFS
define BLURB
  ZnapZend is a ZFS centric backup tool. It relies on snapshot, send and receive todo its work. It has the built-in ability to to manage both local snapshots as well as remote copies by thining them out as time progresses.
  The ZnapZend configuration is stored as properties in the ZFS filesystem itself.
endef

GITHUB_USER  = oetiker
#MASTER_SITES = $(GITHUB_MIRROR)
MASTER_SITES = https://github.com/$(GITHUB_USER)/$(NAME)/releases/download/v$(VERSION)/
VENDOR_URL   = http://www.znapzend.org/

DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD_DEP_PKGS = CSWpm-pod-simple
BUILD_DEP_PKGS = CSWpm-mojolicious

RUNTIME_DEP_PKGS = CSWpm-pod-simple
RUNTIME_DEP_PKGS = CSWpm-mojolicious

include gar/category.mk


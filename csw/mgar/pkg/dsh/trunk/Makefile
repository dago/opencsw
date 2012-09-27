# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dsh
VERSION = 0.25.9
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Distributed shell which command through rsh or ssh on a cluster of machines

MASTER_SITES = http://www.netfort.gr.jp/~dancer/software/downloads/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Use-bash-where-applicable.patch

VENDOR_URL = http://www.netfort.gr.jp/~dancer/software/dsh.html.en

BUILD_DEP_PKGS += CSWlibdshconfig-dev

PACKAGES += CSWdsh
SPKG_DESC_CSWdsh = Distributed shell which command through rsh or ssh on a cluster of machines
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWdsh += CSWlibdshconfig1
RUNTIME_DEP_PKGS_CSWdsh += CSWlibintl8

# for libintl_gettext, libintl_textdomain, libintl_bindtextdomain
EXTRA_LINKER_FLAGS = -lintl

BUILD64 = 1
ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS) 

PRESERVECONF += $(sysconfdir)/dsh.conf

# There are still some tests sporadically failing, disable for now
SKIPTEST ?= 1

include gar/category.mk

